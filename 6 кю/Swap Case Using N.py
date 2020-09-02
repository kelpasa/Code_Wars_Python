'''
Your job is to change the given string s using a non-negative integer n.

Each bit in n will specify whether or not to swap the case for each alphabetic character in s: if the bit is 1, swap the case; if its 0, leave it as is. When you finished with the last bit of n, start again with the first bit.

You should skip the checking of bits when a non-alphabetic character is encountered, but they should be preserved in their original positions.
'''
def swap(s,n):
    res = bin(n).replace('0b','')*len(s)
    result = ''
    num = 0
    for i in s:
        if i.isalpha():
            if res[num] == '1' and i.islower():
                result += i.upper()
            elif res[num] == '1' and i.isupper():
                result += i.lower()
            elif res[num] == '0' and i.isupper():
                result += i.upper()
            elif res[num] == '0' and i.islower():
                result += i.lower()
            num+=1
        else:
            result += i

    return result
