# -*- coding: utf-8 -*-
print("Hej!")
print("Ile ważysz? (w kg)")
waga = int(input())
print("Jaki jest Twój wzrost? (w cm)")
wzrost = float(input())
print("Ile masz lat?")
wiek = int(input())
S=-161
FFM = 10*waga+6.25*wzrost+5*wiek+S
print("Wpisz odpowiednią wartość")
print("Praca siedząca, brak dodatkowej aktywności fizycznej: 1.2\nPraca niefizyczna, mało aktywny tryb życia: 1.4\nLekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu: 1.6\nPraca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu: 1.8\nPraca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu: 2.0")
T = float(input())
print("Dzienne zapotrzebowanie kaloryczne wynosi:",FFM*T)
