

from math import factorial as fac

def exact_p(g1, g2):
    l = len(g1)
    return 2 * fac(l)**2 / fac(2*l)
    
