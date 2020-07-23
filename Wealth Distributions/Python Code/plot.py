import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.special import gamma
import system as s


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]


def histogram(N, alpha, beta, T, w, a, b, bins, S, M):
    h = np.zeros(len(bins) - 1)
    for i in range(M):
        v = s.sim(N, alpha, beta, T, w, a, b, bins, S)
        m, bins = np.histogram(v, bins=bins, density=True)
        h += m / M
    plt.bar(bins[:-1], h, align="edge", width=bins[1],
            ec=colors["cadetblue"], color=colors["powderblue"])
    binscenter = bins[:-1] + 0.5 * bins[1]
    E = np.sum (bins[1] * h * binscenter)
    Var = np.sum(bins[1]*binscenter**2 * h) - E**2
    return E, Var


def gammadistribution(bins, k, theta):
    return  bins **(k-1) * np.exp(- bins / theta) / (gamma(k)*theta**k)



def plot(x, y, xmax, ymax, title, xlabel, ylabel, color, legend):
    plt.ylim(0, ymax)
    plt.xlim(0, xmax)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plot =  plt.plot(x, y, color=colors[color], label=legend)
    plt.legend(handles=plot)
    plt.show()