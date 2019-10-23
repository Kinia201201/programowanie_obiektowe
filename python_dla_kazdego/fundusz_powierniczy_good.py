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

car = int(input("Serwis Merceddesa: "))
rent = int(input("Apartament w Świnoujściu: "))
jet = int(input("Wynajem prywatnego samolotu: "))
gifts = int(input("Podarunki: "))
food = int(input("Obiady w restauracjach: "))
staff = int(input("Personel (służba domowa, kucharz, kierowca, asystent): "))
guru = int(input("Osobisty gutu i coach: "))
games = int(input("Gry komputerowe: "))

total = car + rent + jet + gifts + food + staff + guru + games
food *= 52
print("Rocznie na jedzenie wydajesz:", food)
print("\nOgółem:", total)
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")