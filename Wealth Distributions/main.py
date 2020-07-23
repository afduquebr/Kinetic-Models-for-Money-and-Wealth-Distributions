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
S = np.zeros(T) #Entropía para cada tiempo
M2 = 5
bin = 0.1
M = 10


def main():
    bins = np.arange(0, 4, bin)
    histogram(bins, M)
    plot(bins, exponential(bins, beta))
    



def sim(a, b, bins, S):
    for i in range(1, T+1):
        f = np.random.uniform(0, 1, N)
        p = price(a, b, f)
        m = wealth(a, b, p)
        a = f * m
        b = (1 - f) * m / p
        mw = w * m /(alpha + (beta * p))
        S[i-1] = entropy(mw, bins, M2)
    return b


def price(a, b, f):
    p = np.dot((1 - f), a)
    q = np.dot(f, b)
    return p / q


def wealth(a, b, p):
    wealth = a + (b * p)
    return wealth

def entropy(v, bins, M):
    h = np.zeros(len(bins)-1)
    for i in range(M):
        m, bins = np.histogram(v, bins=bins, density=True)
        h += m/M
    return np.sum(np.where(h != 0,  - h * np.log2(h) * bins[1], 0))

def histogram(bins, M):
    h = np.zeros(len(bins)-1)
    for i in range(M):
        v = sim(a, b, bins, S)
        m, bins = np.histogram(v, bins=bins, density=True)
        h += m/M
    plt.bar(bins[:-1], h, align="edge", width=bins[1],
            ec=colors["cadetblue"], color=colors["powderblue"])


def gamma(bins):
    return ((2/w)**2) * bins * np.exp(-2*bins/w)

def exponential(bins, theta):
    return (1/theta)*np.exp(-bins/theta)
    

def plot(x,y):
    plt.ylim(0, 1)
    plt.xlim(0, 4)
    plt.title("Entropía de Shannon")
    plt.xlabel("Iteración")
    plt.ylabel("Entropía [bits]")
    plt.plot (x,y, color=colors["lightsalmon"])
    plt.show()

main()