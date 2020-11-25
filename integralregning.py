import sympy

class Integralregning():
    def __init__(self, a, b, columns):
        self.a = a
        self.b = b
        self.columns = columns

    def func(self, x, forskrift):
        fx = sympy.sympify(forskrift).subs(dict(x=x))
        return fx

    def area(self, forskrift):
        self.areaoffunc = 0
        DeltaX = (self.b - self.a) / int(self.columns)
        n = 0
        x = self.a
        while True:
            x += DeltaX
            y = self.func(x, forskrift)
            columnareal = y * DeltaX
            if columnareal > 0:
                self.areaoffunc += float(columnareal)
            else:
                pass
            n += 1
            if n >= self.columns:
                print("Arealet for integralkurven er:", self.areaoffunc)
                return self.areaoffunc