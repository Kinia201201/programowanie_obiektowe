# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:07:35 2019

@author: Kinga
"""

# Programowanie obiektowe - problem 1- wersja 1
# a) pole skalarne: f(x,y) = x^2 +y^2  x = (-1,1) y = (-1,1) 
# b) interpolacja: Nx=Ny=4

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
A = 1
B = 1
Nx = 4
Ny = 4
# np = numpy
# np.linspace - zwraca równomiernie rozmieszczone liczby w przedziale
x = np.linspace(-A, A, Nx) 
y = np.linspace(-B, B, Ny)
X, Y = np.meshgrid(x, y) # np.meshgrid - macierz/tablice współrzędnych
Z = X ** 2 + Y ** 2

fig = plt.figure() # tworzy obiekt
ax = fig.gca(projection = '3d')
ax.plot_surface(X, Y, Z, cmap=cm.gray)
plt.show()