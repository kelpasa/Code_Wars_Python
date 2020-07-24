'''
https://www.codewars.com/kata/56ee74e7fd6a2c3c7800037e/train/python'''

def unpack(data):
    nested = True
    while nested:
        new = []
        nested = False
        for i in data:
            if isinstance(i, list):
                new.extend(i)
                nested = True
            elif isinstance(i, set):
                new.extend(i)
                nested = True
            elif isinstance(i, dict):
                new.extend(i.items())
                nested = True
            elif isinstance(i, tuple):
                new.extend(i)
                nested = True
            else:
                new.append(i)
        data = new
    return data
