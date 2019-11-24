# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:52:05 2019

@author: Kinga
"""

# Liczenie


start = int(input("Podaj liczbę początkową: "))
stop = int(input("Podaj liczbę końcową: "))
space = int(input("Podaj wielkość odstępu między kolejnymi liczbami: "))

for i in range(start, stop, space):
    print(i, end=" ")