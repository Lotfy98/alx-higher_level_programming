#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}".format(122 - i + (i % 2) * 32), end="")
