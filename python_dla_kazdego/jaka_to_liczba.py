# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:59:52 2019

@author: Kinga
"""

# Jaka to liczba
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy pdana przez niego liczba jest: za duża, za mała, prawidłowa.

import random

print("""
      \tWitaj w grze 'Jaka to liczba'!\n
      Mam na myśli pewną liczbę z zakresu od 1 do 100.
      Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n
      """)

# ustaw wartości początkowe
the_number = random.randint(1, 100)
guess = int(input("Ta liczba to:"))
tries = 1

# pętla zgadywania
while guess != the_number:
    if guess > the_number:
        print("Za duża...")
    else:
        print ("Za mała...")
    guess = int(input("Spróbuj jeszcze raz. Ta liczba to:"))
    tries += 1
print("Odgadłeś! Ta liczba to", the_number)
print("Do osiągnięcia sukcesu potrzebowałeś", tries, "prób!\n")

input("\n\nAby zakończyć grę naciśnij klawisz Enter.")
