'''
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.


https://www.codewars.com/kata/526989a41034285187000de4/train/python
'''

def ips_between(start, end):
    res = [i-j for i,j in zip([int(i) for i in end.split('.')], [int(i) for i in start.split('.')])]
    return (res[0]*16777216)+(res[1]*65536)+(res[2]*256)+(res[3]*1)
