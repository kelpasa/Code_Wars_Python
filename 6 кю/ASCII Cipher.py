'''
We're going to create a cipher, so that we can send messages to our friends and no one else will know what cool things we're discussing. Our cipher will take two arguments: a key, in the form of an integer, and a message, in the form of a string.

Our first step is to find the largest prime of the key. For example, the prime factorization of 18 is 2 x 3 x 3, so the largest prime is 3. We'll also accept negative integers as keys, so -18 would give us a "largest" prime of -3. Once we've gotten our prime number, we'll encrypt our message.

The way we'll encrypt is to use the base ASCII table values of 0-127. We'll take the ASCII value of every character and add the value of our prime number. For example, the character 'D' has an ASCII value of 68, Adding 3 would give 71, which is 'G'.

So, this will look like the following:

If we're given a key of 18, and a message of "Hello, world", we'll calculate the largest prime to be 3, and then add it to the ASCII values of our string, giving an output of "Khoor/#zruog".

We'll let values greater than 127 or less than 0 "wrap around", and start at the other side of the ASCII table, so a -1 will be considered a 127, and a 128 will be considered a 0.
'''

def factor(n):
    if n > 0:
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        return max(Ans)
    else:
        n = abs(n)
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        return -max(Ans)


def ascii_cipher(message, key):
    arr = []
    for i in message:
        arr.append(ord(i)+factor(key))
    lst = []
    for i in arr:
        if 0 <= i <= 127:
            lst.append(chr(i))
        else:
            i = i % 128
            lst.append(chr(i))

    return ''.join(lst)
