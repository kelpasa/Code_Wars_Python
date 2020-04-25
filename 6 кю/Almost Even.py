'''
We need the ability to divide an unknown integer into a given number of even parts — or at least as even as they can be. The sum of the parts should be the original value, but each part should be an integer, and they should be as close as possible.

Example code:

split_integer(20, 6)  # returns [3, 3, 3, 3, 4, 4]
Complete the function so that it returns an array of integer representing the parts. Ignoring the order of the parts, there is only one valid solution for each input to your function!

'''

def split_integer(num, parts):
    if parts == 1:
        return [num]
    else:
        res = num // parts
        if res*parts == num:
            lst = []
            while parts != 0:
                lst.append(res)
                parts -= 1
            return lst
        else:
            x = num - (res * parts)

            lst = []
            while parts != 0:
                lst.append(res)
                parts -= 1
            arr = []
            for i in lst[:x]:
                arr.append(i+1)
            return lst[:-x] + arr
