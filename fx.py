import numpy as np
from integralregning import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import sympy as sp
from numpy import linalg
from sympy import Eq, solve_linear_system, Matrix
from sympy.interactive import printing
import math
import time


class fx():
    def __init__(self):

        pass



def skaeringmedx():
    xrandom = -10
    decimaler = 5
    a = 8.5
    b = 6
    c = -6
    potens = 2
    while True:
        if round(xrandom, decimaler) == round((a * xrandom ** potens + c) / - b, decimaler):
            print("nice!"+ str(xrandom))
            break
        else:
            print(xrandom)
            xrandom += 0.00001

fx = input("Enter a Polynomial: ")
def func(x):
    return eval(fx.replace('x', str(x)))
y = func(10)
print(y)

#fx = input("Enter a Polynomial: ")
#x = float(input("At wich position should the polynomial be evaluated: "))
#print(eval(fx.replace('x', str(x))))

#polynomial = eval(fx.replace('x', str(x)))


