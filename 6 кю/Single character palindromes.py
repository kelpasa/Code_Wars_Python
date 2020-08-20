'''
https://www.codewars.com/kata/5a2c22271f7f709eaa0005d3/train/python
'''

def solve(s):
    if s == s[::-1]:
        return "OK"
    else:
        long = len(s)
        a = 0
        b = 1
        lst = []
        while long != 0:
            lst.append(s[:a]+s[b:])
            a+=1;b+=1;long-=1
        print(lst)
        for i in lst:
            if i == i[::-1]:
                return "remove one"
        else:
            return "not possible"
