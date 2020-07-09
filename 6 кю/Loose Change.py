'''
Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns a dictionary/hash which shows the least amount of coins used to make up that amount. The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). Therefor the dictionary returned should contain exactly 4 key/value pairs.
'''

from math import floor

def loose_change(cents):
    cents = floor(cents)
    if cents <= 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    else:
        Q = cents // 25
        D = (cents - (Q*25))//10
        N = (cents-((D*10)+(Q*25)))//5
        P = (cents-((N*5)+(D*10)+(Q*25)))//1
        return {'Nickels': N, 'Pennies': P, 'Dimes': D, 'Quarters': Q}

