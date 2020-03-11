def solution(number):
    lst = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0: lst.append(i)
    return sum(lst)
