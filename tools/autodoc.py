# This is a python script that generates documentation for the Bus Pirate terminal interface.
# Loads a list of commands to run in the Bus Pirate terminal over a serial connection.
# Input commands are one per lines, and are read from a file.
# The script uses the pyserial library to communicate with the Bus Pirate over a serial port.
# It sends the commands to the Bus Pirate and captures the output.
# The next command is sent after the previous command has completed when the >\r\n prompt is received.
#
# Captures the VT100 output to asciinema formatted text files:
# [ <timestamp>, "o", data]
# data is a string containing the data that was printed. 
# It must be valid, UTF-8 encoded JSON string as described in JSON RFC section 2.5, 
# with any non-printable Unicode codepoints encoded as \uXXXX
#
# Also decode VT100 to HTML and save to a file for use in the documentation.
# The script is designed to be run from the command line with the following arguments:
# -h, --help: show this help message and exit
# -p, --port: the serial port to use (default: /dev/ttyUSB0)
# -b, --baudrate: the baud rate to use (default: 115200)
# -i, --input: the input file containing the commands to run (default: commands.txt)
# -f, --file: the file to save the output to (default: bus_pirate_output.json)
# -d, --debug: enable debug mode (default: False)

import argparse
from serial import Serial
import json
import time
import re
import random  # For simulating human typing
from collections import deque  # For managing the send queue

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate documentation for the Bus Pirate terminal interface.")
    parser.add_argument("-p", "--port", default="/dev/ttyUSB0", help="The serial port to use (default: /dev/ttyUSB0)")
    parser.add_argument("-b", "--baudrate", type=int, default=115200, help="The baud rate to use (default: 115200)")
    parser.add_argument("-i", "--input", default="commands.txt", help="The input file containing the commands to run (default: commands.txt)")
    parser.add_argument("-f", "--file", default="bus_pirate_output.json", help="The file to save the output to (default: bus_pirate_output.json)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode (default: False)")
    return parser.parse_args()

def read_commands(input_file):
    with open(input_file, "r") as file:
        return [line.strip() for line in file if line.strip()]

def save_asciinema_output(output, timestamp, asciinema_file):
    asciinema_entry = [timestamp, "o", output]
    with open(asciinema_file, "a") as file:
        json.dump(asciinema_entry, file)
        file.write("\n")

def decode_vt100_to_html(output):
    # Simplified VT100 to HTML conversion (expand as needed)
    html_output = output.replace("\033[0m", "").replace("\033[1m", "<b>").replace("\033[31m", "<span style='color:red;'>")
    html_output = re.sub(r"\033\[\d+m", "", html_output)  # Remove other VT100 codes
    return f"<pre>{html_output}</pre>"

def main():
    args = parse_arguments()
    commands = read_commands(args.input)
    asciinema_file = args.file
    html_file = asciinema_file.replace(".json", ".html")
    start_time = None
    prompts = ["\x03"]  # Default list of acceptable prompts

    with open(asciinema_file, "a") as file:
        #add header to asciinema
        #{"version": 2, "width": 80, "height": 21, "timestamp": 1745841708, "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}
        file.write('{"version": 2, "width": 80, "height": 24, "timestamp": ' + str(time.time()) + ', "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}\n')

        with Serial(args.port, args.baudrate, timeout=1) as serial_conn:
            if args.debug:
                print(f"Connected to {args.port} at {args.baudrate} baud.")

            output = ""            
            html_output = ""
            send_queue = deque()  # Queue for characters to send
            current_command = None  # Track the current command being processed
            next_send_time = 0  # Timestamp for when the next character can be sent
            waiting_for_prompt = False  # Flag to indicate waiting for \x03
            newline_scheduled_time = None  # Timestamp for when to send the newline
            additional_delay_end_time = None  # Timestamp for when to end the additional delay
            
            vt100_query = "\0337\033[999;999H\033[6n\0338"
            vt100_reply = "[24;80R"

            while commands or send_queue or waiting_for_prompt or additional_delay_end_time:
                # Add the next command to the send queue if the queue is empty
                if not send_queue and commands and not waiting_for_prompt and not additional_delay_end_time:
                    current_command = commands.pop(0)  # Add newline to simulate Enter
                    send_queue.extend(current_command)  # Add characters to the queue
                    waiting_for_prompt = True  # Set the flag to wait for the prompt
                    if args.debug:
                        print(f"Queueing command: {current_command.strip()}")

                # Send one character at a time from the send queue (non-blocking delay)
                current_time = time.time()
                if send_queue and current_time >= next_send_time:
                    char = send_queue.popleft()
                    serial_conn.write(char.encode("utf-8"))
                    if args.debug:
                        print(f"Sent: {char}\n", end="")
                    # Set the next send time based on a random delay
                    next_send_time = current_time + random.uniform(0.1, 0.4)

                    # Schedule the newline to be sent 1 second after the last character
                    if not send_queue:
                        newline_scheduled_time = current_time + 1.0

                # Send the newline (\r\n) if it is scheduled and the time has passed
                if newline_scheduled_time and current_time >= newline_scheduled_time:
                    serial_conn.write("\r\n".encode("utf-8"))
                    if args.debug:
                        print("Sent: \\r\\n")
                    newline_scheduled_time = None  # Reset the schedule                    

                data = serial_conn.read(serial_conn.in_waiting).decode("utf-8", errors="ignore")

                if data:             
                    if start_time is None:
                        start_time = time.time()
                        timestamp = 0
                    else:
                        timestamp = round(time.time() - start_time, 6)

                    # Check if the vt100_query is present in the data
                    if vt100_query in data:
                        if args.debug:
                            print(f"VT100 query detected: {vt100_query}")
                        serial_conn.write(vt100_reply.encode("utf-8"))  # Respond with the VT100 reply
                        if args.debug:
                            print(f"Sent VT100 reply: {vt100_reply}")                        

                    asciinema_entry = [timestamp, "o", data]
                    json.dump(asciinema_entry, file)
                    file.write("\n")
                    
                    if args.debug:
                        print(data, end="")
                    
                    # Check if the prompt (\x03) is present in the output
                    if "\x03" in data:
                        if args.debug:
                            print(f"Prompt detected")
                        waiting_for_prompt = False  # Reset the flag to allow queuing the next command

                        # Schedule the additional delay
                        additional_delay_end_time = current_time + 1.0  # 1-second delay
                        if args.debug:
                            print(f"Scheduled additional delay of 1 second after prompt detection.")

                    # Check if the additional delay is active and skip queuing the next command until it ends
                    if additional_delay_end_time and current_time >= additional_delay_end_time:
                        # Reset the additional delay timer
                        additional_delay_end_time = None


                    output += data
                
                html_output += decode_vt100_to_html(output)

            #final timestamp in ansiinema file
            file.write('[' + str(round(time.time() - start_time, 6)+2) + ', "o", ""]\n')
            
            with open(html_file, "w") as file:
                file.write(html_output)
            
            if args.debug:
                print(f"Output saved to {asciinema_file} and {html_file}.")

if __name__ == "__main__":
    main()