'''
https://www.codewars.com/kata/57f8ff867a28db569e000c4a/solutions/python
'''

def kebabize(string):
    #your code here
    ans = ''
    for i in string:
        if i.isalpha():
            if i.isupper():
                ans += '-' + i.lower()
            else:
                ans += i
    if len(ans) > 0:
        return ans if ans[0]!='-' else ans[1:]
    else:
        return ''
