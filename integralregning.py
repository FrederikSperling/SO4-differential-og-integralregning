
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

    def func(self, xformel):
        return (self.A * xformel ** self.potens + self.B * xformel + self.C)

    def ILommeregner(self):
        self.DeltaX = 0
        self.Areal = 0
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


