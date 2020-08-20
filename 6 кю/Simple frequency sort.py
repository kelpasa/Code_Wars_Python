'''
https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/solutions/python/me/best_practice
'''


def solve(arr):
    return sorted(sorted(arr), key=lambda x: arr.count(x), reverse=True)
