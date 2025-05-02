# This is a python script that generates HTML screencaps documentation for the Bus Pirate terminal interface.
# Loads a list of commands to run in the Bus Pirate terminal over a serial connection.
# Input commands are one per lines, and are read from a file.
#    # tut-self-test.json
#    m # m - change to HiZ mode
#    1
#    ~ # ~ - start self-test
#    # stop
# Example script. # <filename> begins a new snippet file, and # stop closes it.
# Other lines are commands to be sent to the Bus Pirate terminal, text after # is ignored
#
# The script uses the pyserial library to communicate with the Bus Pirate over a serial port.
# It sends the commands to the Bus Pirate and captures the output.
# The next command is sent after the previous command has completed when the >\r\n prompt is received.
#
# Captures the VT100 output stream and converts snippets to HTML
import argparse
from serial import Serial
import json
import time
import re
import random  # For simulating human typing
from collections import deque  # For managing the send queue
from ansi2html import *


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate asciinema screencast documentation for the Bus Pirate terminal interface.")
    parser.add_argument("-p", "--port", default="/dev/ttyUSB0", help="The serial port to use (default: /dev/ttyUSB0)")
    parser.add_argument("-b", "--baudrate", type=int, default=115200, help="The baud rate to use (default: 115200)")
    parser.add_argument("-i", "--input", default="commands.txt", help="The input file containing the commands to run (default: commands.txt)")
    parser.add_argument("-o", "--output", default="../static/snippets/", help="Where to save the asciinema json files (default: ../static/snippets/)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode (default: False)")
    return parser.parse_args()

def read_commands(input_file):
    with open(input_file, "r") as file:
        return [line.strip() for line in file if line.strip()]

def main():
    args = parse_arguments()
    commands = read_commands(args.input)
    html_file = None
    start_time = None
    timestamp = 0
    
    # States
    STATE_IDLE = 0
    STATE_SEND_COMMAND = 1
    STATE_EXECUTE_COMMAND = 2
    STATE_WAIT_FOR_PROMPT = 3
    STATE_ADDITIONAL_DELAY = 4
    STATE_END = 5

    state = STATE_IDLE  # Initial state
    send_queue = deque()
    delay_time = 0

    vt100_query = "\0337\033[999;999H\033[6n\0338"
    vt100_reply = "[24;80R"   
    vt100_data_last = "" 

    with Serial(args.port, args.baudrate, timeout=1) as serial_conn:
        if args.debug:
            print(f"Connected to {args.port} at {args.baudrate} baud.")

        output = ""            
        html_output = ""
        current_command = None  # Track the current command being processed
        current_filename = None  # Track the current filename being processed   
        while state != STATE_END:
            
            # Read data from the serial connection
            data = serial_conn.read(serial_conn.in_waiting).decode("utf-8", errors="ignore")
            if data:
                if args.debug:
                    print(data, end="")
                
                # write the data to the asciinema file
                if html_file:
                    output = output + data

                # Handle VT100 query
                vt100_search = vt100_data_last + data # combine the last data with the current data to find the VT100 query
                if vt100_query in vt100_search:
                    serial_conn.write(vt100_reply)
                    vt100_data_last = "" # reset the last data
                    if args.debug:
                        print(f"VT100 query detected")
                        print(f"Sent VT100 reply")
                else: # save the previous data to find VT100 query split over multiple reads
                    vt100_data_last = data # save the current data to find the VT100 query
                
            # State machine
            if(state == STATE_IDLE):
                if not commands:
                    state = STATE_END
                    continue

                # get next line, split on # to get the command and comment
                line = commands.pop(0)
                if "#" in line:
                    current_command = line.split("#")[0].strip()
                    current_comment = line.split("#")[1].strip()

                    # handle control actions if command is empty
                    if current_command == "": #this is a control action
                        if current_comment == "stop":
                            
                            if html_file is None:
                                print("No file to close.")
                                quit(1)

                            # close the file
                            try:
                                #remove beginning empty lines
                                output = re.sub(r"^\s*\n", "", output) # remove empty lines at the beginning
                                output = output.replace(" ", "&nbsp;") # replace spaces with &nbsp;
                                #remove unprinted character \x03
                                output = output.replace("\x03", "")
                                output = output.replace("\x07", "") # bell
                                output = output.replace("\x0d", "") # remove backspace characters
                                # The converter, which was ported to PYTHON from JS by Copilot, 
                                # is not accept the raw vt100 input in our variable.
                                # It needs to be written to a file first, then read back in.
                                # This is a workaround for the converter to work.
                                converter = AnsiToHtml()
                                html_file.write(output)
                                html_file.close()      
                                html_file = open(current_filename + '.vt1', "r")                     
                                vt100_in = html_file.read()
                                html_output = converter.to_html(vt100_in)
                                html_file.close()
                                html_file = open(current_filename + '.html', "w")
                                html_file.write(html_output)
                                html_file.close()
                                html_file = None
                                if args.debug:
                                    print(f"Closed file.")
                            except Exception as e:
                                print(f"Error closing file: {e}")
                                quit(1)
                                
                        else:
                            # create a new save file
                            if html_file is not None:
                                print("File already open. Closing it first.")
                                try:
                                    # convert to HTML then save
                                    html_file.write('[' + str(round(time.time() - start_time, 6)+2) + ', "o", ""]\n')
                                    html_file.close()
                                    html_file = None
                                except Exception as e:
                                    print(f"Error closing file: {e}")
                                    quit(1)
                            try:
                                current_filename = args.output + current_comment.strip()
                                html_file = open(args.output + current_comment.strip()+'.vt1', "w")
                                output = ""
                                char = "\r\n"
                                serial_conn.write(char.encode("utf-8"))
                                state = STATE_WAIT_FOR_PROMPT
                                if args.debug:
                                    print(f"Saving output to {current_comment}.")
                            except Exception as e:
                                print(f"Error opening {current_comment}: {e}")
                                quit(1)
                        continue
                        
                else:
                    current_command = line

                serial_conn.write(current_command.encode("utf-8"))
                serial_conn.write("\r\n".encode("utf-8"))
                state = STATE_WAIT_FOR_PROMPT

            elif(state == STATE_WAIT_FOR_PROMPT):
                # Handle prompt detection
                if "\x03" in data:
                    state = STATE_IDLE
                    if args.debug:
                        print(f"Prompt detected")

            elif(state == STATE_END):
                if args.debug:
                    print(f"End of commands reached.")


if __name__ == "__main__":
    main()