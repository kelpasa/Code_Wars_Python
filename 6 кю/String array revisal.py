'''
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

dup(["kelless","keenness"]) = ["keles","kenes"].

Strings will be alphabet characters only. Don't worry about lower and upper case. See test cases for more examples.

Good luck!'''


def smash(arr):
    lst = []
    for i in range(len(arr)):
        try:
            if arr[i] != arr[i+1]:
                lst.append(arr[i])
        except IndexError:
            lst.append(arr[-1])
    return ''.join(lst)


def dup(arry):
    lst = []
    for i in arry:
        lst.append(smash(i))
    return lst
    
