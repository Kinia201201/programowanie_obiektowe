# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:46:51 2019

@author: Kinga
"""

# Sprzedawca samochodów

print("Program oblicza faktyczną cenę samochodu po doliczeniu wszystkich dodatków.")
podstawa = int(input("Wprowadź podstawową cenę samochodu: "))
podatek = 0.25 * podstawa
rejestracja = 0.15 * podstawa
prowizja = 3000
dostarczenie = 1500
print("Cena całkowita to", podstawa + podatek + rejestracja + prowizja + dostarczenie)
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")