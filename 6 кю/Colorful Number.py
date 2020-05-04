'''
Problem
Determine whether a positive integer number is colorful or not.

263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3] are all different; whereas 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6] have 6 twice.

So take all consecutive subsets of digits, take their product and ensure all the products are different.

Examples
263  -->  true
236  -->  false'''

def comp(num):
    res = 1
    for i in str(num):
        res *= int(i)
    return [res]

def decom(num):
    return [int(i) for i in str(num)]

def trip(num):
    x = 0;y = 1;l = len(str(num));lst = []
    while l != 1:
        lst.append(int(str(num)[x])*int(str(num)[y]))
        x += 1;y += 1; l -= 1
    return lst


def colorful(num):
    if num <10:
        return True
    elif 10<= num <100:
        return sorted(sum([comp(num),decom(num)],[]))== sorted(set(sum([comp(num),decom(num)],[])))
    else:
        return sorted(sum([comp(num),decom(num),trip(num)],[])) == sorted(set(sum([comp(num),decom(num),trip(num)],[])))
