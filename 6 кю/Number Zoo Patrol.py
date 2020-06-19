
'''
Background:
You're working in a number zoo, and it seems that one of the numbers has gone missing!

Zoo workers have no idea what number is missing, and are too incompetent to figure it out, so they're hiring you to do it for them.

In case the zoo loses another number, they want your program to work regardless of how many numbers there are in total.'''


def find_missing_number(a):
    n = len(a) + 1
    return ((n*(n+1)/2) - sum(a))
    
    
