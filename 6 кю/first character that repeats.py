'''
Find the first character that repeats in a String and return that character.

first_dup('tweet') => 't'
first_dup('like') => None
This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.
'''
def first_dup(s):
    new_s = ''
    for i in s:
        if s.count(i) == 1:
            new_s += i
            break
    if new_s == '':
        return None
    else:
        return new_s
