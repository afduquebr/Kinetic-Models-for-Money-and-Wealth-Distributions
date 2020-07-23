import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]


N = 1000  # N es el número de agentes
alpha = 1  # alpha es el dinero promedio
beta = 1  # beta es la cantidad de bienes promedio
T = 10 * N  # Tiempo de evolución
w = 1

a = np.full(N, alpha)
b = np.full(N, beta)

def main():
    M = 10
    bins = np.arange(0, 4, 0.1)
    histogram(bins, M)
    plot(bins)



def sim(a, b):
    for i in range(1, T + 1):
        f = np.random.uniform(0, 1, N)
        p = price(a, b, f)
        m = wealth(a, b, p)
        a = f * m
        b = (1 - f) * m / p
    mw = w * m /(alpha + (beta * p))
    return mw


def price(a, b, f):
    p = np.dot((1 - f), a)
    q = np.dot(f, b)
    return p / q


def wealth(a, b, p):
    wealth = a + (b * p)
    return wealth

def entropy(p, dp):
    return np.sum(- p * np.log2(p) * dp)

def histogram(bins, M):
    h = np.zeros(len(bins)-1)
    for i in range(M):
        v = sim(a, b)
        m, bins = np.histogram(v, bins=bins, density=True)
        h += m/M
    plt.bar(bins[:-1], h, align="edge", width=bins[1],
            ec=colors["cadetblue"], color=colors["powderblue"])


def plot(bins):
    plt.ylim(0, 1)
    plt.xlim(0, 4)
    plt.title("T = %.d" %T)
    plt.xlabel("Riqueza")
    plt.ylabel("Probabilidad")
    gamma = ((2/w)**2) * bins * np.exp(-2*bins/w)
    plt.plot(bins, gamma, color=colors["lightsalmon"])
    plt.show()


main()