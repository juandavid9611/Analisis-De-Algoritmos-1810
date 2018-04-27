# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 07:55:06 2018

@author: Juanda
"""
import numpy as np
import matplotlib.pyplot as plt

x = [50,80,110,140,170]
y = [3.5,4.2,5.7,3.8,1.2]
h = 0.1
n = len(x)
res = 0

priDer = np.gradient(x,y)
segDer = np.gradient(x,priDer)
plt.scatter(x, y)
plt.title('Puntos de la trayectoria')
plt.show()
print ("Velocidad en la mitad de la trayectoria: ",priDer[3])
print ("Aceleración en la mitad de la trayectoria: ",segDer[3])
