# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:38:40 2019

@author: Kinga
"""

# Orzeł i reszka
# Program rzuca 100 razy monetą i podeje liczbę wyrzuconych orzełków i reszek
# 0 - orzeł, 1 - reszka

import random


i = 1
orzel = 0
reszka = 0
while i <= 100:
    rzut = random.randint(0,1)
    if rzut == 0:
        orzel += 1
    else:
        reszka += 1
    i +=1
    
print("Liczba wyrzuconych orzełków to", orzel, ", a reszek", reszka, ".")

input("\n\nAby zakończyć grę naciśnij klawisz Enter.")
    