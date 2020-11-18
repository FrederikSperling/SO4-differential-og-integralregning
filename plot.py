import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class plot:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = np.linspace(0, 10)
        self.y = self.func(self.x)

        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, 'r', linewidth=2)
        ax.set_ylim(bottom=0)

        # Make a shaded region
        # ix = np.linspace(a, b)
        # iy = func(ix)
        # verts = [(a, 0), *zip(ix, iy), (b, 0)]
        # poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
        # ax.add_patch(poly)

        #ax.text(0.5 * (self.a + self.b), 30, r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center', fontsize=20)

        fig.text(0.9, 0.05, '$x$')
        fig.text(0.1, 0.9, '$y$')

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')

        ax.set_xticks((self.a, self.b))
        ax.vlines(x=[self.a, self.b], ymin=0, ymax=[self.func(self.a), self.func(self.b)])
        # plt.axvline(x=a,ymin=0,ymax=func(a))
        # plt.axvline(x=b,ymin=0,ymax=func(b))
        ax.set_xticklabels(('$a$', '$b$'))
        ax.set_yticks([])

        plt.show()

    def func(self, x):
        return 3 * x**2


classplot = plot(2, 9)




