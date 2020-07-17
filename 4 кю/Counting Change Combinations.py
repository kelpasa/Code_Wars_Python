'''
https://www.codewars.com/kata/541af676b589989aed0009e7/python

Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite amount of coins.
'''

def count_change(money, coins):

    def recur(money, coins):
        ret = 0
        len_coins = len(coins)
        if len_coins == 0 or money == 0:
            return ret
        for j in range(len_coins):
            coin = coins[j]
            if money < coin:
                return ret
            n, rest = divmod(money, coin)
            if rest == 0:
                ret += 1
                rng = range(n - 2)
            else:
                rng = range(n - 1)
            _coins_ = coins[j + 1:]
            _money_ = money
            for i in rng:
                _money_ -= coin
                ret += recur(_money_, _coins_)
        return ret

    return recur(money, sorted(coins))
