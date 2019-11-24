# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:06:04 2019

@author: Kinga
"""

# Bez samogłosek
# Demonstruje tworzenie nowych łańcuców przy użyciu pętli for

message = input("Wprowadź komunikat: ")
new_message = ""
VOWELS = "aąeęioóuy"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Został utworzony nowy łańcuch:", new_message)
        
print("\nTwój komunikat bez samogłosek to:", new_message)

input("\n\nAby zakończyć grę naciśnij klawisz Enter.")