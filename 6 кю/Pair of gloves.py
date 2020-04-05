'''
Pair of gloves
Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

A pair of gloves is constituted of two gloves of the same color.

You are given an array containing the color of each glove.

You must return the number of pair you can constitute.

You must not change the input array.

  
'''

def number_of_pairs(gloves):
    unique = set(gloves)
    return sum(gloves.count(i)//2 for i in unique)
