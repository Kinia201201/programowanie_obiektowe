# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:28:00 2019

@author: Kinga
"""

# Eksluzywna sieć
# Demonstruje operatory logiczne i warunki złożone

print("\tEksluzywna Sieć Kompterowa")
print("\t  Tylko dla członków!\n")

security = 0

username = ""
while not username:
    username = input("Użytkownik:")
    
password = ""
while not password:
    password = input("Hasło:")
    
if username == "M.Dawson" and password == "sekret":
    print("Cześć, Mike!")
    security = 5
elif username == "S.Meier" and password == "cywilizacja":
    print("Hej, Sid!")
    security = 4
elif username == "S.Miyamoto" and password == "mariobros":
    print("Co u Cibie, Shingeru?")
    security = 3
elif username == "W.Wright" and password == "simsowie":
    print("Jak leci, Will!")
    security = 2
elif username == "gość" or password == "gość":
    print("Witaj, Gościu!")
    security = 1
else:
    print("Nieudana próba logowania. Nie jesteś taki wyjątkowy.\n")
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")