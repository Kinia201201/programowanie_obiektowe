# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:06:23 2019

@author: Kinga
"""

# Inwentarz bohatera
# Demonstuje tworzenie krotek

# utwórz pustą krotkę
inventory = ""

# potraktuj krotkę jako warunek
if not inventory:
    print("Nie posiadasz niczego")
    
input("\nAby kontynuować misję, naciśnij klawisz Enter.")

# utwórz krotkę zawierającą pewne elementy
inventory = ("miecz",
             "zbroja",
             "tarcza",
             "napój uzdrawiający")

# wyświetl krotkę
print("\nWykaz zawartości krotki:")
print(inventory)

# wyświetl każdy element krotki
print("\nElementy Twojego wyposażenia:")
for item in inventory:
    print(item)
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")