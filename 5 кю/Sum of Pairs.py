'''Sum of Pairs
https://www.codewars.com/kata/sum-of-pairs
'''
def sum_pairs(numbers, target_sum):
    cache = set()
    for number in numbers:
        if target_sum - number in cache:
            return [target_sum - number, number]
        cache.add(number)
