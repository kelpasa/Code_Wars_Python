'''
You know how sometimes you write the the same word twice in a sentence, but then don't notice that it happened? For example, you've been distracted for a second. Did you notice that *"the"* is doubled in the first sentence of this description?

As as aS you can see, it's not easy to spot those errors, especially if words differ in case, like *"as"* at the beginning of the sentence.

Write a function that counts the number of sections repeating the same word (case insensitive). The occurence of two or more equal words next after each other count as one.
'''



def count_adjacent_pairs(st): 
    st = st.lower().split()
    check, ret, k = None, 0, 0
    for e in st:
        if e == check and k:
            continue
        if e == check and not k:
            ret, k = ret + 1, 1
        else:
            check,k = e, 0
    return ret
