'''
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:

2332
110011
54322345

You'll be given 2 numbers as arguments: (num,s). Write a function which returns an array of s number of numerical palindromes that come after num. If num is a palindrome itself, it should be included in the count.

Return "Not valid" instead if any one of the inputs is not an integer or is less than 0.'''
def palindrome(n, count):
    if not (isinstance(n, int) and isinstance(count, int)) or n < 0 or count < 0:
        return "Not valid"
    result = []
    if n < 11:
        n = 11
    while count:
        s = str(n)
        if s == s[::-1]:
            result.append(n)
            count -= 1
        n += 1
    return result
