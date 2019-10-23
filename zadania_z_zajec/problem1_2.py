# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:59:09 2019

@author: Kinga
"""
# Programowanie obiektowe - problem 1- wersja 2 (punktty ij)
# a) pole skalarne: f(x,y) = x^2 +y^2  x = (-1,1) y = (-1,1) 
# b) interpolacja: Nx=Ny=4

import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def func( xa, ya ):
    xy = np.zeros( ( len(xa), len(ya) ) )
    for j in range(len( ya )):
        for i in range(len( xa )):
            xy[i,j] = x[i]**2+y[j]**2
    return xy

A = 1
B = 1
Nx = 4
Ny = 4
x = np.linspace(-A, A, Nx) 
y = np.linspace(-A, A, Nx) 
Z = func(x,y) 


X, Y = np.meshgrid(x, y) # np.meshgrid - macierz/tablice współrzędnych



fig = plt.figure() # tworzy obiekt
ax = fig.gca(projection = '3d')
ax.plot_surface(X, Y, Z, cmap=cm.gray)
plt.show()