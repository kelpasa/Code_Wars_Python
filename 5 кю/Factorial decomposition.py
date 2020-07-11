def primes(n):
    n += 1
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def decomp(n):
    res = []
    for p in primes(n):
        rest = n
        s = 0
        while rest >0:
            j = rest // p
            s += j
            rest = j
        if s > 1:
            res.append(f'{p}^{s}')
        else:
            res.append(str(p))
    return ' * '.join(res)
