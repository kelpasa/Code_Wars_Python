'''
https://www.codewars.com/kata/5921c0bc6b8f072e840000c0/python
'''
def sequence_classifier(arr):
    if len(arr) == arr.count(arr[0]):
        return 5
    elif arr == sorted(arr):
        if arr != sorted(list(set(arr))):
            return 2
        return 1
    elif arr == sorted(arr,reverse= True):
        if arr != sorted(list(set(arr)),reverse=True):
            return 4
        return 3
    else:
        return 0

