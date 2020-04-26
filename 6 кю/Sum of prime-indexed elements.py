'''
In this Kata, you will be trained on array indexing and basic prime number operations. Array indices are zero-based; this means that the first element of an array is at index 0.

You will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.

To make this interesting, array lengths in random tests will have up to 5000 elements.

Good luck!
'''


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5)+1))

def total(arr):
    return sum(e for i, e in enumerate(arr) if is_prime(i))
    
    
