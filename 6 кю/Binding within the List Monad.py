'''
https://www.codewars.com/kata/546e416c8e3b6bf82f0002f2/train/python
'''

def bind(lst,func):
    lst = [i for i in map(func,lst)]
    arr = []
    for i in lst:
        for j in i:
            arr.append(j)
    return arr
