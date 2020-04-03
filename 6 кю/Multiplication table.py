'''
our task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
'''
def multiplicationTable(n):
    table = []
    for num in range(1, n+ 1):
        row = []
        for colum in range(1, n + 1):
            row.append(num * colum)
        table.append(row)
    return table
