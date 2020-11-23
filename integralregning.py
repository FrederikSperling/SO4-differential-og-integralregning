import random
import sympy
from GUI import *

class Integralregning:
    def __init__(self, a, b, streger):
        self.a = a
        self.b = b
        self.streger = streger
        self.x = self.a
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

#Jo mere præcis svar man gerne have, jo højere antal søjler (streg) skriver man bare ind i klassen hvor mange man vil have.
#Hvis man gerne vil have et meget præcist svar kommer det til at vente lidt fordi det tager en del tid at beregne for computeren.
#F.eks. 1000 søjler = 1 sekund, 100.000.000 = 20 min, 1.000.000 = 10 sekunder
#Man kan også fjerne print for x, y og streg hvis det skal gå hurtigere.

if app.pog == 0:
    Integral = Integralregning(int(app.intervalx1), int(app.intervalx2), int(app.steger))
    Integral.ILommeregner()
