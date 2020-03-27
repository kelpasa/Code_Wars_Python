'''
The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

The result array should be sorted in ascending order of values.

Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.
'''
def twos_difference(lst):
    arr = []

    for i in lst:
        if i+2 in lst:
            arr.append((i,i+2))

    return sorted(arr)
