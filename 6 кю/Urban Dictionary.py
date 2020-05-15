'''
Design a data structure that supports the following two operations:

addWord (or add_word) which adds a word,
search which searches a literal word or a regular expression string containing lowercase letters "a-z" or "." where "." can represent any letter
You may assume that all given words contain only lowercase letters.

Examples
add_word("bad")
add_word("dad")
add_word("mad")

search("pad") == False
search("bad") == True
search(".ad") == True
search("b..") == True
'''


from re import match
class WordDictionary:
    def __init__(self):
        self.data=[]
  
    def add_word(self,x):
        self.data.append(x)
  
    def search(self,x):
        for word in self.data:
            if match(x+"\Z",word): return True
        return False
        
