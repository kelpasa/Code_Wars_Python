'''
Do names have colors?
Now they do.

Make a function that takes in a name (Any string two chars or longer really, but the name is the idea) and use the ascii values of it's substrings to produce the hex value of its color! Here is how it's going to work:

The first two hexadecimal digits are the SUM of the value of characters (modulo 256).
The second two are the PRODUCT of all the characters (again, modulo 256, which is one more than FF in hexadecimal).
The last two are the ABSOLUTE VALUE of the DIFFERENCE between the first letter, and the sum of every other letter. (I think you get the idea with the modulo thing).
For example "Jack" returns "79CAE5", which is... baby blue!
'''
def string_color(name):
    if len(name) <= 1:
        return None
    else:
        num_sum = 0
        num_multi = 1
        num_minus = ord(name[0])
        name2 = name[1:]
        for i in name:
            num_sum += ord(i)
            num_multi *= ord(i)
        for i in name2:
            num_minus -= ord(i)

        lst = [(num_sum%256),(num_multi%256),(abs(num_minus)%256)]
        print(lst)

        new_name = ''

        for i in lst:
            if i == 0:
                new_name += '00'
            else:
                if len(hex(i).replace('0x','').upper()) == 1:
                    new_name +='0' + (hex(i).replace('0x','').upper())
                else:
                    new_name += hex(i).replace('0x','').upper()

    return new_name
