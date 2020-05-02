'''
Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 2147483647'''

from textwrap import wrap
def group_by_commas(n):

    return ','.join([i[::-1] for i in (wrap(str(n)[::-1],3))][::-1])
