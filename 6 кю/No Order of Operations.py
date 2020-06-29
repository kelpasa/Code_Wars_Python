'''
Imagine if there were no order of operations. Instead, you would do the problem from left to right. For example, the equation a +b *c /da+b∗c/d would become (((a+b)*c)//d)(((a+b)∗c)//d) (Math.floor(((a+b)*c)/d) in JS). Return None/null (depending on your language) if the equation is "".

Task:
Given an equation with a random amount of spaces greater than or equal to zero between each number and operation, return the result without order of operations. Note that if two numbers are spaces apart, act as if they were one number: 1 3 = 13. However, if given something % 0 or something / 0, return None/null.
'''


import re

def no_order(equation):
    try:
        equation = equation.replace(' ','')
        res1 = re.findall(r'\w+',equation)
        res2 = re.findall(r'[+ \- * / ^ %]',equation)


        result = 0
        try:
            if res2[0] == '+':
                result = int(res1[0]) + int(res1[1])
            elif res2[0] == '-':
                result = int(res1[0]) - int(res1[1])
            elif res2[0] == '*':
                result = int(res1[0]) * int(res1[1])
            elif res2[0] == '/':
                result = int(res1[0]) // int(res1[1])
            elif res2[0] == '^':
                result = int(res1[0]) ** int(res1[1])
            elif res2[0] == '%':
                result = int(res1[0]) % int(res1[1])
        except IndexError:
            return int(equation)
        a = 1
        b = 2
        l = len(res2)-1
        while l != 0:
            if res2[a] == '+':
                result += int(res1[b])
            elif res2[a] == '-':
                result -= int(res1[b])
            elif res2[a] == '*':
                result *= int(res1[b])
            elif res2[a] == '/':
                result //= int(res1[b])
            elif res2[a] == '^':
                result **= int(res1[b])
            elif res2[a] == '%':
                result %= int(res1[b])

            b += 1
            a += 1
            l -= 1


        return result
    except ZeroDivisionError:
        return None
