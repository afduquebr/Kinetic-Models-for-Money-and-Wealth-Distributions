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
    M = 5
    mu = 0.5
    sigma = 1.4
    bins = np.arange(0, 4, 0.1)


    # Generate Uniform Histogram
    #h = pl.histogram(N, alpha, beta, T, w, a, b, bins, S, M, mu, sigma)
    #k, theta = pl.gamma_parameters(bins, h)
    #gammastr = "Gamma(" + str(round(k,2)) + "," + str(round(theta,2))+")"
    #pl.plot(bins, pl.gamma_distribution(bins, k, theta), 4, 1, "Distribución de riqueza (f dist. uniforme)", "Riqueza", "Densidad de Probabilidad", "lightsalmon", gammastr)


    # Generate Gini Coefficient
    gini_plot = np.zeros(100)
    gini = 0
    for i in range(M):
        mw = s.sim(N, alpha, beta, T, w, a, b, bins, S, mu, sigma)
        gini_aux, gini_plot_aux = pl.gini(mw, N, w)
        gini += gini_aux/M
        gini_plot += gini_plot_aux/M
    pl.gini_plot(round(gini, 2), gini_plot)


    # Generate Normal Histogram
    #h = pl.histogram(N, alpha, beta, T, w, a, b, bins, S, M, mu, sigma)
    #k, theta = pl.gamma_parameters(bins, h)
    #gammastr = "Gamma(" + str(round(k,2)) + "," + str(round(theta,2))+")"
    #pl.plot(bins, pl.gamma_distribution(bins, k, theta), 4, 1, "Distribución de riqueza (f dist. normal con \u03C3 = 1.0)", "Riqueza", "Densidad de Probabilidad", "lightsalmon", gammastr)


    # Generate kappa and theta graphs
    #fgauss = pl.read_txt("fgauss-sigma-k-theta.txt",3)
    #pl.plot(fgauss[0], fgauss[1], 10.2, 22, " ", "\u03C3", "\u03BA", "lightcoral", "\u03BA(\u03C3)")
    #pl.plot(fgauss[0], fgauss[2], 10.2, 0.5, " ", "\u03C3", "\u03B8", "tomato", "\u03B8(\u03C3)")


    # Generate Entropy
    #s.sim(N, alpha, beta, T, w, a, b, bins, S, mu, sigma)
    #pl.plot(range(T), S, T, 1.3, " ", "Iteración","Entropía [bits]", "indianred", "Entropía de Shannon")


main()
