'''
https://www.codewars.com/kata/557e8a141ca1f4caa70000a6/train/python
'''
def is_triangle_number(num): 
    try:
        if (num ==0):
            return True
        sum, n = 0, 1
        while (sum <= num):
            sum = sum + n
            if (sum == num):
                return True
            n += 1
    
        return False
    except:
        return False
