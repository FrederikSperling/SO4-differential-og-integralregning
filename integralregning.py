
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

    def func(self,xformel):
        #return 3 * xformel + 5
        return self.A * xformel ** self.potens + self.B * xformel + self.C

    def ILommeregner(self):
        self.DeltaX = 0
        self.Areal = 0
        self.sumAreal = 0
        self.DeltaX = (self.b - self.a) / self.streger

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
            #print(self.x)
            #print(streg)
            #Så kan vi finde arealet ved at tage summen af alle søgler.
            self.sumAreal += streg
            #Her laver vi bare en tæller som når den rammer det antal søgler vi har defineret stopper while loopet og der ved vi at vores x-værdi = b.
            n += 1
            if n == self.streger:
                #Så printer vi summen af alle søjlerne og breaker loopet.
                break

#Desto mere præcis svar man gerne have, jo højere antal søjler (streg) skriver man bare ind i klassen hvor mange man vil have.
#Hvis man gerne vil have et meget præcist svar kommer det til at vente lidt fordi det tager en del tid at beregne for computeren.
#F.eks. 1000 søjler = 1 sekund, 100.000.000 = 20 min, 1.000.000 = 10 sekunder
#Man kan også fjerne print for x, y og streg hvis det skal gå hurtigere.
Integral = Integralregning(-10, 10, 200, 2, 6, 5,2)
Integral.ILommeregner()
print(Integral.sumAreal)

