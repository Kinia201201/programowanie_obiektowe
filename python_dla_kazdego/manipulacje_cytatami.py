# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:39:26 2019

@author: Kinga
"""

# Manipulacja cytatami
# Demonstruje metody łańcucha

# Cytat z wypowiedzi prezesa IBM, Thomasa Watsona, z 1943 r.
quote = "Myślę, że istenieje światowy rynek dla może pięciu komputerów"
print("Oryginalny cytat w tłumaczeniu na język polski:")
print(quote)
print("\nDużymi literami:")
print(quote.upper())
print("\nMałymi literami:")
print(quote.lower())
print("\nWszystkie wyrazy z dużej litery:")
print(quote.title())
print("\nZ drobną zmianą:")
print(quote.replace("pięciu", "milionów",2))
print("\nOryginalny cytat pozostał bez zmian:")
print(quote)
print("\nZ odwróconymi wielkościami liter:")
print(quote.swapcase())
print("\nPierwsza litera duża, pozostałe małe:")
print(quote.capitalize())
print("\nBiałe znaki usunięte:")
print(quote.strip())
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")