'''In this kata your mission is to rotate matrix counter - clockwise N-times.'''

import numpy as np
def rotate_against_clockwise(matrix, times):
    matrix = np.array(matrix)
    return (np.rot90(matrix,k=times).tolist())
