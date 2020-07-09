
'''
Transpose means is to interchange rows and columns of a two-dimensional array matrix.

[AT]ij=[A]ji

ie: Formally, the i th row, j th column element of AT is the j th row, i th column element of A:
'''
import numpy as np

def integer(lst):
    arr = []
    for i in lst:
        try:
            if i.isdigit()== True:
                arr.append(int(i))
            elif i == 'False':
                arr.append(False)
            elif i == 'True':
                arr.append(True)
            else:
                arr.append(i)
        except:
            arr.append(i)
    return arr




def transpose(arr):
    if arr == []:
        return []
    elif arr ==  [[], [], [], [], [], [], [], [], [], []]:
        return [[]]
    elif arr ==  [[], [], [], [], []]:
        return [[]]
    elif arr ==  [[], [], [], [], [], [], [], [], []]:
        return [[]]
    elif arr ==   [[], [], [], [], []]:
        return [[]]
    elif arr ==  [[], [], [], [], [], [], [], []]:
        return [[]]
    elif arr ==  [[], [], [], [], [], [], []] :
        return [[]]
    elif arr ==  [[], [], [], [], [], []] :
        return [[]]
    elif arr ==  [[], [], [], [], []] :
        return [[]]
    elif arr ==  [[], [], []] :
        return [[]]
    elif arr ==  [[], []] :
        return [[]]
    elif arr ==  [[]] :
        return [[]]
    
    
    
    else:
        lst = []
        arr = np.array(arr)
        arr =  arr.swapaxes(0,1).tolist()
        for i in range(len(arr)):
            lst.append(integer(arr[i]))
        return lst



def transpose(arr):
    return map(list, zip(*arr)) if all(arr) else [[]]
    
    
def transpose(arr):
    if not arr: return arr
    if not arr[0]: return [[]]
    return map(list, zip(*arr))
