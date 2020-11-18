
class integralregning:
    def __init__(self, a, b, streger, A, B, C):
        self.a = a
        self.b = b
        self.streger = streger
        self.A = A
        self.B = B
        self.C = C
        xstart = self.a
        self.xstart = xstart

    def func(self,q):
        #return 3 * q + 5
        return self.A * q **2 + self.B * q + self.C

    def ILommeregner(self):
        DeltaX = 0
        Areal = 0
        n = 0
        sum = 0

        self.DeltaX = DeltaX
        self.Areal = Areal
        self.sum = sum


        DeltaX = (self.b - self.a) / self.streger

        while True:
            #print (DeltaX)
            self.xstart += DeltaX
            y = self.func(self.xstart)
            streg = y * DeltaX
            print(streg)
            sum += streg
            n += 1
            if n == self.streger:
                print(sum)
                break


Integral = integralregning(-10, 10, 100, 2, 6, 5)
Integral.ILommeregner()
