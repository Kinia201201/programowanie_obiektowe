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


xc = 1 # współrzędna punkty centralnego pola
yc = 2
xa = -2 # punkt A gdzie pole centalne jest równe 1
ya = 1

k = 1/np.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)

x = [-2, 3, 1, -2, 6, 6] # 0,4,5 dodatkowe
y = [1, 1, 2, 3, 4, 1] 

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
u = [None] * len(X)
v = [None] * len(X)
#v = []
for i in X:
    u[j] = X[j]/np.sqrt((xc - xa) ** 2 + (yc - ya) ** 2) #v = (X-C) / |CX| * |CX| * 1/|CA|
    v[j] = Y[j]/np.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
    j = j + 1
    
#u = -X/np.sqrt(X ** 2 + Y ** 2)
#v = -Y/np.sqrt(X ** 2 + Y ** 2)

def lenwek(i):
    return np.sqrt(u[i] ** 2 + v[i] ** 2) # pole centralne równe 1 w punkcie A - i=0
     

fig, ax = plt.subplots(figsize=(8,8))
ax.quiver(X + xc,Y + yc ,u , v)



ax.axis([-5, 8, -5, 8])
ax.set_aspect('equal')

plt.show()
