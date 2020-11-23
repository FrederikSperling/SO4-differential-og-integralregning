import random
import sympy
from GUI import *

class Integralregning:
    def __init__(self, a, b, streger, A, B, C, potens):
        self.a = a
        self.b = b
        self.streger = streger
        self.A = A
        self.B = B
        self.C = C
        self.x = self.a
        self.potens = potens
        self.sumAreal = 0

    #def func1(self, xformel):
        #return (self.A * xformel ** self.potens + self.B * xformel + self.C)

    def func(self, x):
        fx = sympy.sympify(app.integral_forskrift).subs(dict(x=x))
        return fx


    def ILommeregner(self):
        self.DeltaX = 0
        self.DeltaX = (self.b - self.a) / int(self.streger)

        n = 0
        while True:
            #print (DeltaX)
            #Vi finder værdien for hver x-værdi i hver søjle og det kan man gøre ved at addere delta x til den forrige x-værdi
            self.x += self.DeltaX
            #Så skal vi finde y-værdien til den korresponderende x-værdi og det kan vi gøre ved at tage functionen til x-værdien
            y = self.func(self.x)
            #Så finder vi arealet af hver enkelt søjle (vi har bare kaldt den streg) ved at gange vores y-værdi med delta x
            streg = y * self.DeltaX
            #print(y)
            #print(streg)


            #Så kan vi finde arealet ved at tage summen af alle søgler.
            self.sumAreal += streg
            #Her laver vi bare en tæller som når den rammer det antal søgler vi har defineret stopper while loopet og der ved vi at vores x-værdi = b.
            n += 1
            if n >= self.streger:
                print("Arealet for integralkurven er:", self.sumAreal)
                #Så printer vi summen af alle søjlerne og breaker loopet.
                break

    def skaeringmedx(self, xrandom):
        self.xrandom = xrandom
        decimaler = 5
        x = round((self.A * self.xrandom ** self.potens + self.C) / - self.B, decimaler)
        self.xrandom = random.randint(-255, 0)
        while True:
            if round(self.xrandom, decimaler) == round(x):
                #print("nice!" + str(self.xrandom))
                break
            else:
                self.xrandom += 0.0001
                round(self.xrandom, decimaler)
                x = round((self.A * self.xrandom ** self.potens + self.C) / - self.B, decimaler)
                if self.xrandom > x:
                    deltax = self.xrandom - x
                else:
                    deltax = x - self.xrandom
                #print(deltax)
                if deltax > 10:
                    self.xrandom = random.randint(0, 255)

        self.xrandom2 = xrandom
        x2 = round((self.A * self.xrandom2 ** self.potens + self.C) / - self.B, decimaler)

        while True:
            if round(self.xrandom2, decimaler) == round(x2):
                #if self.xrandom2 <= self.xrandom and self.xrandom2 >= self.xrandom - 0.1:
                    #self.xrandom2 = random.randint(0, 255)
                    #print("hej")
                    #self.skaeringmedx(200)
                #else:
                #print("nice2!" + str(self.xrandom2))
                break
            else:
                self.xrandom2 -= 0.0001
                # round(self.xrandom, decimaler)
                x2 = round((self.A * self.xrandom2 ** self.potens + self.C) / - self.B, decimaler)
                #print(self.xrandom2)
                if self.xrandom2 > x2:
                    deltax2 = self.xrandom2 - x2
                else:
                    deltax2 = x2 - self.xrandom2

                #print(deltax2)
                if deltax2 > 10:
                    self.xrandom2 = random.randint(0, 255)

if app.pog == 0:
    Integral = Integralregning(0, 10, int(app.steger), 4, 7, -5, 2)
    Integral.ILommeregner()