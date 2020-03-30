'''
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first.

For empty string return:

('', 0)
Happy coding! :)
'''
import re


def longest_repetition(chars):
    if chars == '':
        return '',0
    else:
        res = max(list(w.group(0) for w in re.finditer(r'(.)\1*',chars)),key=len)
        return res[0],len(res)
