#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# This script generates log data for testing purposes.
# It simulates the output of a web server by printing
# IP addresses, timestamps, HTTP methods, status codes, and file sizes.

for i in range(10000):
    # Sleep for a random short interval to simulate real-time data generation
    sleep(random.random())
    # Generate a random IP address
    ip_address = "{:d}.{:d}.{:d}.{:d}".format(
        random.randint(1, 255), random.randint(1, 255),
        random.randint(1, 255), random.randint(1, 255)
    )
    # Generate a current timestamp
    timestamp = datetime.datetime.now()
    # Choose a random status code from the provided list
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    # Generate a random file size
    file_size = random.randint(1, 1024)

    # Print the generated log entry to stdout
    sys.stdout.write("{} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        ip_address, timestamp, status_code, file_size
    ))
    # Flush the output to ensure it's printed in real-time
    sys.stdout.flush()
