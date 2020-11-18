import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from Integralregning import *
from Diffentialregning import *
from plot import *



#Desto mere præcis svar man gerne have, jo højere antal søjler (streg) skriver man bare ind i klassen hvor mange man vil have.
#Hvis man gerne vil have et meget præcist svar kommer det til at vente lidt fordi det tager en del tid at beregne for computeren.
#F.eks. 1000 søjler = 1 sekund, 100.000.000 = 20 min, 1.000.000 = 10 sekunder
#Man kan også fjerne print for x, y og streg hvis det skal gå hurtigere.
Integral = Integralregning(-10, 10, 200, 2, 6, 5, 2)
testplotclass = Testplot()
