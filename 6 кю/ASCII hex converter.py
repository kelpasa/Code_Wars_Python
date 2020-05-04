'''
Write a module Converter that can take ASCII text and convert it to hexadecimal. The class should also be able to take hexadecimal and convert it to ASCII text.

'''

class Converter():

    @staticmethod
    def to_ascii(h):
        from re import findall as fin
        return ''.join([chr(i) for i in ([int(i,16) for i in fin(r'\w\w',h)])])

    @staticmethod
    def to_hex(s):
        return ''.join([hex(i) for i in [ord(i) for i in s]]).replace('0x','')


