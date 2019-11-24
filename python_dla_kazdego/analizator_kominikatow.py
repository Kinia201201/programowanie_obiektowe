# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:13:36 2019

@author: Kinga
"""

# Analizator komunikatów
# Demonstruje funkcję len() i operator in

message = input("Wprowadź komunikat: ")

print("\nDługość Twojego komunikatu wynosi:", len(message))

print("\nNajczęściej używana litera w języku polskiem, 'a',")
if "a" in message:
    print("wystąpiła w Twoim komunikacie.")
else:
    print("nie wystąpiła w Twoim komunikacie.")


input("\n\nAby zakończyć grę naciśnij klawisz Enter.")