print("Cześć! Jeśli chcesz znać stan konta za kilka lat, podaj kilka informacji:\nJaki jest Twój stan początkowy konta?")
start = float(input())
print("Podaj stopę oprocentowania rocznego.")
stopa = float(input())
print("Podaj liczbę lat na lokacie.")
lata = int(input())
print("Twoje {:.2f} zł przez {} lata na lokacie {:.2f} % urośnie do {:.2f}.".format(start,lata,stopa,start*(1+stopa*lata)))