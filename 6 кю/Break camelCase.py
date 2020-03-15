def solution(identifier):
    new = ''
    for i in identifier:
        if i == i.lower():
            new += i
        elif i == i.upper():
            new += f' {i}'
    return new
