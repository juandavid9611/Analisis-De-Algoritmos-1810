# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:20:20 2018

@author: Juanda
"""
matrix2 = [[1,  2],
          [3,  4]]

matrix3 = [[1,  2,  3],
          [4,  5,  6],
          [7,  8,  9]]
matrix4 = [[1,  2,  3, 4],
          [5,  6, 7,  8],
          [9, 10 , 11, 12],
          [13, 14 , 15, 16]]
matrix5 = [[1,  2,  3, 4, 5],
          [6, 7,  8, 9, 10],
          [11, 12, 13, 14 , 15],
          [16, 17, 18 ,19 , 20],
          [21, 22, 23 ,24 , 25]]
def sumaMatriz(matrix):
    upper = 0
    oper = 0
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix)):
            if j<i:
                upper+= (matrix[j][i])
                oper += 1
            else:
                pass
    return upper, oper

def evaluarFn():
    s,o = sumaMatriz(matrix2)
    print ('Suma para n:',len(matrix2),' = ',s,', f(n) = ',o)
    s,o = sumaMatriz(matrix3)
    print ('Suma para n:',len(matrix3),' = ',s,', f(n) = ',o)
    s,o = sumaMatriz(matrix4)
    print ('Suma para n:',len(matrix4),' = ',s,', f(n) = ',o)
    s,o = sumaMatriz(matrix5)
    print ('Suma para n:',len(matrix5),' = ',s,', f(n) = ',o)

evaluarFn()
    