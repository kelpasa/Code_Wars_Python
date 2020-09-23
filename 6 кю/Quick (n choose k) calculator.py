'''
You may be familiar with the concept of combinations: for example, if you take 5 cards from a 52 cards deck as you would playing poker, you can have a certain number (2,598,960, would you say?) of different combinations.

In mathematics the number of k combinations you can have taking from a set of n elements is called the binomial coefficient of n and k, more popularly called n choose k.

The formula to compute it is relatively simple: n choose k==n!/(k!*(n-k)!), where ! of course denotes the factorial operator.

You are now to create a choose function that computes the binomial coefficient, like this:

https://www.codewars.com/kata/55b22ef242ad87345c0000b2/train/python
'''

from math import factorial as fc
def choose(n,k):
    if n < k:
        return 0
    else:
        return int(fc(n)//(fc(k)*fc(n-k)))
