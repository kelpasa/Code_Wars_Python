'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3'''

def rgb(*color):
    arr = []
    for i in color:
        if i < 0:
            arr.append(hex(0).replace('0x',''))
        elif i > 255:
            arr.append(hex(255).replace('0x',''))
        else:
            arr.append(hex(i).replace('0x',''))

    res = []
    for i in arr:
        if len(i) == 1:
            res.append('0'+i)
        else:
            res.append(i)


    return ''.join(res).upper()
