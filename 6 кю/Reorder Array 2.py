'''
This kata focuses on the Numpy python package and you can read up on the Numpy array manipulation functions here: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html

You will get two integers N and M. You must return an array with two sub-arrays with numbers in ranges [0, N / 2) and [N / 2, N) respectively, each of them being rotated M times.
'''



def call(arr,n):
    while n != 0:
        arr = [arr[-1]]+arr[:-1]
        n -= 1
    return arr

def reorder(a, b):
    return [call([i for i in range(0,a//2)],b),call([i for i in range(a//2,a)],b)]
