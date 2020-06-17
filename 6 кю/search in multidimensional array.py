'''
Write a function that gets a sequence and value and returns true/false depending on whether the variable exists in a multidimentional sequence.

Example:

locate(['a','b',['c','d',['e']]],'e'); // should return true
locate(['a','b',['c','d',['e']]],'a'); // should return true
locate(['a','b',['c','d',['e']]],'f'); // should return false
'''

def parle_list(arr,nw_arr = None):
    if nw_arr is None:
        nw_arr = []
    for i in arr:
        if type(i) == str:
            nw_arr.append(i)
        else:
            parle_list(i,nw_arr)

    return nw_arr



def locate(seq, value):
    seq =  parle_list(seq)
    return value in seq
