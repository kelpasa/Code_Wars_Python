
'''
Task
Given a positive integer as input, return the output as a string in the following format:

Each element, corresponding to a digit of the number, multiplied by a power of 10 in such a way that with the sum of these elements you can obtain the original number.
'''

def simplify(number):

    n = str(number)
    l = len(n)
    s = len(n)
    arr = []
    a = 0

    while l != 0 :
        if l == 1:
            arr.append(n[-1])
        else:
            arr.append(f'{n[a]}*{10 ** (s - 1 - a)}')

        a += 1
        l -= 1

    return '+'.join([i for i in arr if i[0] != '0'])

