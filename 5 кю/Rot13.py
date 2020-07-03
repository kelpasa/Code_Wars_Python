'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''


def rot13(message):
    ASCII = [ord(i) for i in message]
    arr = []
    for i in ASCII:
        if 97<=i<=109 or 65<=i<=77:
            arr.append(chr(i+13))
        elif 110<=i<=122 or 78<=i<=90:
            arr.append(chr(i - 13))
        else:
            arr.append(chr(i))

    return ''.join(arr)
