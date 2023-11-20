#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in my_list:
        try:
            if counter < x:
                print(i, end="")
                counter++
            else:
                break
        except:
            break
    print()
    return (counter)

