'''
You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:

"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"
The first line shows the original balance. Each other line (when not blank) gives information: check number, category, check amount.

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can see them and how many of them you need to have):

"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"
On each line of the report you have to add the new balance and then in the last two lines the total expense and the average expense. So as not to have a too long result string we don't ask for a properly formatted result.

Notes
It may happen that one (or more) line(s) is (are) blank.
Round to 2 decimals your results.
The line separator of results may depend on the language \n or \r\n. See examples in the "Sample tests".
R language: Don't use R's base function "mean()" that could give results slightly different from expected ones.
'''



import re

def check(a):
    b = str(a).split('.')

    if len(b[1])!=2:
        return str(a)+'0'

    else:
        return str(a)
print(check(12.11))


def balance(book):
    book = book.split('\n')
    lst = []
    for i in book:
        lst.append(''.join(re.findall(r'[\w+\.]',i)))
    arr1 = []
    arr2 = []
    for i in lst:
        arr1.append(re.findall(r'[A-Za-z]+',i))
        arr2.append(re.findall(r'[^A-Za-z]+',i))
    arr1 = [ arr1[i] for i in range(len(arr1)) if arr1[i] != []]
    arr1 = [arr1[i][0] for i in range(len(arr1))]
    arr2 = [arr2[i] for i in range(len(arr2)) if arr2[i] != []]
    or_balac = float(arr2[0][0])
    arr2 = arr2[1:]
    res1 = [arr2[i][0] for i in range(len(arr2))]
    res2 = [(arr2[i][1]) for i in range(len(arr2))]
    result1 = f'Original Balance: {or_balac}0\r'
    total = 0
    last = []
    for i,j,k in zip(res1,arr1,res2):
        or_balac -= float(k)
        total += float(k)
        last.append(f'{i} {j} {check(k)} Balance {check(round(or_balac,2))}\r')
    total = round(total,2)
    ae = round(total/len(res2),2)
    last ='\n'.join(last)
    return f'{result1}\n{last}\nTotal expense  {check(total)}\r\nAverage expense  {check(ae)}'
