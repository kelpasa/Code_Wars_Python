'''
In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.

Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:
'''

from collections import deque

def josephus_survivor(items,k):
    items = [i for i in range(1,items+1)]
    d = deque(items)
    res = []
    while len(d) > 0:
        d.rotate(-k)
        res.append(d.pop())
    return res[-1]
