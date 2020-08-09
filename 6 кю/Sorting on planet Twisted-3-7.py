'''
https://www.codewars.com/kata/58068479c27998b11900056e/solutions/python
'''

def sort_twisted37(arr):
    def key(x):
        return int(str(x).translate(str.maketrans('37', '73')))
    return sorted(arr, key=key)
