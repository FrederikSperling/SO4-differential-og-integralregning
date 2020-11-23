import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from integralregning import Integral
from Differentialregning import Differential
import sympy

#Desto mere præcis svar man gerne have, jo højere antal søjler (streg) skriver man bare ind i klassen hvor mange man vil have.
#Hvis man gerne vil have et meget præcist svar kommer det til at vente lidt fordi det tager en del tid at beregne for computeren.
#F.eks. 1000 søjler = 1 sekund, 100.000.000 = 20 min, 1.000.000 = 10 sekunder
#Man kan også fjerne print for x, y og streg hvis det skal gå hurtigere.

Integral.ILommeregner()

class graf:
    def __init__(self):
        pass

    def integralregninggraf(self):
        xlin = np.linspace(Integral.a - Integral.b * 0.5, Integral.b * 1.5)
        xlinfill = np.linspace(Integral.a, Integral.b)
        ylist = []
        ylistfill = []
        listpos = 0
        for values in xlin:
            ylist.append(Integral.func(xlin[listpos]))
            listpos += 1

        listpos = 0
        for values in xlinfill:
            ylistfill.append(float(Integral.func(xlinfill[listpos])))
            listpos += 1

        #print(ylist)
        fig, ax = plt.subplots()
        ax.plot(xlin, ylist, 'black', linewidth=2)
        #Minimum- og maximum x-værdi på grafen. Ud fra det laver den korresponderende y-akse.
        #Grunden til den første if statement er bare at a og b bare sådan at de har lige langt fra rammen af grafen
        #fig, ax = plt.subplots()
        #xstarttilslut = np.linspace(Integral.a - Integral.b * 0.5, Integral.b * 1.5)
        #fx = Integral.func(xstarttilslut)
        #ax.plot(xstarttilslut, fx, 'black', linewidth=2)
        #x.set_xticks((Integral.a, Integral.b)
        ax.vlines(x=[Integral.a, Integral.b], ymin=0, ymax=[float(Integral.func(Integral.a)), float(Integral.func(Integral.b))], colors='blue')
        #ax.set_xticklabels(('$a: $' + str(Integral.a), '$b: $' + str(Integral.b)))
        #ax.text(0.5 * (Integral.a + Integral.b), 100, r"$\int_a^b f(x)\mathrm{d}x$", ha='center', fontsize=20)
        ax.text(0.5 * (Integral.a + Integral.b), 0, r"Areal er: "+str(Integral.sumAreal), ha='center', va='center', fontsize=10,)
        #plt.xlabel('x')
        #plt.ylabel('y')
        #ax.xaxis.label.set_color('black')
        #ax.yaxis.label.set_color('black')
        plt.fill_between(xlinfill, ylistfill, 0, color='blue', alpha=0.2)
        ax.grid(True, color='grey', linestyle='-', linewidth=1)
        plt.show()


    def differentialregninggraf(self):
        xlin = np.linspace(0, 100)
        ylist = []
        ylist2 = []
        listpos = 0
        for values in xlin:
            yvalue = Differential.func(xlin[listpos])
            yvalue2 = Differential.tangent(xlin[listpos])
            ylist.append(yvalue)
            ylist2.append(yvalue2)
            listpos += 1

        fig, ax = plt.subplots()
        ax.plot(xlin, ylist, 'black', linewidth=2)
        ax.plot(xlin, ylist2, 'black', linewidth=2)
        ax.text(Differential.x, Differential.func(Differential.x * 0.7), "Hældningen for punktet er "+ str(Differential.a), horizontalalignment='center', fontsize=10)
        plt.plot(Differential.x, Differential.func(Differential.x), 'r', marker='o', alpha=1)
        plt.xlabel('x')
        plt.ylabel('y')
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.grid(True, color='grey', linestyle='-', linewidth=1)
        plt.show()

