'''
https://www.codewars.com/kata/59098c39d8d24d12b6000020/train/python
'''


def dot(n,m):
    s = '+---'*n+"+"
    n = '| o '*n+'|'
    return f"{s}\n{n}\n"*m+s
