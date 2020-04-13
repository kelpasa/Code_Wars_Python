'''
Take a string str and return a string that is made up of the number of occurances of each english letter in str, followed by that letter. The string shouldn't contain zeros; leave them out.

An empty string, or one with no letters, should return an empty string.

Notes
Ignore all case
str will never be null
Examples
"This is a test sentence."  =>  "1a1c4e1h2i2n4s4t"
""  =>  ""
"555"  =>  ""
FUNDAMENTALSSTRINGSSORTING'''

from re import findall as fin
from collections import Counter as Con


def string_letter_count(s):
    return ''.join([str(j)+i for i,j in sorted(Con(fin(r'[a-zA-Z]',s.lower())).items())])
