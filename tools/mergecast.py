import json
import argparse

def merge_asciinema(file1, file2, output_file):
    # Helper function to load screencast data line by line
    def load_screencast(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        header = json.loads(lines[0])  # First line is the header
        data = [json.loads(line) for line in lines[1:]]  # Remaining lines are data
        return header, data

    # Load the first screencast
    header1, data1 = load_screencast(file1)
    
    # Load the second screencast
    header2, data2 = load_screencast(file2)
    
    # Calculate the time offset for the second screencast
    if data1:
        last_timestamp = float(data1[-1][0])
    else:
        last_timestamp = 0.0
    
    # Adjust timestamps in the second screencast
    for entry in data2:
        entry[0] = f"{float(entry[0]) + last_timestamp:.6f}"
    
    # Merge the data
    merged_data = data1 + data2
    
    # Save the merged screencast to the output file
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(json.dumps(header1) + "\n")  # Write the header
        for entry in merged_data:
            out.write(json.dumps(entry) + "\n")  # Write each data entry
    
    print(f"Merged screencast saved to {output_file}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Merge two Asciinema v2 screencasts.")
    parser.add_argument("file1", help="Path to the first screencast file.")
    parser.add_argument("file2", help="Path to the second screencast file.")
    parser.add_argument("output_file", help="Path to save the merged screencast file.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the merge function with the provided arguments
    merge_asciinema(args.file1, args.file2, args.output_file)