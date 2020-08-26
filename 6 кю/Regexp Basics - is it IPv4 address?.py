'''
Implement String#ipv4_address?, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading 0s, spaces etc.

'''
import re



def chec(i):
    nw = str(int(i))
    if nw == i:
        return True
    else:
        return False

def ipv4_address(address):
    res = re.split(r'[.]',address,maxsplit=3)
    lst = []

    for i in res:
        if i.isdigit():
            lst.append(i)
    if len(lst)!=4:
        return False
    else:
        arr = []
        for i in lst:
            if 0<=int(i)<=255:
                arr.append(i)
            else:
                return False
        result = []
        for i in arr:
            result.append(chec(i))
        result = set(result)
        if len(result) == 1:
            return True
        else:
            return False
