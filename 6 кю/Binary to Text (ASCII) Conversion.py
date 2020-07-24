'''
https://www.codewars.com/kata/5583d268479559400d000064/train/python
'''

from textwrap import wrap
def binary_to_string(binary):
    return ''.join([chr(i) for i in [int(i,2) for i in wrap(binary,8)]])
