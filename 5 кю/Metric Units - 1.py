'''
Scientists working internationally use metric units almost exclusively. Unless that is, they wish to crash multimillion dollars worth of equipment on Mars.

Your task is to write a simple function that takes a number of meters, and outputs it using metric prefixes.

In practice, meters are only measured in "mm" (thousandths of a meter), "cm" (hundredths of a meter), "m" (meters) and "km" (kilometers, or clicks for the US military).

For this exercise we just want units bigger than a meter, from meters up to yottameters, excluding decameters and hectometers.

All values passed in will be positive integers. e.g.'''

def meters(x):
    res = ''
    if x < 10 ** 3:
        res = ''
    elif x < 10 ** 6:
        x = x / (10 ** 3)
        res = 'k'
    elif x < 10 ** 9:
        x = x / (10 ** 6)
        res = 'M'
    elif x < 10 ** 12:
        x = x / (10 ** 9)
        res = 'G'
    elif x < 10 ** 15:
        x = x / (10 ** 12)
        res = 'T'
    elif x < 10 ** 18:
        x = x / (10 ** 15)
        res = 'P'
    elif x < 10 ** 21:
        x = x / (10 ** 18)
        res = 'E'
    elif x < 10 ** 24:
        x = x / (10 ** 21)
        res = 'Z'
    else:
        x = x / (10 ** 24)
        res = 'Y'
    if x % 1 == 0:
        x = int(x)

    return f"{x}{res}{'m'}"
