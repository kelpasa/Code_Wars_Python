'''
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.
'''
def solution(n):
    result = []
    string = list(str(n))
    length = len(string)
    ref = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
           ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
           ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
           ['M', 'MM', 'MMM', 'MM', 'M', 'MM', 'MMM', 'MMMM', 'MM']
        ]
    for i in range(length):
        if string[i] == '0':
            continue
        else:
            result.append(ref[length - 1 - i][int(string[i]) - 1])      
    return ''.join(result)
