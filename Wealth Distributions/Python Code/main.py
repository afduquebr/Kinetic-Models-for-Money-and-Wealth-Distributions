import numpy as np
import system as s
import plot as pl


def main():
    N = 1000  # N es el número de agentes
    alpha = 1  # alpha es el dinero promedio
    beta = 1  # beta es la cantidad de bienes promedio
    T = 10 * N  # Tiempo de evolución
    w = 1
    a = np.full(N, alpha)
    b = np.full(N, beta)
    S = np.zeros(T)  # Entropía para cada tiempo
    M = 10
    mu = 0.5
    sigma = 0.875
    bins = np.arange(0, 4, 0.1)
    h = pl.histogram(N, alpha, beta, T, w, a, b, bins, S, M, mu, sigma)
    k, theta = pl.gamma_parameters(bins, h)
    gammastr = "Gamma(" + str(round(k,2)) + "," + str(round(theta,2))+")"
    pl.plot(bins, pl.gamma_distribution(bins, k, theta), 4, 1, "Distribución de riqueza (f dist. normal con \u03C3 = 0.875)",
            "Riqueza", "Densidad de Probabilidad", "lightsalmon", gammastr)
    #s.sim(N, alpha, beta, T, w, a, b, bins, S, mu, sigma)
    #pl.plot(range(T), S, T, 1.3, "Entropía de Shannon", "Iteración","Entropía [bits]", "limegreen", "Shannon's Entropy")


main()
