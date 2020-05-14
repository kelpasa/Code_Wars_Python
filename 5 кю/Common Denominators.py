'''https://www.codewars.com/kata/54d7660d2daf68c619000d95/python'''


def convertFracts(lst):
    e = 1
    for i in lst:
        e = lcm(e, i[1])
    return [[int(e/i[1])*i[0], e] for i in lst]
    
def gcd(a,b): 
    if a == 0: 
        return b
    return gcd(b % a, a) 
    
def lcm(a,b): 
    return (a*b) / gcd(a,b)
