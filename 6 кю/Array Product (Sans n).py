'''
This is an adaptation of a problem I came across on LeetCode.

Given an array of numbers, your task is to return a new array where each index (new_array[i]) is equal to the product of the original array, except for the number at that index (array[i]).
'''
from numpy import prod as pd


def product_sans_n(nums):
    return [pd(nums[:i] + nums[i+1:]) for i,j in enumerate(nums)]
