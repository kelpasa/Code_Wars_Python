'''
Return the inputted numerical year in century format. For example 2014, would return 21st.

The input will always be a 4 digit string. So there is no need for year string validation

Examples:
Input: 1999 Output: 20th
Input: 2011 Output: 21st
Input: 2154 Output: 22nd
Input: 2259 Output: 23rd
Input: 1124 Output: 12th
Input: 2000 Output: 20th


'''

def whatCentury(year):
    century = 1 + (int(year) - 1)/ 100
    if century % 10 == 1 and century != 11:
        return str(century) + "st"
    if century % 10 == 2 and century != 12:
        return str(century) + "nd"
    if century % 10 == 3 and century != 13:
        return str(century) + "rd"
    return str(century) + "th"
    
   
