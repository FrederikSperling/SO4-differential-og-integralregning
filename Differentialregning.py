import sympy
from GUI import *
import numpy as np

class Differentialregning:
    def __init__(self):
        pass
        #self.a = a
        #self.b = b
        #self.c = c

    # Metode der styrer hvilken formel vi skal bruge.
    # Lige nu har vi kun formel der hedder "ax^2 + bx + c"
    def func(self, x):
        fx = sympy.sympify(app.diff_forskrift).subs(dict(x=x))
        return fx

    def tangent(self, x):
        return self.a * x + self.b

    def DLommeregner(self, x, DeltaX):
        n = 0
        self.x = x
        self.DeltaX = DeltaX

        # Vi bruger linjens ligning mellem 2 punkter for at finde hældningen på den linje der går igennem x og x + DeltaX
        while True:
            self.a = (self.func(self.x + self.DeltaX) - self.func(self.x)) / ((self.x + self.DeltaX) - self.x)

            # Ved at dividere DeltaX med 2 hele tiden får vi den til at gå mod 0
            # Dette betyder at vi kommer tættere på at have den tangent der går igennem x

            #print(self.a)
            self.DeltaX = self.DeltaX / 2

            # Vi laver en variabel der hedder n så vi kører vores while loop 40 gange
            n += 1
            if n == 40:
                self.b = self.func(self.x) - self.a * self.x
                print(self.a)
                self.DeltaX = DeltaX
                #print("Skæringspunktet for differentialregningskurven er:", self.b)
                break

    def HastighedLommeregner(self, nummer):
        n = 0
        self.newx = self.x
        self.newDeltaX = self.DeltaX
        self.list = []
        self.xvalues = np.linspace(self.x, self.x+100, num=nummer)
        for x in self.xvalues:
        # Vi bruger linjens ligning mellem 2 punkter for at finde hældningen på den linje der går igennem x og x + DeltaX
            while True:
                self.newa = (self.func(self.newx + self.newDeltaX) - self.func(self.newx)) / ((self.newx + self.newDeltaX) - self.newx)
                # Ved at dividere DeltaX med 2 hele tiden får vi den til at gå mod 0
                # Dette betyder at vi kommer tættere på at have den tangent der går igennem x

                # print(self.a)
                self.newDeltaX = self.newDeltaX / 2

                # Vi laver en variabel der hedder n så vi kører vores while loop 40 gange
                n += 1
                if n == 40:
                    self.newb = self.func(self.newx) - self.newa * self.newx
                    # print("Skæringspunktet for differentialregningskurven er:", self.b)
                    n = 0
                    #print(self.newa)
                    self.list.append(self.newa)
                    self.newDeltaX = 7
                    self.newx += 1
                    break
        print(self.list)


if app.pog == 1:
    Differential = Differentialregning()
    Differential.DLommeregner(float(app.x),7)
    Differential.HastighedLommeregner(100)