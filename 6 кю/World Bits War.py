'''https://www.codewars.com/kata/58856a06760b85c4e6000055'''
def bits_battle(numbers):
    if numbers == []:
        return 'tie'
    else:
        odd = ''.join([bin(i).replace('0b','') for i in numbers if i%2==1]).count('1')
        even = ''.join([bin(i).replace('0b','') for i in numbers if i%2==0]).count('0')
        if odd > even:
            return 'odds win'
        elif odd < even:
            return 'evens win'
        else:
            return 'tie'
            
'''https://www.codewars.com/kata/58865bfb41e04464240000b0/solutions/python'''
def num_odd(numbers):
    odd = ([(bin(i).replace('0b', '').replace('0', '')) for i in numbers if i % 2 == 1])
    num_minus_odd = ''
    num_plus_odd = ''
    for i in odd:
        try:
            if i[0] == '-':
                num_minus_odd += i[1:]
            else:
                num_plus_odd += i
        except:
            num_plus_odd += i

    return  num_plus_odd.count('1') - num_minus_odd.count('1')


def num_even(numbers):
    even = ([(bin(i).replace('0b', '').replace('0', '')) for i in numbers if i % 2 == 0])
    num_minus_even = ''
    num_plus_even = ''
    for i in even:
        try:
            if i[0] == '-':
                num_minus_even += i[1:]
            else:
                num_plus_even += i
        except:
            num_plus_even += i

    return  num_plus_even.count('1') - num_minus_even.count('1')


def bits_war(numbers):
    if num_odd(numbers) > num_even(numbers):
        return  "odds win"
    elif num_odd(numbers) < num_even(numbers):
        return "evens win"
    else:
        return "tie"

