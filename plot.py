import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from integralregning import *
from Diffentialregning import *

#Desto mere præcis svar man gerne have, jo højere antal søjler (streg) skriver man bare ind i klassen hvor mange man vil have.
#Hvis man gerne vil have et meget præcist svar kommer det til at vente lidt fordi det tager en del tid at beregne for computeren.
#F.eks. 1000 søjler = 1 sekund, 100.000.000 = 20 min, 1.000.000 = 10 sekunder
#Man kan også fjerne print for x, y og streg hvis det skal gå hurtigere.

Integral = Integralregning(1, 10, 100, 2, 6, 5, 2)
Integral.ILommeregner()
class graf:
    def __init__(self):
        #Minimum- og maximum x-værdi på grafen. Ud fra det laver den korresponderende y-akse.
        #Grunden til den første if statement er bare at a og b bare sådan at de har lige langt fra rammen af grafen
        self.x = np.linspace(Integral.a - Integral.b * 0.5, Integral.b * 1.5)
        self.y = Integral.func(self.x)
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, 'r', linewidth=2)
        ax.set_ylim(bottom=0)
        #ax.set_xticks((Integral.a, Integral.b))
        ax.vlines(x=[Integral.a, Integral.b], ymin=0, ymax=[Integral.func(Integral.a), Integral.func(Integral.b)], colors='r')
        #ax.set_xticklabels(('$a: $' + str(Integral.a), '$b: $' + str(Integral.b)))
        ax.text(0.5 * (Integral.a + Integral.b), 100, r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center', fontsize=20)
        ax.text(0.5 * (Integral.a + Integral.b), 200, r"Areal er: "+str(Integral.sumAreal), horizontalalignment='center',
                fontsize=10)
        plt.xlabel('hej2')
        plt.ylabel('hej')
        ax.xaxis.label.set_color('r')
        ax.yaxis.label.set_color('r')
        plt.fill_between(self.x, self.y, -10, color='r', alpha=0.2)
        ax.grid(True, color='grey', linestyle='-', linewidth=1)
        plt.show()





