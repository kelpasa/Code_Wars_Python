'''https://www.codewars.com/kata/56b3b9c7a6df24cf8c00000e/train/python'''

def list_depth(l):
    depths = []
    for item in l:
        if isinstance(item, list):
            depths.append(list_depth(item))
    if len(depths) > 0:
        return 1 + max(depths)
    return 1
