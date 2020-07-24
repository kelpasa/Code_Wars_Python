'''
https://www.codewars.com/kata/565c4e1303a0a006d7000127/train/python
'''


from textwrap import wrap
def number_format(n):
    if n < 0 :
        n = wrap(str(abs(n))[::-1],3)
        return '-'+','.join([i[::-1] for i in n[::-1]])
    else:
        n = wrap(str(n)[::-1], 3)
        return ','.join([i[::-1] for i in n[::-1]])
