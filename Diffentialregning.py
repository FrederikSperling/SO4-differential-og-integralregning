


class diffenrentialregning:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def func(self, q):
        return (self.a * q **2 + self.b * q + self.c)

    def Differential(self, x, DeltaX):
        n = 0


        while True:
            a = (self.func(x + DeltaX) - self.func(x)) / ((x + DeltaX) - x)

            print(a)
            DeltaX = DeltaX / 2
            n += 1
            if n == 40:
                break

        print (a)
        return a



objekt1 = diffenrentialregning(6, 4, 2)
objekt1.Differential(4,7)