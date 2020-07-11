'''
ohn has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
It can happen that in two distinct families with the same family name two people have the same first name too.
'''
def meeting(s):
    res = s.upper().replace(";"," ").split()
    res = [ res[i].replace(':'," ").split() for i in range(len(res))]
    res = sorted([(f'{i[1]}, {i[0]}') for i in res])
    new_s = ''
    for i in res:
        new_s += f'({i})'
    return new_s
