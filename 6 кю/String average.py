'''You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"'''

def average_string(s):
    contener = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    try:
        arr = []
        for i in s.split():
            arr.append(contener[i])
        if arr == []:
            return "n/a"
        else:
            res = sum(arr) // len(arr)
            for i,j in contener.items():
                if j == res:
                    return i

    except:
        return "n/a"
