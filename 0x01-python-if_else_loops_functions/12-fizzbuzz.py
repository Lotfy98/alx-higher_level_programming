#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            end_char = "\n" if i == 100 else " "
            print("FizzBuzz", end=endChar)
        elif i % 3 == 0:
            endChar = "\n" if i == 100 else " "
            print("Fizz", end=endChar)
        elif i % 5 == 0:
            endChar = "\n" if i == 100 else " "
            print("Buzz", end=endChar)
        else:
            endChar = "\n" if i == 100 else " "
            print(i, end=endChar)
