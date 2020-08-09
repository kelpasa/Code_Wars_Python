'''
https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
'''

def stock_list(listOfArt, listOfCat):
    if len(listOfCat) == 0 or len(listOfCat) == 0:
        return ''
    ans = [int(i) for i in list(str(0)*len(listOfCat))]
    for i in listOfArt:
        i = i.split()
        if i[0][0] in listOfCat:
            ans[listOfCat.index(i[0][0])] += int(i[1]) 
    if ans.count(0) == len(ans):
        return ''
    ans_arr = []
    i = 0
    while i < len(listOfCat):
        ans_arr.append('(' + listOfCat[i] + ' : ' + str(ans[i]) + ')')
        i += 1
    return ' - '.join(ans_arr)
