'''
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
'''

def snail(array):
    temp_list = []
    if array and len(array) > 1:
        if isinstance(array[0], list):
            temp_list.extend(array[0])
        else:
            temp_list.append(array[0])
        array.pop(0)
        for lis_index in range(len(array)):
            temp_list.append(array[lis_index][-1])
            array[lis_index].pop(-1)
        if isinstance(array[-1], list):
            temp_list.extend(array[-1][::-1])
        else:
            temp_list.append(array[-1])
        array.pop(-1)
        for lis_index in range(len(array)):
            temp_list.append(array[::-1][lis_index][0])
            array[::-1][lis_index].pop(0)
        temp_list.extend(snail(array))
        return temp_list
    elif array:
        return array[0]
    else:
        return []
