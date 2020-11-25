import matplotlib.pyplot as plt

class graf():
    def __init__(self):
        pass

    def xlabel(self, xlabel, xlabelname, color):
        if xlabel == True:
            plt.xlabel(str(xlabelname), color=color)

    def ylabel(self, ylabel, ylabelname, color):
        if ylabel == True:
            plt.ylabel(str(ylabelname), color=color)