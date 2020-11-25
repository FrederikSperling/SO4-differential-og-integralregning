import tkinter as tk
from tkinter import messagebox, ttk

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        root.title("MainMenu")
        root.geometry("400x300")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Velkommen til differential/integral lommeregneren\n Vælg en af af ovenstående muligheder")
        self.label.pack()
        #Integral regning
        self.integralknap = tk.Button(self, text="Integralregning", command=self.on_integral, padx=10, pady=10)
        self.integralknap.pack()
        #Differential regning
        self.differentialknap = tk.Button(self, text="Differentialregning", command=self.on_differentialregning, padx=10, pady=10)
        self.differentialknap.pack()
        #Afslut
        afslut = tk.Button(self, text="AFSLUT", command=self.master.destroy, padx=10, pady=10, fg="red")
        afslut.pack()



    def on_integral(self):
        self.integralwindow = tk.Toplevel(root)
        self.integralwindow.title("Integralregning")
        self.integralwindow.geometry("400x300")
        #indtastning af funktionforskrift
        tk.Label(self.integralwindow, text="Indtast din funktionsforskrift (Der skal være * mellem tal og x)"
                                           "\n eksempel (2x^2 + 2x + 2) skal skrives som (2*x**2 + 2*x + 2)"
                                           "\n for at skrive noget i potens skal du skrive **").pack()
        self.indtast_integral_func = tk.Entry(self.integralwindow, width=30)
        self.indtast_integral_func.pack()
        #Indtastning af antal søjler
        tk.Label(self.integralwindow, text="Indtast antallet af søjler du ønsker at dele din kurve op i"
                                           "\n(jo flere du vælger des mere præcist)\n 1.000 anbefales").pack()
        self.Antalsteger = tk.Entry(self.integralwindow, width=30)
        self.Antalsteger.pack()
        #Indtastning af den første værdi for det interval man gerne vil finde arealet af
        tk.Label(self.integralwindow, text="Indtast den første værdi for dit interval").pack()
        self.interval1 = tk.Entry(self.integralwindow, width=30)
        self.interval1.pack()
        #indtastning af den anden værdi for intervallet
        tk.Label(self.integralwindow, text="Indtast den anden værdi for dit interval").pack()
        self.interval2 = tk.Entry(self.integralwindow)
        self.interval2.pack()
        #Knap for beregning af integral
        self.beregn_integral = tk.Button(self.integralwindow, fg="green", text="Beregn", command=self.on_beregn_integral).pack()
        #Knap der tager dig tilbage til hovedmenuen
        tk.Button(self.integralwindow, text="Tilbage til hovedmenu", command=self.integralwindow.destroy, fg="red").pack()


    def on_beregn_integral(self):
        # Self.pog der bare en variable som vi sætter til enten 0 eller 1, fordi vores main crashede,
        #hvis vi både kørte integralregning.py og differentialregning.py. Så hvis pog = 0 kører integralregning.py
        #og hvis pog = 1 kører differentialregning.py
        self.pog = 0
        self.steger = self.Antalsteger.get()
        self.integral_forskrift = self.indtast_integral_func.get()
        self.intervalx1 = self.interval1.get()
        self.intervalx2 = self.interval2.get()

        #Fejlmeddelse der checker om brugeren har indtastet et input
        if len(self.steger) == 0:
            tk.messagebox.showwarning(title=None, message="Du skal angive antallet af søjler")
        if len(self.integral_forskrift) == 0:
            tk.messagebox.showwarning(title=None, message="Du skal indtaste en funktionsforskrift")
        if len(self.intervalx1) == 0:
            tk.messagebox.showwarning(title=None, message="Du skal indtaste det første tal for dit interval")
        if len(self.intervalx2) == 0:
            tk.messagebox.showwarning(title=None, message="Du skal indtaste det andet tal for dit interval")
        #Vi laver root.destroy() tilsidst for ellers kunne vi ikke køre vores andre scripts i vores main.
        root.destroy()

    def on_differentialregning(self):
        self.differentialwindow = tk.Toplevel(root)
        self.differentialwindow.title("Differentialregning")
        self.differentialwindow.geometry("400x300")

        #Indtastning af x-værdi
        tk.Label(self.differentialwindow, text="Indtast x-værdien for det punkt du ønsker at finde tangenten for").pack()
        self.indtast_x = tk.Entry(self.differentialwindow, width=30)
        self.indtast_x.pack()
        #Indtastning af funktion
        tk.Label(self.differentialwindow, text="Indtast din funktion").pack()
        self.indtast_diff_func = tk.Entry(self.differentialwindow, width=30)
        self.indtast_diff_func.pack()
        #Knap for beregning af differentialregning
        self.beregn_diff = tk.Button(self.differentialwindow, fg="green", text="Beregn", command=self.on_beregn_diff, padx=10, pady=10).pack()
        #Knap der tager dig tilbage til hovedmenuen
        tk.Button(self.differentialwindow, text="Tilbage til hovedmenu", command=self.differentialwindow.destroy, fg="red").pack()

    def on_beregn_diff(self):
        self.pog = 1
        self.diff_forskrift = self.indtast_diff_func.get()
        self.x = self.indtast_x.get()
        if len(self.diff_forskrift) == 0:
            tk.messagebox.showwarning(title=None, message="Du skal indtaste en funktion")
        if len(self.x) == 0:
            tk.messagebox.showwarning(title=None, message="Du skal indtaste en x-værdi")
        #print("Antallet af streger:", self.diff_forskrift, "\nFunktionsforskrift:", self.x)
        root.destroy()

root = tk.Tk()
app = GUI(master=root)
app.mainloop()

