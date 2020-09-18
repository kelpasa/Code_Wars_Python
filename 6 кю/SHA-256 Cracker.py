'''
This kata aims to show the vulnerabilities of hashing functions for short messages.

When provided with a SHA-256 hash, return the value that was hashed. You are also given the characters that make the expected value, but in alphabetical order.

The returned value is less than 10 characters long. Return nil for Ruby and Crystal, None for Python, null for Java when the hash cannot be cracked with the given characters.


https://www.codewars.com/kata/587f0abdd8730aafd4000035/python
'''

from itertools import *
import hashlib


def sha256_cracker(hash, chars):
    lst = [''.join(i) for i in permutations(chars)]
    lst =  [(i.encode()) for i in lst]
    arr = []
    for i in lst:
        if hashlib.sha256(i).hexdigest() == hash:
            arr.append(i)
            break
    else:
        return None

    return (arr[-1]).decode()
