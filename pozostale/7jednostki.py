print("Podaj długość w centymetrach")
dlugosc = float(input())
print("Długość %.2f cm to: %.2f metrów = %.2f cali" % (dlugosc,dlugosc/100,dlugosc/0.393700787))
print("Długość {:.2f} cm to: {:.2f} metrów = {:.2f} cali".format(dlugosc,dlugosc/100,dlugosc/0.393700787))
