'''
https://www.codewars.com/kata/587fb57e12fc6eadf200009b/train/python
'''

import hashlib

def to_sha256(s):
    s = s.encode()
    return hashlib.sha256(s).hexdigest()
