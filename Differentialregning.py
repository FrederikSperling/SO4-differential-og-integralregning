import sympy

class Differentialregning:
    def __init__(self,):
        pass

    # Metode der styrer hvilken formel vi skal bruge.

    def func(self, x, forskrift):
        fx = sympy.sympify(forskrift).subs(dict(x=x))
        return fx

    def tangent(self, x):
        return self.a * x + self.b

    def slopeforpoint(self, DeltaX, forskrift, x):
        self.x = x
        self.DeltaX = DeltaX
        #self.inputpol = input("Enter differential polynomial here")
        n = 0
        # Vi bruger linjens ligning mellem 2 punkter for at finde hældningen på den linje der går igennem x og x + DeltaX
        while True:
            self.a = (self.func(self.x + self.DeltaX, forskrift) - self.func(self.x, forskrift)) / ((self.x + self.DeltaX) - self.x)

            # Ved at dividere DeltaX med 2 hele tiden får vi den til at gå mod 0
            # Dette betyder at vi kommer tættere på at have den tangent der går igennem x

            #print(self.a)
            self.DeltaX = self.DeltaX / 2

            # Vi laver en variabel der hedder n så vi kører vores while loop 40 gange
            n += 1
            if n == 40:
                self.b = self.func(self.x, forskrift) - self.a * self.x
                #print("Skæringspunktet for differentialregningskurven er:", self.b)
                return self.a