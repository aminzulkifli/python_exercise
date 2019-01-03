# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:06:29 2019

@author: Aminurafiuddin
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    if len(aStr)==1:
            return char==aStr
    mid=len(aStr)//2
    midc=aStr[mid]
    if char==midc:
        return True
    elif char<midc:
        return isIn(char,aStr[:mid])
    else:
        return isIn(char,aStr[mid+1:])