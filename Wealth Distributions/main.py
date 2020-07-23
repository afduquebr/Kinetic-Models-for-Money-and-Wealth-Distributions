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
    nsim = 10  # Número de simulaciones para promediar
    heights = np.zeros(39)  # Alturas de las barras
    bins = np.arange(0, 4, 0.1)  # Bins con espaciamiento 0.01

    for i in range(nsim):
        print(i)
        wealth = sim(a, b)  # Simulación
        n, bins, histograux = plt.hist(wealth, bins=bins, density=True, stacked=True)  # Histograma
        plot(histograux, bins)
        heights = heights + (n / nsim)  # Promediando
    br = plt.bar(bins[:-1], heights, align="edge", width=0.1, ec=colors["cadetblue"], color=colors["powderblue"])  # Diagrama de barras
    plot(br, bins)  # Plot

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

def plot(x, bi):
  plt.ylim(0,1)
  plt.xlim(0,4)
  plt.title("T = %.d" %(T))
  plt.xlabel("Riqueza")
  plt.ylabel("Probabilidad")
  expvalues = 4 * bi * np.exp(-2*bi) #Para graficar la exponencial
  #histogram = x #Histograma
  expplot = plt.plot(bi, expvalues, color=colors["lightsalmon"]) #Exponencial
  plt.show()

main()