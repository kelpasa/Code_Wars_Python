'''
If you reverse the word "emirp" you will have the word "prime". That idea is related with the purpose of this kata: we should select all the primes that when reversed are a different prime (so palindromic primes should be discarded).

For example: 13, 17 are prime numbers and the reversed respectively are 31, 71 which are also primes, so 13 and 17 are "emirps". But primes 757, 787, 797 are palindromic primes, meaning that the reversed number is the same as the original, so they are not considered as "emirps" and should be discarded.
'''
from math import log, ceil

def makeSieveEmirp(n):
    sieve, setPrimes = [0]*n, set()
    for i in range(2, n):
        if not sieve[i]:
            setPrimes.add(i)
            for j in range(i**2, n, i): sieve[j] = 1
    return { n for n in setPrimes if n != int(str(n)[::-1]) and int(str(n)[::-1]) in setPrimes }


def find_emirp(n):
    setEmirp = makeSieveEmirp( 10**(int(ceil(log(n,10)))) )
    crunchL = [p for p in setEmirp if p <= n]
    return [len(crunchL), max(crunchL), sum(crunchL)]
