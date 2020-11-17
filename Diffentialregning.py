


class diffenrentialregning:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    # Metode der styrer hvilken formel vi skal bruge.
    # Lige nu har vi kun formel der hedder "ax^2 + bx + c"
    def func(self, q):
        return (self.a * q **2 + self.b * q + self.c)

    def Differential(self, x, DeltaX):
        n = 0

        # Vi bruger linjens ligning mellem 2 punkter for at finde hældningen på den linje der går igennem x og x + DeltaX
        while True:
            a = (self.func(x + DeltaX) - self.func(x)) / ((x + DeltaX) - x)

            # Ved at dividere DeltaX med 2 hele tiden får vi den til at gå mod 0
            # Dette betyder at vi kommer tættere på at have den tangent der går igennem x

            #print(a)
            DeltaX = DeltaX / 2
            n += 1
            if n == 40:
                break

        return a



objekt1 = diffenrentialregning(6, 4, 2)
objekt1.Differential(4,7)