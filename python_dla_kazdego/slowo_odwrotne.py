# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:01:10 2019

@author: Kinga
"""

# Słowo odrotnie

word = input("Podaj słowo do odwrócenia: ")



print("Twoje słowo na odwrót to:")

for i in range(len(word), 0, -1):
    print(word[i -1], end = " ")