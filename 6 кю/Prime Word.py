'''
Your task
X and Y are playing a game. A list will be provided which contains n pairs of strings and integers. They have to add the integeri to the ASCII values of the stringi characters. Then they have to check if any of the new added numbers is prime or not. If for any character of the word the added number is prime then the word will be considered as prime word.

Can you help X and Y to find the prime words?

Example:
prime_word([["Emma", 30], ["Liam", 30]])  ->  [1, 1]
'''

def ASCII(arr,n):
    return [ord(i)+n for i in arr]

def prime(arr):
    return [i for i in arr if IsPrime(i) != None]

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return n


def prime_word(array):
    arr = []
    for i in range(len(array)):
        arr.append(ASCII(array[i][0],array[i][1]))
    lst = []
    for i in range(len(arr)):
        lst.append(prime(arr[i]))
    res = []
    for i in range(len(lst)):
        if lst[i] != []:
            res.append(1)
        else:
            res.append(0)
    return res
