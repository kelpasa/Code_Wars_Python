'''
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
'''

def add(arr):
    return [int(i) for i in arr]



def pyramid(n):
    arr = []
    for i in range(1,n+1):
        arr.append(list('1'*i))
    lst = []
    for i in arr:
        lst.append(add(i))
    return lst
