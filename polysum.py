# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:53:34 2019

@author: Aminurafiuddin
"""

# n : number of sides
# s : length of sides
# area = 0.25*n*s^2/tan(pi/n)
# perimeter = length of boundary by polygon
from math import pi,tan
def polysum(n,s):
    #pi = 3.1416 
    # get perimeter
    peri = (n*s)**2
    # get area
    area = 0.25 * n *(s**2) / tan(pi/n)
    polysum = area+ peri
    return round(polysum,4)