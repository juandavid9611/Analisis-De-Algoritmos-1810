# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:20:37 2018

@author: Juanda

Este codigo permite obtener el area entre dos curvas en el 
caso más simple en el cual se intersectan en dos puntos, 
para el ejemplo se utilizaran las funciones
f(x) = 4+cos(x+1)
g(x) = exp(x)*sin(x)
h(x) = g(x) - f(x) = 0
El calculo de las raices se realiza con el metodo de
Biseccion con E=0.000001

"""
from math import*
from pylab import*

def biseccion(f, a, b, e):
    while b-a>=e:
        c=(a+b)/2
        if f(c)==0:
            return c
        else:
            if f(a)*f(c)>0:
                a=c
            else:
                b=c
    return c

def simpson(f,a,b,m):
    h=(b-a)/m
    s=0
    x=a
    for i in range (1,m):
        s=s+2*(i%2+1)*f(x+i*h)
    s=h/3*(f(a)+s+f(b))
    return s

def f(x): return 4+x*cos(x+1)
def g(x): return exp(x)*sin(x)
def h(x): return exp(x)*sin(x)-4-x*cos(x+1)

f=4+x*cos(x+1)
g=exp(x)*sin(x)
x=arange(0,3.5,0.1)
plot(x,f,'b')
plot(x,g,'r')
grid(True)
show()

print('Mediante la grafica se evidencia que las intersacciones estan entre a: 1.0 y 1.5 ; y b: 3.0 y 3.2')

print('Si no existen 2 puntos de interseccion el programa no continuara la ejecucion')
a=biseccion(h,1,1.5,0.000001);
print('Interseccion en a = ',a)
b=biseccion(h,3,3.2,0.000001);
print('Interseccion en b = ',b)


print('Para la formula de Simpson se utiliza m = 10')

r=simpson(h,a,b,10)
print('Area entre las curvas = ',r)