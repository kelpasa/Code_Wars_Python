'''
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"
'''
import re
def smash(strinr):
    return sum([ord(i)-96 for i in strinr])


def solve(st):
    res = re.findall(r'[^aeiou]+',st)
    lst = []
    for i in res:
        if len(i) == 1:
            lst.append(ord(i)-96)
        else:
            lst.append(smash(i))

    return max(lst)
