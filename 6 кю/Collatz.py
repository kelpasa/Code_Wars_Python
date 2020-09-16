'''
https://www.codewars.com/kata/5286b2e162056fd0cb000c20/python
'''

def collatz(n):
    hist=[n]
    res=n
    while res != 1:
        if res % 2 == 0:
            res=res/2
        else:
            res=res*3+1
        hist.append(res)
    return '->'.join([str(i) for i in [int(i) for i in hist]])
