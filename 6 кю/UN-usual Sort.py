'''
In another Kata I came across a weird sort function to implement. We had to sort characters as usual ( 'A' before 'Z' and 'Z' before 'a' ) except that the numbers had to be sorted after the letters ( '0' after 'z') !!!

(After a couple of hours trying to solve this unusual-sorting-kata I discovered final tests used **usual** sort (digits **before** letters :-)

So, the unusualSort/unusual_sort function you'll have to code will sort letters as usual, but will put digits (or one-digit-long numbers ) after letters.
'''

def unusual_sort(array):
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []
    for i in array:
        try:
            if i.isupper():
                lst1.append(i)
            elif i.islower():
                lst2.append(i)
            elif i.isdigit():
                lst3.append(i)
        except:
            lst4.append(i)
    return sorted(lst1)+sorted(lst2)+(sorted(lst4+lst3,key=lambda x: str(x)))
