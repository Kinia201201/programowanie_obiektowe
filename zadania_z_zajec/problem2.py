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
xc = 1
yc = 2
x = [3, 1, -2] # - xc
y = [1, 2, 3] # -yc

x = [2, 0, -1]
y = [0, 1, 2]

X, Y = np.meshgrid(x, y)
u = X/np.sqrt(X ** 2 + Y ** 2)
v = Y/np.sqrt(X ** 2 + Y ** 2)

fig, ax = plt.subplots(figsize=(8,8))
ax.quiver(X + xc,Y + yc,u,v)



ax.axis([-2, 5, -1, 6])
ax.set_aspect('equal')

plt.show()
