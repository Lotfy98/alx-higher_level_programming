#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, counter = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            counter++
        except (ValueError, TypeError, IndexError):
            continue
        i++
    print()
    return (counter)
