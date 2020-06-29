'''
Ever since you started work at the grocer, you have been faithfully logging down each item and its category that passes through. One day, your boss walks in and asks, "Why are we just randomly placing the items everywhere? It's too difficult to find anything in this place!" Now's your chance to improve the system, impress your boss, and get that raise!

The input is a comma-separated list with category as the prefix in the form "fruit_banana". Your task is to group each item into the 4 categories Fruit, Meat, Other, Vegetable and output a string with a category on each line followed by a sorted comma-separated list of items.
'''
from re import findall as fin


def group_groceries(groceries):

    fruit = []
    meat = []
    other = []
    vegetable = []

    for i in groceries.split(','):
        if i in fin(r'fruit_\w+',groceries):
            fruit.append(i.replace('fruit_',''))
        elif i in fin(r'meat_\w+', groceries):
            meat.append(i.replace('meat_',''))
        elif i in fin(r'vegetable_\w+', groceries):
            vegetable.append(i.replace('vegetable_',''))
        else:
            i = i.split('_')
            other.append(i[1])

    return f'fruit:{",".join(sorted(fruit))}\nmeat:{",".join(sorted(meat))}\nother:{",".join(sorted(other))}\nvegetable:{",".join(sorted(vegetable))}'
