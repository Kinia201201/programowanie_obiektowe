# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:08:53 2019

@author: Kinga
"""

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

n = [3, 4, 5]
radius = [7.0, 2.5, 4.0]
center = [(1.0, 2.0), (3.0, 4.0), (2.0, 2.0)]
start_angle = [45, 0, 0]

Poly1 = Poly(n[0], radius[0], center[0], start_angle[0])
Poly2 = Poly(n[1], radius[1], center[1], start_angle[1])
Poly3 = Poly(n[2], radius[2], center[2], start_angle[2])


pc = Poly_Collection([])
pc.polyList.append(Poly1)
pc.polyList.append(Poly2)
pc.polyList.append(Poly3)


print(pc.max_radius())