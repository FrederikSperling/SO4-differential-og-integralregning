import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from Integralregning import *
from Diffentialregning import *

Integral = Integralregning(-10, 10, 10000, 2, 6, 5, 2)

class Testplot:
    def __init__(self):
        Integral.ILommeregner()
        #Minimum- og maximum x-værdi på grafen. Ud fra det laver den korresponderende y-akse.
        #Grunden til den første if statement er bare at a og b bare sådan at de har lige langt fra rammen af grafen
        if Integral.a > Integral.b:
            if Integral.a < 0:
                self.x = np.linspace(Integral.a * 1.5, Integral.b + Integral.a * 0.5)
            else:
                self.x = np.linspace(0, Integral.b * Integral.a * 0.5)
        else:
            if Integral.a < 0:
                self.x = np.linspace(Integral.a * 1.5, Integral.b + Integral.b * 0.5)
            else:
                self.x = np.linspace(0, Integral.b * Integral.b * 0.5)

        self.y = self.func(self.x)
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, 'r', linewidth=2)
        ax.set_ylim(bottom=0)
        ax.set_xticks((Integral.a, Integral.b))
        ax.vlines(x=[Integral.a, Integral.b], ymin=0, ymax=[self.func(Integral.a), self.func(Integral.b)])
        ax.set_xticklabels(('$a: $' + str(Integral.a), '$b: $' + str(Integral.b)))
        ax.text(0.5 * (Integral.a + Integral.b), 100, r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center', fontsize=20)
        ax.text(0.5 * (Integral.a + Integral.b), 200, r"Areal er: "+str(Integral.sumAreal), horizontalalignment='center',
                fontsize=10)
        plt.show()

    def func(self, x):
        return (Integral.A * x ** Integral.potens + Integral.B * x + Integral.C)





