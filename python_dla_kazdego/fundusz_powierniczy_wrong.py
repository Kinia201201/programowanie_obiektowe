# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:14:06 2019

@author: Kinga
"""

# Uczestnik funduszy powierdniczego - niepoprawna wersja
# Demonstruje błąd logiczny

print(
      """
                      Uczestnik funduszu powierniczego
          
   Sumuje Twoje miesięczne wydatki, żeby Twój fundusz powierniczy się nie wyczerpał
   (bo wtedy byłbyś zmuszony do podjęcia prawdziwej pracy).
   
   Wprowadź swoje wymagane miesięczne koszty. Ponieważ jesteś bogaty, zignoruj 
   grosze i swoje koszty podaj w pełnych złotych.
   
   """
   )

car = input("Serwis Merceddesa: ")
rent = input("Apartament w Świnoujściu: ")
jet = input("Wynajem prywatnego samolotu: ")
gifts = input("Podarunki: ")
food = input("Obiady w restauracjach: ")
staff = input("Personel (służba domowa, kucharz, kierowca, asystent): ")
guru = input("Osobisty gutu i coach: ")
games = input("Gry komputerowe: ")

total = car + rent + jet + gifts + food + staff + guru + games
print("\nOgółem", total)
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")