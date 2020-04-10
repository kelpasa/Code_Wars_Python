'''
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
'''


import re

def decipher(s):
    return s.replace(''.join(re.findall(r'\d+',s)),chr(int(''.join(re.findall(r'\d+',s)))))

def this(s):
    if len(s) > 2:
        return s[0]+s[-1]+s[2:-1]+s[1]
    else:
        return s

def decipher_this(string):
    arr = []
    lst = []
    for i in string.split():
        arr.append(decipher(i))
    for i in arr:
        lst.append(this(i))
    return ' '.join(lst)
