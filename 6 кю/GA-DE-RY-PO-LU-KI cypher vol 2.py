'''
The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

 G => A
 g => a
 a => g
 A => G
 D => E
  etc.
The letters, which are not on the list of substitutes, stays in the encrypted text without changes.

Other keys often used by Scouts:

PO-LI-TY-KA-RE-NU
KA-CE-MI-NU-TO-WY
KO-NI-EC-MA-TU-RY
ZA-RE-WY-BU-HO-KI
BA-WO-LE-TY-KI-JU
RE-GU-LA-MI-NO-WY
Task
Your task is to help scouts to encrypt and decrypt thier messages. Write the Encode and Decode functions.

Input/Output
The function should have two parameters.
The message input string consists of lowercase and uperrcase characters and whitespace character.
The key input string consists of only lowercase characters.
The substitution has to be case-sensitive.
'''

def decode(message, key):
    pass
    pass
    key_1 = {i: j for i, j in zip([key[i].lower() for i in range(len(key)) if i % 2 == 0],
                                  [key[i].lower() for i in range(len(key)) if i % 2 == 1])}
    key_2 = {i: j for i, j in zip([key[i].lower() for i in range(len(key)) if i % 2 == 1],
                                  [key[i].lower() for i in range(len(key)) if i % 2 == 0])}
    key_3 = {i: j for i, j in zip([key[i].upper() for i in range(len(key)) if i % 2 == 0],
                                  [key[i].upper() for i in range(len(key)) if i % 2 == 1])}
    key_4 = {i: j for i, j in zip([key[i].upper() for i in range(len(key)) if i % 2 == 1],
                                  [key[i].upper() for i in range(len(key)) if i % 2 == 0])}
    key = dict(list(key_1.items()) + list(key_2.items()) + list(key_3.items()) + list(key_4.items()))
    lst = []
    for i in message:
        if i in key.keys():
            lst.append(key[i])
        else:
            lst.append(i)
    return ''.join(lst)

def encode(message, key):
    key_1 = {i:j for i,j in zip([key[i].lower() for i in range(len(key)) if i % 2 == 0 ],[key[i].lower() for i in range(len(key)) if i % 2 == 1 ])}
    key_2 = {i:j for i,j in zip([key[i].lower() for i in range(len(key)) if i % 2 == 1], [key[i].lower() for i in range(len(key)) if i % 2 == 0])}
    key_3 = {i:j for i,j in zip([key[i].upper() for i in range(len(key)) if i % 2 == 0 ],[key[i].upper() for i in range(len(key)) if i % 2 == 1 ])}
    key_4 = {i:j for i,j in zip([key[i].upper() for i in range(len(key)) if i % 2 == 1], [key[i].upper() for i in range(len(key)) if i % 2 == 0])}
    key =  dict(list(key_1.items()) + list(key_2.items())+list(key_3.items())+list(key_4.items()))
    lst = []
    for i in message:
        if i in key.keys():
            lst.append(key[i])
        else:
            lst.append(i)
    return ''.join(lst) 
