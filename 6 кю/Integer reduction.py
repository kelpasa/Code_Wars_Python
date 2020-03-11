'''In this Kata, you will be given two integers n and k and your task is to remove k-digits from n and return the lowest number possible, without changing the order of the digits in n. Return the result as a string.

Let's take an example of solve(123056,4). We need to remove 4 digits from 123056 and return the lowest possible number. The best digits to remove are (1,2,3,6) so that the remaining digits are '05'. Therefore, solve(123056,4) = '05'.

Note also that the order of the numbers in n does not change: solve(1284569,2) = '12456', because we have removed 8 and 9.

More examples in the test cases.

Good luck!'''
def solve(n,k):
    s = str(n)
    prev = 0
    removed = 0
    for _ in range(k):
        for i in range(prev, len(s)-1):
            if s[i+1] < s[i]:
                s = s[:i] + s[i+1:]
                prev = max(0, i - 1)
                removed += 1
                break
            prev = i
    return s[:len(s)-(k-removed)]
