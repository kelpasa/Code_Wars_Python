'''
Complete the function that takes a string as an input, and return a list of all the unpaired characters (i.e. they show up an odd number of times in the string), in the order they were encountered as an array.

In case of multiple appearances to choose from, take the last occurence of the unpaired character.
'''

def odd_one_out(s):
    result = []
    dictResult = {}

    for item in s:
        dictResult[item] = dictResult.get(item,0) + 1
        if dictResult[item] % 2 == 0:
            dictResult.pop(item)
    return list(dictResult.keys())
