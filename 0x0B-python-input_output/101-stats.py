#!/usr/bin/python3
import sys
import signal

# Initialize a dictionary to store the count of each status code
status_codes = {}
# Initialize a variable to store the total file size
total_size = 0
# Initialize a counter for the number of lines read
line_count = 0

# Define a signal handler for keyboard interruption (CTRL + C)


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Function to print the statistics


def print_statistics():
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        print("{}: {}".format(status_code, status_codes[status_code]))


# Read from stdin line by line
try:
    for line in sys.stdin:
        # Increment the line count
        line_count += 1
        # Split the line into components
        parts = line.split()
        # Extract the status code and file size from the line
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        # Update the total file size
        total_size += file_size
        # Update the count for the status code
        if status_code not in status_codes:
            status_codes[status_code] = 0
        status_codes[status_code] += 1

        # Print the statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Print the statistics upon keyboard interruption
    print_statistics()
    raise

# Print the final statistics if the end of input is reached
print_statistics()
