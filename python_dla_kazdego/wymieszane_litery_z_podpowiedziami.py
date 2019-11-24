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
Aby uzyska podpowiedź napisz "pomoc".
""")
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("""
          Niestety, to nie to słowo.
          Aby uzyskać podpowiedź napisz 'pomoc'.
          """)
    
    guess = input("Twoja odpowiedź: ")
    
    if guess == "pomoc":
        if word == "python":
            print("Język programowania wysokiego poziomu ogólnego przeznaczenia.")
            guess = input("Twoja odpowiedź: ")
        elif word == "anagram":
            print("Wyrażenie lub całe zdanie powstałe przez przestawienie liter bądź sylab innego wyrazu lub zdania.")
            guess = input("Twoja odpowiedź: ")
        elif word == "łatwy":
            print("Synonim słowa prosty.")
            guess = input("Twoja odpowiedź: ")
        elif word == "skomplikowany":
            print("Synonim słowa zawiły.")
            guess = input("Twoja odpowiedź: ")
        elif word == "odpowiedź":
            print("Uzyskuje się ją na pytanie.")
            guess = input("Twoja odpowiedź: ")
        elif word == "ksylofon":
            print("Instrument muzyczny z grupy idiofonów uderzanych.")
            guess = input("Twoja odpowiedź: ")
 
    
if guess == correct:
    print("Udało się! Zgadłeś\n")
 
if guess == "":     
    print("Dziękuję za udział w grze.")

input("\nAby zakończyć grę, naciśnij klawisz Enter.")