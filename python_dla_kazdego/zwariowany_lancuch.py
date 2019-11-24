# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:40:59 2019

@author: Kinga
"""

# Zwariowany łańcuch
# Demonstruje użycie pętli for z łańcuchem znaków

word = input("Wprowadź jakieś słowo: ")

print("\nOto poszczególne litery Twojego słowa:")
for letter in word:
    print(letter)
    
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")