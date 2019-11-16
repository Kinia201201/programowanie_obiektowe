# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:07:28 2019

@author: Kinga
"""

# Maitre d'
# Demonstruje traktowanie wartości jako earunku

print("Witaj w Chateau D' Smakosz\n"\
      "Wydaje się, że tego wieczoru mamy prawie komplet gości.\n")

money = int(input("Ile złotych wsuniesz do kieszeni maitre 'd?\n"))

if money:
    print("Och, przypomniałem sobie o wolnym stoliku. Proszę tędy.")
else:
    print("Proszę zaczekać. To może trochę potrwać.")
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")