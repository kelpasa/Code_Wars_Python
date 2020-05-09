'''
https://www.codewars.com/kata/574b448ed27783868600004c/python
'''


import numpy as np


def filter_val(lst):
    l  = len(lst)
    while True:
        U = float(np.average(lst))
        Q = float(np.std(lst))
        mini = U - 2.5 * Q
        maxi = U + 2.5 * Q
        arr = [x for x in lst if mini <= x <= maxi]
        if len(arr) == len(lst):
            s = Q / len(lst)**0.5
            return [[l, len(arr)], U,s]
        else:
            lst =arr
