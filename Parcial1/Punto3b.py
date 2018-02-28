# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 07:06:01 2018

@author: Juanda
"""
import math

def newtonRaphson(f,df,a,b,tol=1.0e-5):
    'import error'
    from numpy import sign
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): print('Root is not bracketed')
    x = 0.5*(a + b)
    for i in range(30):
        fx = f(x)
        if fx == 0.0: return x
        # Tighten the brackets on the root
        if sign(fa) != sign(fx): b = x
        else: a = x
        # Try a Newton-Raphson step
        dfx = df(x)
        # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
        # If the result is outside the brackets, use bisection
        if (b - x)*(x - a) < 0.0:
            dx = 0.5*(b - a)
            x = a + dx
        # Check for convergence
        print('Iteration: ',i,'X: ',x)
        if abs(dx) < tol*max(abs(b),1.0): return x
    print('Too many iterations in Newton-Raphson')

def f(x): return math.log(x+2) - math.sin(x)
def df(x): return (1/(x+2) - math.cos(x))
x = newtonRaphson(f,df,-1.99999,0.0)
print ('Raiz: ',x)