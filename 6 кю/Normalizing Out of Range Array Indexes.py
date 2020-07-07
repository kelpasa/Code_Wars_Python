'''
Implement a function that normalizes out of range sequence indexes (converts them to 'in range' indexes) by making them repeatedly 'loop' around the array. The function should then return the value at that index. Indexes that are not out of range should be handled normally and indexes to empty sequences should return undefined/None depending on the language.

For positive numbers that are out of range, they loop around starting at the beginning, so
'''

ef norm_index_test(seq, ind):
    if seq == []:
        return None

    else:
        return seq[ind%len(seq)]
