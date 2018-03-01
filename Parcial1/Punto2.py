# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 07:42:16 2018

@author: Juanda
"""
from numpy import *
import math


def f(x): return math.e**x      

def Aitken(x0,x1,x2):
    return x2-((x2-x1)**2)/(x2-2*x1+x0)
def serTaylor(x,k):
    return sum((x**i)/math.factorial(i) for i in range(k+1))
    
def detConvergencia():
    y=1
    x0=serTaylor(y,0)
    x1=serTaylor(y,1)
    x2=serTaylor(y,2)
    err=1
    i=3
    p0=Aitken(x0,x1,x2)
    print('Pn(x)','\t\t','Error')
    while(err>1.e-8):
        p1=p0
        print(p0,'\t\t',err)
        x0=serTaylor(y,i-2)
        x1=serTaylor(y,i-1)
        x2=serTaylor(y,i)
        i+=1
        p0=Aitken(x0,x1,x2)
        err=abs(p0-p1)/abs(p0)

detConvergencia()
    