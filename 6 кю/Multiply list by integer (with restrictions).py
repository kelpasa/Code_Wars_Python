'''
Task:
Given a list of integers l, return the list with each value multiplied by integer n.

Restrictions:
The code must not:

contain *.
use eval() or exec()
contain for
modify l
Happy coding :)
'''
def multiply(n, l):
    lst = []
    long = len(l)
    x = 0
    while long != 0:
        lst.append((l[x].__mul__(n)))
        x +=1;long-=1
    return lst
