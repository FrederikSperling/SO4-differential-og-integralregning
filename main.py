import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from integralregning import *
from Differentialregning import *
import sympy
from plot import *


graf = graf()
graf.differentialregninggraf()
graf.integralregninggraf()
#Integral.skaeringmedx(200)


def func(x):
    #fx = eval(input.replace('x', str(x)))
    fx = sympy.sympify(input).subs(dict(x=x))
    return fx
