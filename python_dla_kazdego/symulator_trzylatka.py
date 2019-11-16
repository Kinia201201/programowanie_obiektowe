# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:54:05 2019

@author: Kinga
"""

# Symulator trzylatka
# Demonstruje pętlę while

print("\tWitaj w 'Symulatorze trzylatka'\n")
print("Ten program symuluje rozmowę z trzyletnim dzieckiem.")
print("Spróbuj przerwać to szaleństwo")
response = ""
while response != "Dlatego.":
    response = input("Dlaczego?\n")
    
print("Aha, już wiem.")
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")