'''
Find the sum of the digits of all the numbers from 1 to N (both ends included).

Examples
# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46
'''
from itertools import chain
def compute_sum(n):

    return sum([int(i) for i in (list(chain(*[list(str(i)) for i in range(1,n+1)])))])
