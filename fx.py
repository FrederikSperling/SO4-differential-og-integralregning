import numpy as np
from integralregning import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import sympy as sp
from numpy import linalg
from sympy import Eq, solve_linear_system, Matrix
from sympy.interactive import printing



class fx():
    def __init__(self):

        pass

    def func(self):
        x = input("Skriv en funktion")
        xsplit = x.split("x")
        print(xsplit)
        #xsplit2 = [hej + "h " for hej in spaceremove]
        #print(xsplit2)
        #if "h" in xsplit2:
            #print("hej")

func = fx()
func.func()