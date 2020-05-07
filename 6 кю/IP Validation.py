'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples
Valid inputs:

1.2.3.4
123.45.67.89
Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note that leading zeros (e.g. 01.02.03.04) are considered invalid.
'''


def is_valid_IP(string):
    parts = string.split(".")
    if len(parts)!=4:
        return False
    for item in parts:
        if not item.isdigit():
            return False
        if len(item)>1 and item[0]=='0':
            return False
        i = int(item)
        if i <0 or i >255:
            return False
    return True
