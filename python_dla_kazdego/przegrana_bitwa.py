# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:53:43 2019

@author: Kinga
"""

# Przegrana bitwa
# Demonstruje przerażającą petlę nieskończoną

print("""
      Twój samotny bohater jest otoczony przez ogromną armię trolli.
      Wielka masa ich zgniłozielonych ciał rozciąga się aż po horyzont.
      Bohater wyjmuje miecz z pochwy, gotów do stoczenia sweoj ostatniej walki.
      """)
health = 10
trolls = 0
damage = 3

while health >= 0:
    trolls += 1
    health -= damage
    print("Bohater pokonuje złego trolla, "\
          "ale odnosi obrażenia i traci", damage, "punkty zdrowia.\n")
    
print("Twój bohater walczył dzielnie i pokonał", trolls, "trolli.")
print("Lecz niestety Twój bohater nie żyje.")

input("\n\nAby zakończyć grę naciśnij klawisz Enter.")