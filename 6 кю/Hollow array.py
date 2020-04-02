'''
An array is said to be hollow if it contains 3 or more 0s in the middle that are preceded and followed by the same number of non-zero elements. Furthermore, all the zeroes in the array must be in the middle of the array.

Write a function named isHollow/is_hollow/IsHollow that accepts an integer array and returns true if it is a hollow array,else false.
'''
def is_hollow(x):
    if len(x)<3:
        return False
    z = 0    
    for i,(a,b) in enumerate(zip(x,x[::-1])):
        if i>len(x)//2:
            return z>=2
        if (a==0) != (b==0):
            return False
        if a!=0 and z>0:
            return False
        if a==0:
            z += 1
        elif z>0:
            return False
