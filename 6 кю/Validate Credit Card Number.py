'''
In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.

Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.

Here is the algorithm:
'''
def validate(n):
        n = [int(i) for i in (str(n))]
        if len(n) % 2 == 0:
            lst = []
            for i in range(len(n)):
                if i % 2 == 0:
                    lst.append(n[i]*2)
                else:
                    lst.append(n[i])
            new_lst = []
            for i in range(len(lst)):
                if lst[i] > 9:
                    new_lst.append(lst[i]//2)
                else:
                    new_lst.append(lst[i])
            if sum(new_lst) % 10 == 0:
                return True
            else:
                return False

        else:
            lst = []
            for i in range(len(n)):
                if i % 2 == 1:
                    lst.append(n[i] * 2)
                else:
                    lst.append(n[i])
            new_lst = []
            for i in range(len(lst)):
                if lst[i] > 9:
                    new_lst.append(lst[i] //2 )
                else:
                    new_lst.append(lst[i])

            if sum(new_lst) % 10 == 0:
                return True
            else:
                return False
