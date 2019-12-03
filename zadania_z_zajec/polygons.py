# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:08:53 2019

@author: Kinga
"""

import numpy
import matplotlib.patches
import matplotlib.pyplot as plt

class Poly_Collection(object):
    def __init__(self, polyList = []):
        self.polyList = polyList
        
    def max_radius(self):
        return max(Poly_Collection.radius for Poly_Collection in self.polyList)
        
class Poly(object):
    def __init__(self, n, radius = 1.0, center = (0.0, 0.0), start_angle = 0.0):
        self.n = n
        self.radius = radius
        self.center = center
        self.start_angle = start_angle
        
    def get_vertices(self):
        angles = numpy.linspace(0.0, 360.0, self.n+1, dtype='float') + self.start_angle
        numpy.radians(angles, angles)
        x = self.radius * numpy.cos(angles) + self.center[0]
        y = self.radius * numpy.sin(angles) + self.center[1]
        return x, y
    
    def plot(self, ax, facecolor='yellow'):
        x, y = self.get_vertices()
        vertices = list(zip(x, y))
        poly = matplotlib.patches.Polygon(vertices, facecolor=facecolor, edgecolor='black')
        ax.add_patch(poly)
        
        
if __name__ == '__main__':

    n = [3, 4, 5]
    radius = [7.0, 2.5, 4.0]
    center = [(1.0, 2.0), (3.0, 4.0), (2.0, 2.0)]
    start_angle = [45, 0, 0]
    

    
    pc = Poly_Collection([])
    for i, j, k, l in zip(n, radius, center, start_angle):
        p = Poly(i, j, k, l)
        pc.polyList.append(p)
    
    
    fig, ax = plt.subplots()
    ax.set_xlabel('Polygons radius max: ' + str(pc.max_radius())) 
    colors = ['yellow', 'red', 'blue']
    for poly, color in zip(pc.polyList, colors):
        poly.plot(ax, facecolor=color)
    ax.autoscale()
    ax.set_aspect('equal')
    fig.show() 
    
    colors = ['yellow', 'red', 'blue']
    for poly, color in zip(pc.polyList, colors):
        fig, ax = plt.subplots()
        ax.set_xlabel('Polygons radius: ' + str(poly.radius)) 
        poly.plot(ax, facecolor=color)
        print('Polygons radius : ', poly.radius)
        ax.autoscale()
        ax.set_aspect('equal')
        fig.show()    
    
        
   
    
    
