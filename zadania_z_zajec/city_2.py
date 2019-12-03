# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:13:43 2019

@author: Kinga
"""
import numpy

A = (1,2)
B = (10,5)
C = (2,4)

position = [{'name': 'A', 'coordinates': A}, {'name': 'B', 'coordinates': B},{'name': 'C', 'coordinates': C}]

for i in range(len(position)):
    element = position[i]
    city = element['coordinates']
    name = element['name']
    for j in range(i + 1, len(position)):
        nextelement = position[j]
        nextcity = nextelement['coordinates']
        nextname = nextelement['name']
        x = abs(nextcity[0] - city[0])
        y = abs(nextcity[1] - city[1])
        d = round(numpy.sqrt(x**2 + y**2),2)
        print("The distance between cities", name, "and", nextname, "is", d, ".")
