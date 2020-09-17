'''
Find the area of a generic n-sided polygon. The area_polygon will receive in input a list of n (x, y) tuples which are the coordinates of the n vertices and shall output the area of the polygon rounded to 1 decimal place. The input will always be at least 3 points, and the polygon will not be self-intersecting.
https://www.codewars.com/kata/5727500a20c7f837fc001869/python
'''
def area_polygon(vertex):
    vertex = vertex+[vertex[0]]
    res_1 = [i[0] for i in vertex]
    res_2 = [i[1] for i in vertex]
    result_1 = sum([i*j for i,j in zip(res_1[:-1],res_2[1:])])
    result_2 = sum([i*j for i,j in zip(res_1[1:],res_2[:-1])])
    return round(abs(result_1-result_2)/2,1)
