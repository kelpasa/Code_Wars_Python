'''
You will receive an array as paramter that contains 1 or more integers and a number n.

Here is a little visualization of the process:

Step 1: Split the array in two:

{1, 2, 5, 7, 2, 3, 5, 7, 8}
      /            \
{1, 2, 5, 7}    {2, 3, 5, 7, 8}
Step 2: Put the arrays on top of each other:

   {1, 2, 5, 7}
{2, 3, 5, 7, 8}
Step 3: Add them together:

{2, 4, 7, 12, 15}
Repeat the above steps n times or until there is only one number left, and then return the array.
'''
def divide_list(numbers):
    half = len(numbers) // 2
    return numbers[:half], numbers[half:]

def add_lists(list_a, list_b):
    if len(list_a) < len(list_b):
        list_a.insert(0,0)
        
    results = []
    for i in range(len(list_a)):
        results.append(list_a[i] + list_b[i])
    
    return results

def split_and_add(numbers, n):
    if len(numbers) == 1:
        return numbers
        
    for i in range(n):
        a,b = divide_list(numbers)
        numbers = add_lists(a,b)
        
    return numbers
