# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:24:24 2019

@author: Kinga
"""

# Hasło
# Demonstruje instrukcję if oraz klauzulę else

print("Witaj w systemie firmy Bezpieczny Komputer SA")
print("-- bezpieczeństwo to podstawa naszego działania\n")

password = input("Wprowadź hasło: ")

if password == "sekret":
    print("Dostęp został udzielony")
    print("Witaj! Musisz być kimś bardzo ważnym")
else:
    print("Odmowa dostępu")
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")