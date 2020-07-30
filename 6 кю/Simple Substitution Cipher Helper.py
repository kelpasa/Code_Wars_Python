'''
https://www.codewars.com/kata/52eb114b2d55f0e69800078d/train/python
'''

class Cipher(object):

    def __init__(self, map1, map2):
        self.m1 = map1
        self.m2 = map2

    def encode(self, s):
        res = {a:b for a,b in zip(self.m1,self.m2)}
        result = []
        for i in s:
            try:
                result.append(res[i])
            except:
                result.append(i)
        return ''.join(result)
    def decode(self, s):
        res = {a: b for a, b in zip(self.m2, self.m1)}
        result = []
        for i in s:
            try:
                result.append(res[i])
            except:
                result.append(i)
        return ''.join(result)
