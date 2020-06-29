'''Write a function that returns a (custom) FizzBuzz sequence of the numbers 1 to 100.

The function should be able to take up to 4 arguments:

The 1st and 2nd arguments are strings, "Fizz" and "Buzz" by default;
The 3rd and 4th argyments are integers, 3 and 5 by default.
Thus, when the function is called without arguments, it will return the classic FizzBuzz sequence up to 100:'''

def fizz_buzz_custom(string_one='Fizz', string_two='Buzz', num_one=3, num_two=5):
    lst =  []
    for i in range(1,101):
        if i % num_two == 0 and i % num_one == 0:
            lst.append(f'{string_one+string_two}')
        elif i % num_one == 0:
            lst.append(string_one)
        elif i % num_two == 0:
            lst.append(string_two)

        else:
            lst.append(i)

    return lst
