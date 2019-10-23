# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:39:49 2019

@author: Kinga
"""

# Komputer nastrojóW
# Demonstruje klauzulę elif

import random

print("Wyczuwam Twoją energię. Twoje prawdziwe emocje znajduja odbicie na moim ekranie.")
print("Jesteś...")
mood = random.randint(1,3)
if mood == 1:
    # szczęśliwy
    print( \
          """
          -----------
          |         |
          |  0   0  |
          |    <    |
          |         |
          | .     . |
          |  '...'  |
          -----------
          """)
elif mood == 2:
    # zły
    print( \
          """
          -----------
          |         |
          |  0   0  |
          |    <    |
          |         |
          | ------  |
          |         |
          -----------
          """)
elif mood ==3:
        # smutny
    print( \
          """
          -----------
          |         |
          |  0   0  |
          |    <    |
          |         |
          |   .'.   |
          |  '   '  |
          -----------
          """)
else:
    print("Nieprawidłowa wartość nastroju! (Musisz być na prawdę w złym humorze).")
    
print("...dzisiaj.")

input("\n\nAby zakończyć grę naciśnij klawisz Enter.")