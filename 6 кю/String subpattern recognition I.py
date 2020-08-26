'''
https://www.codewars.com/kata/5a49f074b3bfa89b4c00002b/train/python
'''

def has_subpattern(text):
    for i in range(1, len(text) // 2 + 2):
        if len(text) % i == 0:
            subtext = text[:i]
            num_subtext = text.count(subtext)
            if num_subtext > 1 and num_subtext * len(subtext) == len(text):
                return True
    return False
