'''
https://www.codewars.com/kata/586a933fc66d187b6e00031a/train/python
'''



import random
def generateName():
    lst = []
    l = 6
    while l != 0:
        lst.append(chr(random.randint(65,90)))
        l -=1
    return ''.join(lst)
