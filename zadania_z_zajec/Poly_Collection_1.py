# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:08:53 2019

@author: Kinga
"""

class Poly_Collection(object):
    def __init__(self, n, radius = 1.0, center = (0.0, 0.0), start_angle = 0.0):
        self.n = n
        self.radius = radius
        self.center = center
        self.start_angle = start_angle
        
        
n = [3, 4, 5]
radius = [7.0, 2.5, 4.0]
center = [(1.0, 2.0), (3.0, 4.0), (2.0, 2.0)]
start_angle = [45, 0, 0]
    
poly_list = [Poly_Collection(n[0], radius[0], center[0], start_angle[0]),
             Poly_Collection(n[1], radius[1], center[1], start_angle[1]),
             Poly_Collection(n[2], radius[2], center[2], start_angle[2])]   

max_radius = max(Poly_Collection.radius for Poly_Collection in poly_list)
print(max_radius)
    
#polyList = []
#polyList.append(Poly_Collection(3, 7.0, (1.0, 2.0), 45))
#polyList.append(Poly_Collection(4, 2.5, (3.0, 4.0), 0))
#polyList.append(Poly_Collection(5, 4.0, (2.0, 2.0), 0))

#print(polyList[2].radius)
#print(Poly_Collection.max_radius())
