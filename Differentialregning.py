import numpy as np
from integralregning import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from GUI import *

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
        #self.inputpol = input("Enter differential polynomial here")
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
                #print("Skæringspunktet for differentialregningskurven er:", self.b)
                break

if app.pog == 1:
    Differential = Differentialregning()
    Differential.DLommeregner(int(app.x),7)