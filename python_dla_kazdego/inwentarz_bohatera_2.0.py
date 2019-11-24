# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:06:23 2019

@author: Kinga
"""

# Inwentarz bohatera 2.0
# Demonstuje krotki


# utwórz krotkę zawierającą pewne elementy
# za pomocą pętli for
inventory = ("miecz",
             "zbroja",
             "tarcza",
             "napój uzdrawiający")
print("\nElementy Twojego wyposażenia:")
for item in inventory:
    print(item)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")    
    
# wyświetl długość krotki
print("Twój dobytek zawiera", len(inventory), "elementy(-ów).")

input("\nAby kontynuować grę, naciśnij klawisz Enter.")    

# sprawdź, czy element należy do krotki, za pomocą operatorów in
if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

# wyświetl jeden element wskazany przez indeks
index = int(input("\nWprowadź indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje się", inventory[index])

# wyświetl wycinek
start = int(input("\nWprowadź indeks wyznaczający poczatek wycinka: "))
finish = int(input("\nWprowadź indeks wyznaczający koniec wycinka: "))
print("inventory[", start, ":", finish, "to", end=" ")
print(inventory[start:finish])

input("\nAby kontynuować grę, naciśnij klawisz Enter.")    

# dokonaj konkatencji dwóch krotek

chest = ("złoto", "klejnoty")
print("Znajdujesz skrzynię, która zawiera: ")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)

input("\n\nAby zakończyć grę naciśnij klawisz Enter.")