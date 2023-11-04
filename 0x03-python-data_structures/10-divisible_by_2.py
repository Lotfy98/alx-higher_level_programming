#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for num in my_list:
        res.append(num % 2 == 0)
    return res
