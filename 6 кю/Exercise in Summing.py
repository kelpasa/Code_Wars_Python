'''
https://www.codewars.com/kata/52cd0d600707d0abcd0003eb/train/python
'''

def minimum_sum(values, n):
    return sum(sorted(values,reverse=False)[:n])


def maximum_sum(values, n):
    return sum(sorted(values,reverse=True)[:n])
