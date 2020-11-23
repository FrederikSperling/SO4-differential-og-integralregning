from GUI import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from integralregning import *
from Differentialregning import *
import sympy
from plot import *

app.mainloop()

graf = graf()
graf.differentialregninggraf()
graf.integralregninggraf()
#Integral.skaeringmedx(200)
