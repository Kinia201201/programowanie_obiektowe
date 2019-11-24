# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:37:02 2019

@author: Kinga
"""

# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinnien odgadnąć pierwotne słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

# wubierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)

# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# utworz pusty anagram
#   dopóki wybrane słowo zawiera jakieś litery
#       usuń wylosowaną literę z wybranego słowa
#       dodaj wylosowaną literę do anagramu

# utwórz pomieszaną wersję słowa
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
# rozpocznij grę
print("""
      Witaj w grze 'Wymieszane litery'!
      
      Uporządkuj litery, aby odtworzyć prawidłowe słowo.)
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.
""")
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    guess = input("Twoja odpowiedź: ")
    
if guess == correct:
    print("Udało się! Zgadłeś\n")
    
print("Dziękuję za udział w grze.")

input("\nAby zakończyć grę, naciśnij klawisz Enter.")