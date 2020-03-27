'''
In telecomunications we use information coding to detect and prevent errors while sending data.

A parity bit is a bit added to a string of binary code that indicates whether the number of 1-bits in the string is even or odd. Parity bits are used as the simplest form of error detecting code, and can detect a 1 bit error.

In this case we are using even parity: the parity bit is set to 0 if the number of 1-bits is even, and is set to 1 if odd.

We are using them for the transfer of ASCII characters in binary (7-bit strings): the parity is added to the end of the 7-bit string, forming the 8th bit.

In this Kata you are to test for 1-bit errors and return a new string consisting of all of the correct ASCII caracters in 7 bit format (removing the parity bit), or "error" in place of ASCII characters in which errors were detected.
'''

def parity_bit(binary):
    lst =  []

    for i in binary.split():
        if (i.count('1') % 2 == 0 and i[-1] == '0') or (i.count('1') % 2 == 0 and i[-1] == '1'):
            lst.append(i[:-1])
        else:
            lst.append('error')
    
    return ' '.join(lst)
