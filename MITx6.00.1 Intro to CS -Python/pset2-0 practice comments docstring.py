'''
Course: MITx 6.00.1x Intro to Comp Sci
Date: 13 Sep 2017
Optional Problem:
    A regular polygon has n number of sides. Each side has length s.

    The area of a regular polygon is: (0.25*n*s**2)/(tan(pi/n))

    The perimeter of a polygon is: length of the boundary of the polygon

    Write a function called polysum that takes 2 arguments, n and s. This function 
    should sum the area and square of the perimeter of the regular polygon. The 
    function returns the sum, rounded to 4 decimal places.

A large part of programming is being able to write understandable code and 
read code from other people. The course code graders are able to grade you on 
correctness but not on style. This problem will give you practice with (1) 
writing code that will be read by others and (2) understanding code that others 
wrote.
'''

def polysum(n, s):
    '''
    Returns the sum of a regular polygon's area + (square of the perimeter)
    rounded to 4 decimal places.
    
    n = number of sides
    s = length of each side
    
    Locally imports pi and tan from math module.
    '''
    from math import pi, tan
    area = (0.25*n*s**2)/(tan(pi/n))
    peri_sq = (n*s)**2
    return round(area + peri_sq, 4)

