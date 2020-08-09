'''
https://www.codewars.com/kata/5844e0890d3bedc5c5000e54/solutions/python
'''

class FileMaster():

    def __init__(self, filepath):
        self.filepath = filepath

    def extension(self):
        return self.filepath[self.filepath.index('.')+1:]

    def filename(self):
        l = self.filepath[:self.filepath.index('.')]
        l_arr = l.split('/')
        return l_arr[-1]

    def dirpath(self):
        # Your code here
        l = self.filepath[:self.filepath.index('.')]
        l_arr = l.split('/')
        return '/'.join(l_arr[:len(l_arr)-1]) + '/'
