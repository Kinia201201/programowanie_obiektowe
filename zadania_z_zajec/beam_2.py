# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 00:17:42 2020

@author: Kinga
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:09:28 2019

@author: Kinga
"""

import numpy as np
import matplotlib.pyplot as plt


class Beam(object):
    def __init__(self, L, P, a, crosssection, material):
        self.L = L
        self.P = P
        self.a = a
        self.crosssection = crosssection
        self.material = material
      
    # w kNm    
    def moment(self):
        x1 = np.arange(0, self.a + 0.1, 0.1)
        x2 = np.arange(self.a, self.L + 0.1, 0.1)
        x = np.block([x1, x2])
        moment = []
        for i in x:
            if i <= self.a:
                moment.append(10 ** (-3) * (self.P * (self.L - self.a) / self.L) * i)
            else:
                moment.append(10 ** (-3) * ((self.P * (self.L - self.a) / self.L) * i - self.P * (i - self.a)))
        return x, moment
    
    def shear(self, x):
        shear = []
        already = 0
        for i in x:
            if i < self.a:
                shear.append(self.P * (self.L - self.a) / self.L)
            if i == self.a and already == 0:              
                shear.append(self.P * (self.L - self.a) / self.L)
                already = 1
            if i == self.a and already == 1:
                shear.append(self.P * (self.L - self.a) / self.L - self.P)
                already = 2
            if i > self.a:
                shear.append(self.P * (self.L - self.a) / self.L - self.P)
        return shear
    
    def deflection(self, x, I):
        deflection = []
        for i in x:
            if i <= self.a:
                deflection.append(10 ** 3 * self.P * i * (self.L - self.a) * (self.a ** 2 - 2 * self.L * self.a + i ** 2)/(6 * self.L * self.material.E * I))
            else:
                deflection.append(10 ** 3 * self.P * self.a * (self.L - i) * (self.a ** 2 - 2 * self.L * i + i ** 2)/(6 * self.L * self.material.E * I))
        return deflection
    
    # w MPa
    def stress(self, W, moment):
        yp = np.arange(-self.crosssection.h / 2, self.crosssection.h / 2 + 0.1, 0.5)
        sigma = []
        for i in yp:
            sigma.append(10 ** (-3) * max(moment) * i / I)
        return yp, sigma
    
    def strain(self, sigma):
        if self.material.behaviour == 'elastic':
            epsilon = []
            for i in sigma:
                epsilon.append(i / (self.material.E * 10 ** (-6)))
            return epsilon
        else:
            raise RuntimeError('Unknown behaviour')
    
    def index(self):
        return self.crosssection.index()    
        
        
class CrossSection(object):
    def __init__(self, b, h ):
        self.b = b
        self.h = h
        
    def index(self):
        I = self.b * self.h ** 3 / 12
        W = self.b * self.h ** 2 / 6
        return I, W
    
class Material(object):
    def __init__(self, E, v, fy, behaviour = 'elastic'):
        self.E = E
        self.v = v
        self.fy = fy
        self.behaviour = behaviour    

if __name__ == '__main__':
    print("Poniższy program tworzy wykres momentów, siły tnącej, ugięcia, naprężeń oraz odkształceń.\n")
    sections = {'small': CrossSection(0.1, 0.3),
                'medium': CrossSection(0.3, 0.9),
                'big': CrossSection(0.9, 2.7)}
    materials = {'cupper': Material(180000000000, 0.3, 300000000),
                 'steel': Material(210000000000, 0.2, 500000000)}
    L = int(input("Podaj długość belki w m: "))
    P = int(input("Podaj wartość siły w N: "))
    a = int(input("Podaj odleglość siły P od początku osi belki w m: "))
    s = input("Wybierz przekrój: 'small', 'medium', 'big': ")
    m = input("Wybierz materiał: 'cupper', 'steel': ")
    
    # Jednostki m, N, Nm, Pa
    MyBeam = Beam(L, P, a, sections[s], materials[m])
    x, moment = MyBeam.moment()
    shear = MyBeam.shear(x)
    I, W = MyBeam.index()
    deflection = MyBeam.deflection(x, I)
    yp, sigma = MyBeam.stress(W, moment)
    epsilon = MyBeam.strain(sigma)
    
    # Wykres momentu
    plt.plot(x, moment, color="green", linewidth=2)
    plt.ylim(max(moment) + 1 / 10 * max(moment), 0)
    plt.xlabel("Długość belki [m]\n\nMaksymalny moment: " + str(round(max(abs(max(moment)),abs(min(moment))),2)) + " kNm")
    plt.ylabel("Moment [kNm]")
    plt.title("Wykres momentu")
    plt.grid(True)
    plt.show()
    
    # Wykres siły tnącej
    plt.plot(x, shear, color="green", linewidth=2)
    plt.xlabel("Długość belki [m]")
    plt.ylabel("Siła tnąca [N]")
    plt.title("Wykres siły tnącej")
    plt.grid(True)
    plt.show()
    
    # Wykres ugięcia
    plt.plot(x, deflection, color="green", linewidth=2)
    plt.xlabel("Długość belki [m]\n\nMaksymalne ugięcie: " + str(round(max(abs(max(deflection)),abs(min(deflection))),3)) + " mm")
    plt.ylabel("Ugięcie [mm]")
    plt.title("Wykres ugięcia")
    plt.grid(True)
    plt.show()
    
    # Wykres naprężeń
    plt.plot(sigma, yp,  color="green", linewidth=2)
    plt.xlabel("Naprężenie [MPa]\n\nMaksymalne naprężenie: " + str(round(max(abs(max(sigma)),abs(min(sigma))),3)) + " MPa")
    plt.ylabel("Wysokość przekorju belki [m]")
    plt.title("Wykres naprężeń")
    plt.grid(True)
    plt.show()

    # Wykres odkształceń
    plt.plot(epsilon, yp, color="green", linewidth=2)
    plt.xlabel("Odkształcenie [-]\n\nMaksymalne odkształcenie: " + str(round(max(abs(max(epsilon)),abs(min(epsilon))),4)))
    plt.ylabel("Wysokość przekorju belki [m]")
    plt.title("Wykres odkształceń")
    plt.grid(True)
    plt.show()
    
    # Wykres odkształcenia-naprężenia
    plt.plot(epsilon, sigma, color="green", linewidth=2)
    plt.xlabel("Odkształcenie [-]")
    plt.ylabel("Naprężenie [MPa]")
    plt.title("Wykres odkształcenia-naprężenia")
    plt.grid(True)
    plt.show()