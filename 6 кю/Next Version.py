'''
You're fed up about changing the version of your software manually. Instead, you will create a little script that will make it for you.

Exercice
Create a function nextVersion, that will take a string in parameter, and will return a string containing the next version number.

For example:


'''


def next_version(version):
    ls = list(map(int, version.split(".")))
    for i in range(len(ls)-1, -1, -1):
        ls[i] += 1
        if ls[i] > 9 and i != 0:
            ls[i] = 0
        else:
            break
    return ".".join(map(str, ls))
