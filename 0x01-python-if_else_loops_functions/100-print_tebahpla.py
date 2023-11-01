#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}".format(97 + i - ((i + 1) % 2) * 32), end="")
