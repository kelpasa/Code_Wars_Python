'''
https://www.codewars.com/kata/58b57f984f353b3dc9000030/solutions/python/me/best_practice
'''

palindrome=lambda n,s:(s*n)[:n//2]+(s*n)[~-n//2::-1]
