'''
Given a sorted array of numbers, return the summary of its ranges.

Examples
summary_ranges([1, 2, 3, 4]) == ["1->4"]
summary_ranges([1, 1, 1, 1, 1]) == ["1"]
summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7", "9->10"]
summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]
'''


def summary_ranges(nums):
    def f():
        cur = []
        for x in nums:
            if not cur:
                cur = [x]
            elif x == cur[-1] + 1:
                cur[1:] = x,
            elif x != cur[-1]:
                yield cur
                cur = [x]
        if cur:
            yield cur
    return [str(xs[0]) if xs[0] == xs[-1] else f'{xs[0]}->{xs[-1]}' for xs in f()]
