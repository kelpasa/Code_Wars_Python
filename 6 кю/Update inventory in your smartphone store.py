'''
You will be given an array which lists the current inventory of stock in your store and another array which lists the new inventory being delivered to your store today.

Your task is to write a function that returns the updated list of your current inventory in alphabetical order.

Example
cur_stock = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]

update_inventory(cur_stock, new_stock)  ==>
[(15, 'Apple'), (25, 'HTC'), (5, 'LG'), (1000, 'Nokia'), (54, 'Samsung'), (43, 'Sony')]
'''

def update_inventory(cur_stock, new_stock):
    cur_stock = sorted(cur_stock, key= lambda x: x[1])
    new_stock = sorted(new_stock, key=lambda x: x[1])
    lst1 = [i[1] for i in new_stock]
    lst2 = [i[1] for i in cur_stock]
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    for i in cur_stock:
        if i[1] in lst1:
            arr1.append(i)
        else:
            arr3.append(i)
    for i in new_stock:
        if i[1] in lst2:
            arr2.append(i)
        else:
            arr4.append(i)


    res1 = [i[1] for i in arr1]
    res2 = [i[0] for i in arr1]
    res3 = [i[0] for i in arr2]


    tot = []

    for i,j,k  in zip(res2,res3,res1):
        tot.append((i+j,k))

    return sorted(tot+arr3+arr4,key= lambda x: x[1])

