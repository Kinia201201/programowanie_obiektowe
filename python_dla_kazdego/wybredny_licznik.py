# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:17:33 2019

@author: Kinga
"""

# Wybredny licznik
# Demonstruje instrukcje break i continue 

count = 0
while True:
    count += 1
    # zakończ pętlę, jeśli wartość zmiennej count jest większa niż 10
    if count >10:
        break
    # pomiń liczbę 5
    if count ==5:
        continue
    print(count)

input("\n\nAby zakończyć grę naciśnij klawisz Enter.")