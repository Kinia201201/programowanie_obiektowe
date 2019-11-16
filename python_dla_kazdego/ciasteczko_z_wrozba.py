# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:15:56 2019

@author: Kinga
"""

# Ciasteczko z wróżbą
# Program losowo wybiera 1 z 5 przepowiedni

import random

guess = input("Witaj! Chcesz zobaczysz swoją dzisiajszą przepowiednię? Wpisz TAK/NIE\n")

while guess == "TAK":
    omen = random.randint(1,5)
    if omen == 1:
        print("\nNie lej łez nad stłuczonym dzbankiem mleka. I tak w nim było za dużo wody.")
    elif omen == 2:
        print("\nWschodnia Góra kroczy przez wodę - Buddowie przychodzą z nikąd.")
    elif omen == 3:
        print("""\nTwoja Prawdziwa Natura nie może ulec zniszczeniu, a to dlatego,
              że sama jest zniszczeniem - nigdy nie narodzona, nie może nigdy umrzeć.""")  
    elif omen == 4:
        print("\nCel wojny zawsze jest sprawiedliwy, ale środki nigdy.")
    else:
        print("\nCierpliwy zaspokaja pragnienie wodą oczekiwania.")
    break
if guess == "NIE":
    print("\nDobrze. To do zobaczenia następnym razem!")        
input("\n\nAby zakończyć grę naciśnij klawisz Enter.")