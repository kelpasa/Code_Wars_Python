'''
https://www.codewars.com/kata/51edd51599a189fe7f000015/solutions/python/me/best_practice
'''

def solution(array_a, array_b):
    lst =[]
    for i,j in zip(array_a,array_b):
        lst.append((i-j)**2)
    return sum(lst)/len(lst)
