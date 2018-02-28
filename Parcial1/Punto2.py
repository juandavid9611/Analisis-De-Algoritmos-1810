# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 07:42:16 2018

@author: Juanda
"""

import math


def f(x): return math.e**x      

def AitkenMethod():
    x0 = 0                     
    tolerance = 1e-10          
    epsilon = 1e-16            
    maxIterations = 20          
    haveWeFoundSolution = 0
    for i in range(maxIterations):
        x1 = f(x0)
        x2 = f(x1)
    
        denominator = (x2 - x1) - (x1 - x0);
    
        if(abs(denominator) < epsilon):         
            print('WARNING: denominator is too small')
            break      
    
        aitkenX = x2 - ( (x2 - x1)**2 )/denominator
        
        if(abs(aitkenX - x2) < tolerance):       
            print('The fixed point is ', aitkenX)        
            haveWeFoundSolution = 1
            break
    
        x0 = aitkenX                                      
    
    if(haveWeFoundSolution == 0):   
        print('Luego su radio de convergencia es r = 1')
        print('Ultimo valor calculado de la serie ', aitkenX)
AitkenMethod()