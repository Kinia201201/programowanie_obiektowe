# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:03:52 2019

@author: Kinga
"""

# Najlepsze wyniki 2.0
# Demonstruje sekwencje zagnieżdżone

scores = []
choice = None

while choice != "0":
    print(
    """
    Najlepsze wyniki
    0 - zakończ
    1 - pokaż wyniki
    2 - dodaj wynik
    """
    )
    choice = input("Wybierasz: ")
    print()
    
    # zakończ program
    if choice == "0":
        print("Do widzenia.")
    
    # wypisz tabelę najlepszych wyników    
    elif choice == "1":
        print("Najlepsze wyniki\n")
        if scores != []:
            print("GRACZ\t\tWYNIK")
            for entry in scores:
                score, name = entry
                print(name, "\t\t", score)
        else:
            print("Brak wyników.")
    
    # dodaj wynik
    elif choice == "2":
        name = input("Podaj nazwę gracza: ")
        score = int(input("Jaki wynik gracz uzyskał?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
        
    # nieznana opcja
    else:
        print("Niestety,", choice, "nie jest prawidłowym wyborem.")
    
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
    
        