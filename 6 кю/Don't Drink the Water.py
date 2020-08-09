'''
https://www.codewars.com/kata/562e6df5cf2d3908ad00019e/train/python
'''

import numpy as np

def separate_liquids(glass):
    d = {"H": 1.36, "W": 1.0, "A": 0.87, "O": 0.80}
    invd = dict(zip(d.values(),d.keys()))
    arr = np.array(glass)
    oshape = arr.shape
    glass = arr.reshape((arr.size,)).tolist()
    glass = [d[i] for i in glass]
    glass = sorted(glass)
    glass = [invd[i] for i in glass]
    glass = np.array(glass).reshape(oshape).tolist()
    return glass
