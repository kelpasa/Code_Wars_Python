'''Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
'''
def format_duration(s):
    if s == 0:
        return 'now'
    else:
        result_list = []
        rest = s
        for divisor, name in zip([60, 60, 24, 365, float('inf')], ['second', 'minute', 'hour', 'day', 'year']):
            value = int(rest % divisor)
            rest = (rest - value) // divisor
            if value:
                s = f'{value} {name}'
                if value > 1:
                     s += 's'
                result_list.append(s)

        result_list.reverse()

        if len(result_list) > 1:
            return ', '.join(result_list[:-1]) + ' and ' + result_list[-1]

        return result_list[-1]
