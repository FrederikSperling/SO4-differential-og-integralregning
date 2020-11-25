from integralregning import Integralregning
from Differentialregning import Differentialregning
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox, ttk

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
        if len(self.steger) == 0:
            messagebox.showwarning(title=None, message="Du skal angive antallet af søjler")
        if len(self.integral_forskrift) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste en funktionsforskrift")
        if len(self.a) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste det første tal for dit interval")
        if len(self.b) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste det andet tal for dit interval")
        # Vi laver root.destroy() tilsidst for ellers kunne vi ikke køre vores andre scripts i vores main.
        root.destroy()
        self.Integral = Integralregning(float(self.a), float(self.b), int(self.steger))
        self.integralgraf()

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
        Label(self.differentialwindow, text="Indtast din funktion").pack()
        self.indtast_diff_func = Entry(self.differentialwindow, width=30)
        self.indtast_diff_func.pack()
        # Knap for beregning af differentialregning
        self.beregn_diff = Button(self.differentialwindow, fg="green", text="Beregn", command=self.on_beregn_diff,
                                     padx=10, pady=10).pack()
        # Knap der tager dig tilbage til hovedmenuen
        Button(self.differentialwindow, text="Tilbage til hovedmenu", command=self.differentialwindow.destroy,
                  fg="red").pack()

    def on_beregn_diff(self):
        self.diff_forskrift = self.indtast_diff_func.get()
        self.x = self.indtast_x.get()
        if len(self.diff_forskrift) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste en funktion")
        if len(self.x) == 0:
            messagebox.showwarning(title=None, message="Du skal indtaste en x-værdi")
        # print("Antallet af streger:", self.diff_forskrift, "\nFunktionsforskrift:", self.x)
        root.destroy()
        self.Differential = Differentialregning()
        self.Differential.slopeforpoint(7, self.diff_forskrift, float(self.x))
        self.differentialgraf()

    def afslut(self):
        quit()

    def integralgraf(self):
        print(self.Integral.area(self.integral_forskrift))
        xvalues = np.linspace(self.Integral.a - self.Integral.b * 0.5, self.Integral.b * 1.5)
        plt.plot(xvalues, app.yvalues(xvalues, True, False, False, False))
        plt.xlabel('x', color='red')
        plt.ylabel('y', color='red')
        plt.vlines(x=[self.Integral.a, self.Integral.b], ymin=0, ymax=[float(self.Integral.func(self.Integral.a, self.integral_forskrift)), float(self.Integral.func(self.Integral.b, self.integral_forskrift))], colors='blue')
        xvaluesfill = np.linspace(self.Integral.a, self.Integral.b)
        newyvaluesfill = np.array(app.yvalues(xvaluesfill, True, False, False, False), dtype=float)
        plt.text(0.5 * (self.Integral.a + self.Integral.b), self.Integral.func(self.Integral.b - self.Integral.a, self.integral_forskrift), r"Areal er: "+str(self.Integral.area(self.integral_forskrift)), ha='center', va='center', fontsize=10)
        plt.fill_between(xvaluesfill, newyvaluesfill, 0, color='blue', alpha=0.2)
        plt.show()

    def differentialgraf(self):
        deltax = 7
        xvalues = np.linspace(self.Differential.x - 100, self.Differential.x + 100)
        plt.plot(xvalues, app.yvalues(xvalues, False, True, False, False), 'black')
        plt.plot(self.Differential.x, self.Differential.func(self.Differential.x, self.diff_forskrift), 'r', marker='o', alpha=1)
        plt.plot(xvalues, app.yvalues(xvalues, False, False, True, False), 'black')
        plt.text(self.Differential.x, self.Differential.func(self.Differential.x * 0.7, self.diff_forskrift), "Hældningen for punktet er " + str(self.Differential.slopeforpoint(deltax, self.diff_forskrift, float(self.x))), horizontalalignment='center', fontsize=10)
        plt.xlabel('x', color='red')
        plt.ylabel('y', color='red')
        plt.show()

        #Her kommer grafen for hastighederne ud fra alle hældningerne på grafen.
        plt.plot(xvalues, app.yvalues(xvalues, False, False, False, True))
        plt.xlabel('x', color='red')
        plt.ylabel('y', color='red')
        plt.show()

    def yvalues(self, linspace, inte, diff, difftangent, slopes):
        xvalues = linspace
        yvalueslist = []
        listpos = 0
        if slopes == True:
            x = float(self.x)
        for values in xvalues:
            if inte == True:
                yvalueslist.append(self.Integral.func(xvalues[listpos], self.integral_forskrift))
            if diff == True:
                yvalueslist.append(self.Differential.func(xvalues[listpos], self.diff_forskrift))
            if difftangent == True:
                yvalueslist.append(self.Differential.tangent(xvalues[listpos]))
            if slopes == True:
                yvalueslist.append(self.Differential.slopeforpoint(7, self.diff_forskrift, int(x)))
                x +=1

            listpos += 1
        return yvalueslist

app = GUI()
root.mainloop()



