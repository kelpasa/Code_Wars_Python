'''
Task
A masked number is a string that consists of digits and one asterisk (*) that should be replaced by exactly one digit. Given a masked number s, find all the possible options to replace the asterisk with a digit to produce an integer divisible by 6.

Input/Output
[input] string s

A masked number.

1 ≤ inputString.length ≤ 10000.

[output] a string array

Sorted array of strings representing all non-negative integers that correspond to the given mask and are divisible by 6.
'''

def is_divisible_by_6(s):
    lst = []
    x = 0
    l = 10
    while l != 0:


        a = s.replace("*",str(x))
        if int(a) % 6 == 0:
            if a[0] == '0' and len(a)>1:
                lst.append(a.replace('0','',1))
            else:
                lst.append(a)
        x = x+ 1
        l-=1
    return lst
