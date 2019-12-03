# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:13:43 2019

@author: Kinga
"""
import numpy

A = (1,2)
B = (10,5)
C = (2,4)

position = [A, B, C]

for i in range(len(position)):
    city = position[i]
    for j in range(i + 1, len(position)):
        nextcity = position[j]
        x = abs(nextcity[0] - city[0])
        y = abs(nextcity[1] - city[1])
        d = numpy.sqrt(x**2 + y**2)
        print("The distance between cities", position[i], "and", position[j], "is", d, ".")
