'''
Create range generator function that will take up to 3 parameters - start value, step and stop value. This function should return an iterable object with numbers. For simplicity, assume all parameters to be positive numbers.
'''
def range_function(*n):
    if len(n) == 3:
        return [i for i in range(n[0],n[2]+1,n[1])]
    elif len(n) == 2:
        return [i for i in range(n[0],n[1]+1)]
    else:
        return [i for i in range(1,n[0]+1)]
