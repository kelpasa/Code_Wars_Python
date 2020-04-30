'''
Time to win the lottery!

Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot. Example ticket:

[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
To do this, you must first count the 'mini-wins' on your ticket. Each sub array has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini win. Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

All inputs will be in the correct format. Strings on tickets are not always the same length.
'''

def add(arr):
    return [ord(i) for i in arr]


def bingo(ticket,win):
    arr_1 = [add(list(i[0])) for i in ticket]
    arr_2 = [i[1] for i in ticket]
    lst = [i for i in zip(arr_1,arr_2)]
    s = 1
    for i in lst:
        if i[1] in i[0]:
            s += 1
    if s > win:
        return 'Winner!'
    else:
        return 'Loser!'
