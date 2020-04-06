'''
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'

'''

import re

def dashatize(num):
  return 'None' if num is None else '-'.join(w for w in re.split(r'([13579])', str(abs(num))) if len(w)>0)
