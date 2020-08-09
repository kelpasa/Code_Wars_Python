'''
https://www.codewars.com/kata/58439be66f5fc42e30000076/solutions/python
'''

def letter_pattern(words):
    return "".join(letters[0] if len(set(letters)) == 1 else "*" for letters in zip(*words))
        
