'''
Implement a function which behaves like the uniq command in UNIX.

It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

Example:

['a','a','b','b','c','a','b','c'] --> ['a','b','c','a','b','c']
'''



def uniq(seq):
    arr = []
    for i in range(len(seq)):
        try:
            if seq[i] != seq[i+1]:
                arr.append(seq[i])
        except:
            arr.append(seq[i])
    return arr
