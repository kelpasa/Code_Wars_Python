'''
You must create a method that can convert a string from any format into CamelCase. This must support symbols too.

Don't presume the separators too much or you could be surprised.

Tests
camelize("example name")   # => ExampleName
camelize("your-NaMe-here") # => YourNameHere
camelize("testing ABC")    # => TestingAbc
'''
import re
def camelize(str_):
    return ''.join([i.capitalize() for  i in (re.split(r'\W',str_.replace('_',' ')))])
