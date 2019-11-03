# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:10:04 2019

@author: Kinga
"""
# Programowanie obiektowe - problem 2
# pole wektorowe:F(x,y) = x^2 +y^2  srodek = (1,2) wektor jedn = (-2,1)
# wizualizacja w x = [3,1,-2] i y = [1,2,3]


import matplotlib.pyplot as plt
import numpy as np
def funcX(value):
    return value - (xc - value)
def funcY(value):
    return value - (yc - value)

xc = 1
yc = 2
x = [-2, 3, 1, -2, 6] # 0 i 4 dodatkowe
y = [1, 1, 2, 3, 4] 

x = [i - xc for i in x]
y = [i - yc for i in y]

X = np.array(x)
Y = np.array(y)
#Y = [[-1, 0 , 1]]
#X, Y = np.meshgrid(x, y)
#X, Y = np.array(x, y)

#funcX(X[j])
#(Y[j] - (1 - Y[j]))
j = 0
for i in X:
    u[j] = -X[j]/np.sqrt(funcX(X[j]) ** 2 + funcY(Y[j]) ** 2)
    v[j] = -Y[j]/np.sqrt(funcX(X[j]) ** 2 + funcY(Y[j]) ** 2)
    j = j + 1
    
#u = -X/np.sqrt(X ** 2 + Y ** 2)
#v = -Y/np.sqrt(X ** 2 + Y ** 2)

len = np.sqrt(u[0] ** 2 + v[0] ** 2)

fig, ax = plt.subplots(figsize=(8,8))
ax.quiver(X + xc,Y + yc ,u , v)



ax.axis([-3, 7, 0, 5])
ax.set_aspect('equal')

plt.show()
