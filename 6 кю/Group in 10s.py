'''
Write a function groupIn10s which takes any number of arguments, and groups them into sets of 10s and sorts each group in ascending order.

The return value should be an array of arrays, so that numbers between 0-9 inclusive are in position 0 and numbers 10-19 are in position 1, etc.

Here's an example of the required output:

grouped = group_in_10s(8, 12, 38, 3, 17, 19, 25, 35, 50) 

grouped[0]     # [3, 8]
grouped[1]     # [12, 17, 19]
grouped[2]     # [25]
grouped[3]     # [35, 38]
grouped[4]     # None
grouped[5]     # [50]'''

def group_in_10s(*li):
    li,result,ini,i = sorted(li),[],10,0
    while i < len(li):
        temp = []
        while i < len(li) and li[i] < ini:
            temp.append(li[i]) ; i += 1
        result.append(temp or None) ; ini += 10
    return result
