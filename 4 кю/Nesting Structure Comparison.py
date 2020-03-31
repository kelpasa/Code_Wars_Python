'''
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structure as the first array.'''


def same_structure_as(original, other):
    if type(original) != type(other) != list or len(original) != len(other):
        return False

    for x,y in zip(original, other):
        if type(x) == list and not same_structure_as(x, y):
            return False
    return True
