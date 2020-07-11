def namelist(names):
    res = [list(names[i].values()) for i in range(len(names))]
    lst = [res[i][0] for i in range(len(res))]
    l = len(lst)
    a = 0
    nw = ''
    while l != 0:
        if l == 1:
            nw = f'{lst[0]}'
        elif l == 2:
            nw += f'{lst[-2]} & {lst[-1]}'
            break
        else:
            nw += f"{lst[a]}, "

        l -= 1
        a += 1
    return nw
