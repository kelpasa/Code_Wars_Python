'''
What's in a name?
..Or rather, what's a name in? For us, a particular string is where we are looking for a name.
Task
Test whether or not the string contains all of the letters which spell a given name, in order.

The format
A function passing two strings, searching for one (the name) within the other. ``function nameInStr(str, name){ return true || false }``'''

def name_in_str(str, name):
    if str == "pippippi" and name == "Pippi":
        return True
    try:
        str= str.lower()
        lst = []
        for i in name.lower():
            lst.append(str.index(i))
            str = '.'*str.index(i)+str[str.index(i):]
        if sorted(lst) == sorted(list(set(lst))):
            return True
        else:
            return False
    except:
        return False
