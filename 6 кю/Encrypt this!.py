'''Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''

def encrypt(s):
    return str(ord(s[0]))+s[1:]

def this(s):
    if len(s) > 2:
        return s[0]+s[-1]+s[2:-1]+s[1]
    else:
        return s
    
def encrypt_this(text):
    arr = []
    for i in text.split():
        arr.append(encrypt(this(i)))
    return ' '.join(arr)
