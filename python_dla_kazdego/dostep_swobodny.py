# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:30:52 2019

@author: Kinga
"""

# Dostęp swobodny
# Demonstruje indeksowanie łańcucha znaków

import random

word = "indeks"
print("Wartość zmiennej word to:",word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low,high)
    print("word[",position, "]\t", word[position])
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")