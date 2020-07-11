'''
Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.

Examples:

# returns test_controller
to_underscore('TestController')

# returns movies_and_books
to_underscore('MoviesAndBooks')

# returns app7_test
to_underscore('App7Test')

# returns "1"
to_underscore(1)
'''

def to_underscore(string):
    string = str(string)
    nw = ''
    for i in string:
        if i.isupper():
            nw += f'_{i.lower()}'

        else:
            nw += i
    if len(nw) == 1:
        return nw
    else:
        return nw[1:]
