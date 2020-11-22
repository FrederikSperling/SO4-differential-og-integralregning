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

input = input("Polynomial here")

def func(x):
    #fx = eval(input.replace('x', str(x)))
    fx = sympy.sympify(input).subs(dict(x=x))
    return fx
    #fx = str(sympy.sympify(input).subs(dict(x=x)))
    #fx2 = eval(fx)
    #return fx2

xlin = np.linspace(-100, 1000, num=1000)
ylist = []
listpos = 0
for values in xlin:
    yvalue = func(xlin[listpos])
    ylist.append(yvalue)
    listpos += 1

print(ylist)
fig, ax = plt.subplots()
ax.plot(xlin, ylist, 'black', linewidth=2)
plt.show()
