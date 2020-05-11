'''
The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of positions where the input strings do not match.

Examples (in JavaScript):

hamming("I like turtles","I like turkeys")  //returns 3
hamming("Hello World","Hello World")  //returns 0
'''

def hamming(a,b):
    res = 0
    for i,j in zip(a,b):
        if i != j:
            res +=1
    return res
