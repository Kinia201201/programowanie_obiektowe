# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:17:59 2019

@author: Kinga
"""

# Kalkulator napiwku

rachunek = int(input("Cześć! Podaj sumę rachunku wystawionego przez restaurację. "))
print("15% napiwek to", round(float(rachunek * 0.15),2))
print("A 20% napiwek to", round(float(rachunek * 0.20),2))
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")
