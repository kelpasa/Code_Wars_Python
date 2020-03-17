'''
You are given two strings (st1, st2) as inputs. Your task is to return a string containing the numbers in st2 which are not in str1. Make sure the numbers are returned in ascending order. All inputs will be a string of numbers.'''
def findAdded(st1, st2):
    x = list(st2)
    for i in st1:
        if i not in x:
            pass
        else:
            x.remove(i)
    return ''.join(sorted(x))
