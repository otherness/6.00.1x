from math import *

def polysum(n,s):
    
    '''
    This function sums the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places.
    '''
    area = (0.25*n*s**2)/tan(pi/n)    # calculate the area or regular polygon
    perim = n * s                     # calculate the perimeter of a polygon
    
    return round((area + perim**2), 4)