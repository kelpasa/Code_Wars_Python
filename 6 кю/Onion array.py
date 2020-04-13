'''
An onion array is an array that satisfies the following condition for all values of j and k:

If all of the following are true:

j >= 0
k >= 0
j + k = array.length - 1
j != k
then:

a[j] + a[k] <= 10
Examples:
[1, 2, 19, 4, 5]   =>  true  (as 1+5 <= 10 and 2+4 <= 10)
[1, 2, 19, 4, 10]  =>  false (as 1+10 > 10)'''

def is_onion_array(a):
    for i in range(len(a)): 
        if len(a) - 1 - i != i : 
            if  a[i] + a[len(a)-1-i] > 10: 
                return False
    return True
