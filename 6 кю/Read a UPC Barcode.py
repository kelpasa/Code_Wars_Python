'''
Your task is to convert a string representing the lines/spaces in a 12 digit barcode/UPC-A into a string of numbers 0-9.

A black line represents a 1 and a space represents 0. The string you are returning is the decimal representation of those binary digits. NOTE: The digits 0-9 are not represented as bits the usual way, UPC has it's own tables which are preloaded as LEFT_HAND and RIGHT_HAND dictionaries.

The LEFT_HAND and RIGHT_HAND dictionaries contain 7 digit bit strings as keys and an integer for values. For example:

'0011001' = 1 in LEFT_HAND

'1100110' = 1 in RIGHT_HAND, left and right side bit strings are complements of each other.
'''

from textwrap import wrap


def left_decode(code):
    left = code[3:45]
    s = ''
    for i in left:
        if i == ' ':
            s += '0'
        else:
            s += '1'
    return wrap(s, 7)

def right_code(code):
    right = code[50:92]
    s = ''
    for i in right:
        if i == ' ':
            s += '0'
        else:
            s += '1'

    return  wrap(s, 7)


def read_barcode(barcode):
    LEFT_HAND = {
        '0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9

    }
    RIGHT_HAND = {
        '1110010': 0,
        '1100110': 1,
        '1101100': 2,
        '1000010': 3,
        '1011100': 4,
        '1001110': 5,
        '1010000': 6,
        '1000100': 7,
        '1001000': 8,
        '1110100': 9

    }
    left = left_decode(barcode)
    right = right_code(barcode)
    new_left = ""
    new_right = ""
    for i in left:
        new_left += str(LEFT_HAND[i])
    for i in right:
        new_right += str(RIGHT_HAND[i])

    return f'{new_left[0]} {new_left[1:]} {new_right[0:-1]} {new_right[-1]}'


print(read_barcode('▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'))
