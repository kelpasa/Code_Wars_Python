'''
https://www.codewars.com/kata/57a153e872292d7c030009d4/train/python
'''

def simple_transposition(text):
    lst1 = []
    lst2 = []
    for i in range(len(text)):
        if i % 2 == 0:
            lst1.append(text[i])
        else:
            lst2.append(text[i])

    return ''.join(lst1)+''.join(lst2)
