'''
bserve the process with the array given below and the tracking of the sums of each corresponding array.

[5, 3, 6, 10, 5, 2, 2, 1] (34) ----> [5, 3, 6, 10, 2, 1] ----> (27) ------> [10, 6, 5, 3, 2, 1]  ----> [4, 1, 2, 1, 1] (9) -----> [4, 1, 2] (7)
The tracked sums are : [34, 27, 9, 7]. We do not register one of the sums. It is not difficult to see why.

We need the function track_sum(), (trackSum(), Javascript) that receives an array and outputs an array with the following result in the order given below:
'''



def track_sum(arr):
    s1 = sum(arr)
    s2 = sum(set(arr))
    lst = sorted(set(arr),reverse=True)[1:]
    arr = sorted(set(arr),reverse=True)
    arr = ([i-j for i,j in zip(arr,lst)])
    s3 = sum(arr)
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    s4 = sum(res)
    return [[s1,s2,s3,s4],res]
