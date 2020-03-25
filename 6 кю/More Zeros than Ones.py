'''
Create a moreZeros function which will receive a string for input, and return an array containing only the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.

You should remove any duplicate characters, keeping the first occurence of any such duplicates, so they are in the same order in the final array as they first appeared in the input string.

Examples

'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False

        --> ['a','b','d']

'DIGEST'--> ['D','I','E','T']
'''
def more_zeros(s):
    ns = ''
    for i in s:
        if i not in ns:
            ns += i
    ns = [bin(ord(i)).replace('0b','') for i in ns]
    lst = []
    for i in ns:
        if i.count('0') > i.count('1'):
            lst.append(chr(int(i,2)))
    return lst
