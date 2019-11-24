# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:00:07 2019

@author: Kinga
"""

# Licznik
# Demonstruje funkcję range()

print("Liczenie:")
for i in range(10):
    print(i, end=' ')
    
print("\n\nLiczenie co 5:")
for i in range(0, 50, 5):
    print(i, end=' ')
    
print("\n\nLiczenie do tyłu:")
for i in range(10, 0, -1):
    print(i, end=' ')
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")