'''
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:

2332
110011
54322345

For a given number num, return its closest numerical palindrome which can either be smaller or larger than num. If there are 2 possible values, the larger value should be returned. If num is a numerical palindrome itself, return it.

For this kata, single digit numbers will NOT be considered numerical palindromes.

Also, you know the drill - be sure to return "Not valid" if the input is not an integer or is less than 0.
'''
def palindrome(num):
    try:
        if num == int(num) and num == abs(num):
            if len(str(num))== 1:
                return 11
            else:
                num_plus = num
                while str(num_plus) != str(num_plus)[::-1]:
                    num_plus +=1


                num_minus = num
                while str(num_minus) != str(num_minus)[::-1]:
                    num_minus -= 1

                if num_plus - num  > num - num_minus:
                    return num_minus
                else:
                    return num_plus

        else:
            return 'Not valid'
    except:
        return 'Not valid'
