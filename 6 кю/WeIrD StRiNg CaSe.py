'''
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''

def up_lw(s):
    new_s = ''
    for i in range(len(s)):
        if i % 2 == 0:
            new_s += s[i].upper()
        else:
            new_s += s[i].lower()
    return new_s


def to_weird_case(string):
    return ' '.join([up_lw(i) for i in string.split()])

