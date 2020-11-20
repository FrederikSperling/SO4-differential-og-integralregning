from tkinter import*
import tkinter as tk
from Equation import*


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        root.title("MainMenu")
        root.geometry("400x300")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #introduktions tekst
        self.label = tk.Label(self.master, text="Velkommen til differential/integral lommeregneren\n Vælg en af af ovenstående mugliheder")
        self.label.pack()
        #Integral regning
        self.integralknap = tk.Button(self, text="Integralregning", command=self.on_integral, padx=10, pady=10)
        self.integralknap.pack(side=TOP)
        #Differential regning
        self.differentialknap = tk.Button(self, text="Differentialregning", command=self.on_differentialregning, padx=10, pady=10)
        self.differentialknap.pack(side=TOP)
        #Afslut
        afslut = tk.Button(self, text="AFSLUT", command=self.master.destroy, padx=10, pady=10, fg="red")
        afslut.pack(side=BOTTOM)



    def on_integral(self):
        self.integralwindow = tk.Toplevel(root)
        self.integralwindow.title("Integralregning")
        self.integralwindow.geometry("400x300")
        #indtastning af funktionforskrift
        tk.Label(self.integralwindow, text="Indtast din funktionsforskrift"
                                           "\n for at skrive noget i potens skal du skrive **").pack()
        self.indtast_integral_func = tk.Entry(self.integralwindow, width=30)
        self.indtast_integral_func.pack()
        #Indtastning af antal søjler
        tk.Label(self.integralwindow, text="Indtast antallet af søjler du ønsker at dele din kurve op i"
                                           "\n(jo flere du vælger des mere præcist)\n 10.000 anbefales").pack()
        self.Antalsteger = tk.Entry(self.integralwindow, width=30)
        self.Antalsteger.pack()
        self.beregn_intetal = tk.Button(self.integralwindow, text="Beregn",command=self.on_beregn_integral).pack()
        self.mainmenu = tk.Button(self.integralwindow, text="Tilbage til hovedmenu", command=self.integralwindow.destroy,fg="red").pack()

    def on_beregn_integral(self):
        kk = self.Antalsteger.get()
        uu = self.indtast_integral_func.get()
        print(uu,kk)



    def on_differentialregning(self):
        self.differentialwindow = tk.Toplevel(root)
        self.differentialwindow.title("Differentialregning")
        self.differentialwindow.geometry("400x300")

        tk.Label(self.differentialwindow, text="Indtast din funktion").pack()
        self.indtast_diff_func = tk.Entry(self.differentialwindow, width=30).pack()
        self.beregn_diff = tk.button(self.differentialwindow,text="beregn", command=self.on_beregn_diff, padx=10, pady=10).pack()

    def on_beregn_diff(self):
        pass





root = tk.Tk()
app = GUI(master=root)
app.mainloop()

