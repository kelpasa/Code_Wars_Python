'''
About the replacement
 Choose exactly one element from the sequence and replace it with another integer > 0. It is not allowed to replace a number with itself or to change no number at all.

Task
 Find the minimal possible sequence after performing a valid replacement and sorting the sequence.

Input:
 Input contains sequence with N integers. All elements of the sequence > 0. The sequenc will never be empty.

Output:
 Return sequence with N integers — the minimum possible values of each sequence element after one replacement and the sorting are performed.

Examples:

([1,2,3,4,5])  =>  [1,1,2,3,4]
([4,2,1,3,5])  =>  [1,1,2,3,4]
([2,3,4,5,6])  =>  [1,2,3,4,5]
([2,2,2])      =>  [1,2,2]
([42])         =>  [1]
'''
def sort_number(a): 
    if max(a) != 1:
        a.remove(max(a))
        a.append(1)
    else:
        a.remove(max(a))
        a.append(2)
        
    return sorted(a)
