'''
https://www.codewars.com/kata/550f22f4d758534c1100025a/solutions/python
'''

def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    res = []
    for i in arr:
        if res and dict[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res
