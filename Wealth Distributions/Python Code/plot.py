import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.special import gamma
import system as s


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]


def histogram(N, alpha, beta, T, w, a, b, bins, S, M, mu, sigma):
    h = np.zeros(len(bins) - 1)
    for i in range(M):
        v = s.sim(N, alpha, beta, T, w, a, b, bins, S, mu, sigma)
        m, bins = np.histogram(v, bins=bins, density=True)
        h += m / M
    plt.bar(bins[:-1], h, align="edge", width=bins[1],
            ec=colors["cadetblue"], color=colors["powderblue"])
    return h

def histograux(bins, v):
    m, bins = np.histogram(v, bins=bins, density=True)
    plt.bar(bins[:-1], m, align="edge", width=0.0003,
            ec=colors["cadetblue"], color=colors["powderblue"])
    return m

def gamma_parameters(bins,h):
    binscenter = bins[:-1] + 0.5 * bins[1]
    E = np.sum(bins[1] * h * binscenter)
    Var = np.sum(bins[1] * binscenter ** 2 * h) - E ** 2
    k = E ** 2 / Var
    theta = Var / E
    return k, theta


def gamma_distribution(bins, k, theta):
    return  bins **(k-1) * np.exp(- bins / theta) / (gamma(k)*theta**k)

def normal_distribution(bins, mu, sigma):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-((bins - mu)**2/(2*(sigma**2))))

def straight_line(bins, m, b):
    return m*bins + b

def read_txt(filename, rows):
    file = open(filename, 'r')
    lines = file.readlines()
    data = list()
    for i in range(rows):
        aux = list()
        for line in lines:
            aux.append(float(line.split()[i]))
        data.append(aux)
    return data


def gini(mw, N, w):
    mw_aux = np.sort(mw)
    maux = np.zeros(100)
    sum = 0
    fair_area = 100*100/2
    for i in range(1,N+1):
        sum += mw_aux[i-1]*100/(w*N)
        if (i%(0.01*N) == 0):
            j = i/10
            maux[int(j)-1] += sum
    gini = (fair_area - np.sum(maux))/fair_area
    return gini, maux

def gini_plot(gini, giniplot):
    string = "Medida de desigualdad (g=" + str(gini) + ")"
    gin = plt.plot(range(1, 101), range(1, 101), '--', color=colors["firebrick"], label="Curva de igualdad perfecta")
    plot(range(1, 101), giniplot, 100, 100, string, "Porcentaje de población", "Porcentaje de riqueza", "lightcoral",
            "Curva de Lorenz")

def sigma_mu_gini(x,y, color, legend):
    plt.plot(x, np.full(len(x), y), color=colors[color], label=legend)

def alpha_beta_sigma(x,y):
    ab_sigma = plt.plot(x, np.full(len(x), y), '--', color=colors["indianred"], label="Districuión uniforme")

def kappa_theta(x, y, legend):
    plt.plot(x, y, 'o', color=colors["dodgerblue"], label=legend)

def plot(x, y, xmax, ymax, title, xlabel, ylabel, color, legend):
    plt.ylim(1, ymax)
    plt.xlim(0, xmax)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yscale('log')
    plot = plt.plot(x, y, color=colors[color], label=legend)
    plt.legend()
    plt.show()