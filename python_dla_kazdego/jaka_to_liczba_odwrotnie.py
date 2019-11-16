# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:19:16 2019

@author: Kinga
"""

# Jaka to liczba - odwrotnie
# Użytkownik wybiera losowo liczbę z zakresu od 1 do 100.
# Komputer próbuje ją odgadnąć, a użytkownik go informuje,
# czy pdana przez niego liczba jest: za duża, za mała, prawidłowa.

# Pseudokod:

# przywitanie użytkowaniak i prosba o wybranie liczby od 1 do 100
# gracz wybiera liczbę od 1 do 100
# komputer losuje liczbę od 1 do 100
# ustawia licznik prób
# dopóki nie jest prawidłowa
#   jezeli za mało
#       komputer ogranicza losowanie liczb od 1 do podanej
#   w przeciwnym wypadku
#       komputer ogranicza losowanie liczb od podanej do 100
#   zwieksza licznik prób
# jezeli uzytkownik potwierdzi liczbe, gratuluje
# informacja ile prób komputer potrzebował na odgadnięcie liczby

import random

print("""
      \tWitaj w grze 'Jaka to liczba'!\n
      Tym razem to ja spróbuje odgadnąć!
      Wybierz liczbę z zakresu od 1 do 100.
      Odpowadaj na pytanie ZA MAŁO/ZA DUŻO/PRAWIDŁOWO.\n
      """)

input("\t\tGotowy?! Naciśnij klawisz Enter.\n")

number = random.randint(1,100)
print("Czy to jest liczba", number,"?")
guess = input("")
tries = 1

while guess != "PRAWIDŁOWO":
    if guess == "ZA MAŁO":
        number = random.randint(number,100)
    else:
        number = random.randint(1,number)
    print("Czy to jest liczba", number,"?")
    guess = input("")
    tries += 1
print("Huraaa udało się! Potrzebowałem", tries, "prób, aby odgadnąć Twoją liczbę.")
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")