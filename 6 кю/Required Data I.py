'''
We need a function count_sel() that receives an array or list of integers (positive and negative) and may give us the following information in the order and structure presented bellow:

[(1), (2), (3), [[(4)], 5]]

(1) - Total amount of received integers.

(2) - Total amount of different values the array has.

(3) - Total amount of values that occur only once.

(4) and (5) both in a list

(4) - It is (or they are) the element(s) that has (or have) the maximum occurrence. If there are more than one, the elements should be sorted (by their value obviously)

(5) - Maximum occurrence of the integer(s)
'''


def count_sel(lst):
    l = len(lst)
    s = len(set(lst))
    k = len([i for i in lst if lst.count(i) == 1])
    n = max([lst.count(i) for i in lst])
    m = sorted(list(set([i for i in lst if lst.count(i) == n])))
    return [l,s,k,[m,n]]
