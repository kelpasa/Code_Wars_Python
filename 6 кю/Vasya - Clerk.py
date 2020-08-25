'''
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
'''

def tickets(people):
    change = {25: 0, 50: 0, 100: 0}
    for money in people:
        if money == 25:
            change[25] += 1
        elif money == 50:
            change[50] += 1
            change[25] -= 1
        elif money == 100:
            change[100] += 1
            if change[50] >= 1:
                change[50] -= 1
                change[25] -= 1
            else:
                change[25] -= 3
        if change[25] + change[50] + change[100] < 0 or change[25] < 0:
            return "NO"

    return "YES"
