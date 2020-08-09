'''
https://www.codewars.com/kata/558ffec0f0584f24250000a0/solutions/python
'''

lower = "abcdefghijklmnopqrstuvwxyz"
table = str.maketrans(lower + lower.upper(), lower[::-1] + lower.upper()[::-1])

def decode(stg):
    if not isinstance(stg, str):
        return "Input is not a string"
    return stg.translate(table)
