'''
Many items that are available for sale have a barcode somewhere on them - this allows them to be scanned at a checkout.

Your task is to create an algorithm to convert a series of ones and zeroes from the scanner into an Universal Product Code (UPC). You can learn more about UPC from Wikipedia. We will be using the UPC-A formatting.

'''

from textwrap import wrap
def decode(S):
    return wrap(S,7)


def barcode_scanner(barcode):
    LEFT_HAND = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'

    }
    RIGHT_HAND = {
        '1110010': '0',
        '1100110': '1',
        '1101100': '2',
        '1000010': '3',
        '1011100': '4',
        '1001110': '5',
        '1010000': '6',
        '1000100': '7',
        '1001000': '8',
        '1110100': '9'
    }
    r_lst =[]
    l_lst =[]
    for i in  decode(barcode[3:45]):
        l_lst.append(LEFT_HAND[i])

    for i in  decode(barcode[50:92]):
        r_lst.append(RIGHT_HAND[i])
