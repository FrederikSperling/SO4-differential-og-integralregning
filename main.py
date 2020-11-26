from integralregning import Integralregning
from Differentialregning import Differentialregning
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
from tkinter import *
from tkinter import messagebox
import sympy
matplotlib.use("TkAgg")


root = Tk()

class GUI():
    def __init__(self):
        root.title("MainMenu")
        root.geometry("400x300")
        self.label = Label(root, text="Velkommen til differential/integral lommeregneren\n Vælg en af af ovenstående muligheder")
        self.label.pack()
        # Integral regning
        self.integralknap = Button(root, text="Integralregning", command=self.on_integral, padx=10, pady=10)
        self.integralknap.pack()
        # Differential regning
        self.differentialknap = Button(root, text="Differentialregning", command=self.on_differentialregning,
                                          padx=10, pady=10)
        self.differentialknap.pack()
        # Afslut
        afslut = Button(root, text="AFSLUT", command=root.destroy, padx=10, pady=10, fg="red")
        afslut.pack()


    def on_integral(self):
        self.integralwindow = Toplevel(root)
        self.integralwindow.title("Integralregning")
        self.integralwindow.geometry("400x300")
        Label(self.integralwindow, text="Indtast din funktionsforskrift (Der skal være * mellem tal og x)"
                                           "\n eksempel (2x^2 + 2x + 2) skal skrives som (2*x**2 + 2*x + 2)"
                                           "\n for at skrive noget i potens skal du skrive **").pack()
        self.indtast_integral_func = Entry(self.integralwindow, width=30)
        self.indtast_integral_func.pack()
        # Indtastning af antal søjler
        Label(self.integralwindow, text="Indtast antallet af søjler du ønsker at dele din kurve op i"
                                           "\n(jo flere du vælger des mere præcist)\n 1.000 anbefales").pack()
        self.Antalsteger = Entry(self.integralwindow, width=30)
        self.Antalsteger.pack()
        # Indtastning af den første værdi for det interval man gerne vil finde arealet af
        Label(self.integralwindow, text="Indtast den første værdi for dit interval").pack()
        self.interval1 = Entry(self.integralwindow, width=30)
        self.interval1.pack()
        # indtastning af den anden værdi for intervallet
        Label(self.integralwindow, text="Indtast den anden værdi for dit interval").pack()
        self.interval2 = Entry(self.integralwindow)
        self.interval2.pack()
        # Knap for beregning af integral
        self.beregn_integral = Button(self.integralwindow, fg="green", text="Beregn",
                                         command=self.on_beregn_integral).pack()
        # Knap der tager dig tilbage til hovedmenuen
        Button(self.integralwindow, text="Tilbage til hovedmenu", command=self.integralwindow.destroy,
                  fg="red").pack()

    def on_beregn_integral(self):
        self.steger = self.Antalsteger.get()
        self.integral_forskrift = self.indtast_integral_func.get()
        self.a = self.interval1.get()
        self.b = self.interval2.get()

        # Fejlmeddelse der checker om brugeren har indtastet et input
        if len(str(self.steger)) == 0:
            messagebox.showwarning(title=None, message="Du skal angive antallet af søjler")
        else:
            try:
                self.steger = int(self.steger)
            except:
                messagebox.showwarning(title=None, message="Søglerne skal være en integer")

        if len(self.integral_forskrift) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste en funktionsforskrift")

        if len(str(self.a)) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste det første tal for dit interval")
        else:
            try:
                self.a = float(self.a)
            except:
                messagebox.showwarning(title=None, message="Intervallet skal være en float")

        if len(str(self.b)) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste det andet tal for dit interval")
        else:
            try:
                self.b = float(self.b)
            except:
                messagebox.showwarning(title=None, message="Intervallet skal være en float")
        try:
            self.Integral = Integralregning(float(self.a), float(self.b), int(self.steger))
            self.integralgraf()
        except:
            messagebox.showwarning(title=None, message="Ingen strings udover (), /, *, x i funktionsforskriften")


    def on_differentialregning(self):
        self.differentialwindow = Toplevel(root)
        self.differentialwindow.title("Differentialregning")
        self.differentialwindow.geometry("400x300")

        # Indtastning af x-værdi
        Label(self.differentialwindow,
                 text="Indtast x-værdien for det punkt du ønsker at finde tangenten for").pack()
        self.indtast_x = Entry(self.differentialwindow, width=30)
        self.indtast_x.pack()
        # Indtastning af funktion
        Label(self.differentialwindow, text="Indtast din funktionsforskrift (Der skal være * mellem tal og x) \n eksempel (2x^2 + 2x + 2) skal skrives som (2*x**2 + 2*x + 2) \n for at skrive noget i potens skal du skrive **").pack()
        self.indtast_diff_func = Entry(self.differentialwindow, width=30)
        self.indtast_diff_func.pack()
        # Knap for beregning af differentialregning
        self.beregn_diff = Button(self.differentialwindow, fg="green", text="Beregn", command=self.on_beregn_diff,
                                     padx=10, pady=10).pack()
        # Knap til hastighedsgrafen
        Hastighedsgrafbutton = Button(self.differentialwindow, fg="green", text="Hastighedsgraf", command=self.hastighedsgraf).pack()
        # Knap der tager dig tilbage til hovedmenuen
        Button(self.differentialwindow, text="Tilbage til hovedmenu", command=self.differentialwindow.destroy,
                  fg="red").pack()

    def on_beregn_diff(self):
        self.diff_forskrift = self.indtast_diff_func.get()
        self.x = self.indtast_x.get()
        if len(self.diff_forskrift) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste en funktion")
        if len(str(self.x)) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste en x-værdi")
        else:
            try:
                self.x = float(self.x)
            except:
                messagebox.showwarning(title=None, message="x skal være en float/integer")

        #try:
        self.Differential = Differentialregning()
        self.Differential.slopeforpoint(7, self.diff_forskrift, float(self.x))
        self.differentialgraf()
        #except:
            #messagebox.showwarning(title=None, message="Ingen strings udover (), /, *, x i funktionsforskriften")

    def afslut(self):
        quit()

    def integralgraf(self):
        plt.subplot(1, 1, 1)
        print(self.Integral.area(self.integral_forskrift))
        xvalues = np.linspace(self.Integral.a - self.Integral.b * 0.5, self.Integral.b * 1.5)
        yvalues = [sympy.sympify(self.integral_forskrift).subs(dict(x=x)) for x in xvalues]
        plt.plot(xvalues, yvalues)
        plt.xlabel('x', color='red')
        plt.ylabel('y', color='red')
        plt.vlines(x=[self.Integral.a, self.Integral.b], ymin=0, ymax=[float(self.Integral.func(self.Integral.a, self.integral_forskrift)), float(self.Integral.func(self.Integral.b, self.integral_forskrift))], colors='blue', label='a')
        xvaluesfill = np.linspace(self.Integral.a, self.Integral.b)
        yvaluesfill = [sympy.sympify(self.integral_forskrift).subs(dict(x=x)) for x in xvaluesfill]
        xvaluesfillarray = np.array(yvaluesfill, dtype=float)
        plt.text(0.5 * (self.Integral.a + self.Integral.b), self.Integral.func(self.Integral.b - self.Integral.a, self.integral_forskrift), r"Areal er: "+str(self.Integral.area(self.integral_forskrift)), ha='center', va='center', fontsize=10)
        plt.fill_between(xvaluesfill, xvaluesfillarray, 0, color='blue', alpha=0.2)
        plt.title("Integralregning")
        plt.grid(which=BOTH, color='grey')
        plt.show()

    def differentialgraf(self):
        plt.subplot(2, 1, 1)
        deltax = 7
        xvalues = np.linspace(self.Differential.x - 100, self.Differential.x + 100)
        yvalues = [sympy.sympify(self.diff_forskrift).subs(dict(x=x)) for x in xvalues]
        plt.plot(xvalues, yvalues, 'black')
        plt.plot(self.Differential.x, self.Differential.func(self.Differential.x, self.diff_forskrift), 'r', marker='o', alpha=1)

        yvaluestangent = [self.Differential.a * x + self.Differential.b for x in xvalues]
        plt.plot(xvalues, yvaluestangent, 'black')
        plt.text(self.Differential.x, self.Differential.func(self.Differential.x * 0.7, self.diff_forskrift), "Hældningen for punktet er " + str(self.Differential.slopeforpoint(deltax, self.diff_forskrift, float(self.x))), horizontalalignment='center', fontsize=10)
        plt.xlabel('x', color='red')
        plt.ylabel('y', color='red')
        plt.title("Differentialregning")
        plt.grid(which=BOTH, color='grey')
        plt.show()
        #Den viser ikke anden graf need fix

    def hastighedsgraf(self):
        try:
            plt.subplot(2, 1, 2)
            #Her kommer grafen for hastighederne ud fra alle hældningerne på grafen.'
            xvalues = np.linspace(self.Differential.x - 100, self.Differential.x + 100)
            plt.plot(xvalues, app.yvalues(xvalues))
            plt.xlabel('x', color='red')
            plt.ylabel('y', color='red')
            plt.title("Kurve med hældninger fra differentialregning")
            plt.grid(which=BOTH, color='grey')
            plt.show()
        except:
            messagebox.showwarning(title=None, message="Du kan ikke bruge denne knap før du har brugt beregn knappen")

    def yvalues(self, linspace):
        xvalues = linspace
        yvalueslist = []
        for values in xvalues:
                yvalueslist.append(self.Differential.slopeforpoint(7, self.diff_forskrift, int(values)))
        return yvalueslist

app = GUI()
root.mainloop()



