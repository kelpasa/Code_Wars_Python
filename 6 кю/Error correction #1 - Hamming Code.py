'''
Background information
The Hamming Code is used to correct errors, so-called bit flips, in data transmissions. Later in the description follows a detailed explanation of how it works. In this Kata we will implement the Hamming Code with bit length 3, this has some advantages and disadvantages:

✓ Compared to other versions of hamming code, we can correct more mistakes
✓ It's simple to implement
x The size of the input triples


https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/python
'''

def encode(string):
    return ''.join(['{0:08b}'.format(i) for i in [ord(i) for i in string]]).replace('1','111').replace('0','000')

def decode(bits):
    res = list(map(''.join, zip(*[iter(bits)]*3)))
    lst = []
    for i in res:
        if i.count('1')>i.count('0'):
            lst.append('1')
        else:
            lst.append('0')

    return  ''.join([chr(i) for i in [int(i,2) for i in list(map(''.join, zip(*[iter(''.join(lst))]*8)))]])
