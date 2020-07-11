'''We'd like to know the area of an arbitrary shape. The only information of the shape is that it is bounded within the square area of four points: (0, 0), (1, 0), (1, 1) and (0, 1).

Given a function f(x, y) which returns a boolean representing whether the point (x, y) is inside the shape, determine the area of the shape. Your answer is allowed to differ from the true answer by at most 0.01.'''

import numpy as np

def area_of_the_shape(f):
    count = 0
    n = 10000
    for _ in range(n):
        x = np.random.random()
        y = np.random.random()
        if f(x, y): count += 1
    return 1 * count / n
