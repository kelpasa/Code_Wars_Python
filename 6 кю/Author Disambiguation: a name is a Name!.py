'''
The objective is to disambiguate two given names: the original with another

This kata is slightly more evolved than the previous one: Author Disambiguation: to the point!.

The function could_be is still given the original name and another one to test against.
'''



D = {":":" ", u"\xe0":"a", u"\xf4":"o", u"\xef":"i"}
change = lambda w: ''.join(D.get(c, c).lower() for c in w if c not in ".!,;?")

def could_be(original, another):
    original = change(original).split()
    another = change(another).split()
    return all(w in original for w in another) if original and another else False
