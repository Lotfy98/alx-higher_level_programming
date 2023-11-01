#!/usr/bin/python3
output = ""
for i in range(97, 123):
    if i not in [101, 113]:
        output += chr(i)
print("{}".format(output), end="")
