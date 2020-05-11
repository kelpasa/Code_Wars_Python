'''
SMS messages are limited to 160 characters. It tends to be irritating, especially when freshly written message is 164 characters long. Your task is to shorten the message to 160 characters, starting from end, by replacing spaces with camelCase, as much as necessary.

For example:

Original message (169 chars):

No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it.

Shortened message (160 chars):

No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt.
'''



def shortener(mes):
    if len(mes) <= 160:
        return mes
    if not ' ' in mes:
        return mes
    mes = mes[::-1]
    pos = mes.find(' ')
    mes = mes[:pos-1] + mes[pos-1].upper() + mes[pos+1:]
    return shortener(mes[::-1])
