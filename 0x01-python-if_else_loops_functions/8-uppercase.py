#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            result += "{:c}".format(ord(str[i]) - 32)
        else:
            result += "{:c}".format(ord(str[i]))
    print(result)
