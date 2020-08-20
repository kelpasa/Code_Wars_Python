'''
https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2/train/python
'''
from datetime import datetime, timedelta

def solve(arr):
    times = sorted(datetime.strptime(a, '%H:%M') for a in set(arr))
    times = times + [times[0].replace(day=times[0].day + 1)]
    m = max(j - i - timedelta(minutes=1) for i, j in zip(times, times[1:]))
    return '{:0>2}:{}'.format(*str(m).split(':')[:-1])
