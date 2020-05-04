'''
##Overview

Write a helper function that takes in a Time object and converts it to a more human-readable format. You need only go up to '_ weeks ago'.

to_pretty(0) => "just now"

to_pretty(40000) => "11 hours ago"
##Specifics

The output will be an amount of time, t, included in one of the following phrases: "just now", "[t] seconds ago", "[t] minutes ago", "[t] hours ago", "[t] days ago", "[t] weeks ago".
You will have to handle the singular cases. That is, when t = 1, the phrasing will be one of "a second ago", "a minute ago", "an hour ago", "a day ago", "a week ago".
The amount of time is always rounded down to the nearest integer. For example, if the amount of time is actually 11.73 hours ago, the return value will be "11 hours ago".
Only times in the past will be given, with the range "just now" to "52 weeks ago" 
'''
def to_pretty(n):
    if n == 0:
        return 'just now'
    elif 0<n<60:
        if n ==1:
            return 'a second ago'
        else:
            return f"{n} seconds ago"
    elif 60<n<3600:
        n = n // 60
        if n == 1:
            return 'a minute ago'
        else:
            return f'{n} minutes ago'
    elif 3600 < n < 86400:
        n = n // 3600
        if n == 1:
            return 'an hour ago'
        else:
            return f'{n} hours ago'
    elif 86400 < n < 604800:
        n = n // 86400
        if n == 1:
            return 'a day ago'
        else:
            return f'{n} days ago'
    elif 604800 < n :
        n = n // 604800
        if n == 1:
            return 'a week ago'
        else:
            return f'{n} weeks ago'
