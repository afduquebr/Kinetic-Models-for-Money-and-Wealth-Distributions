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
    sigma = 0.125
    bins = np.arange(0, 4, 0.1)


    # Generate Uniform Histogram
    #h = pl.histogram(N, alpha, beta, T, w, a, b, bins, S, M, mu, sigma)
    #k, theta = pl.gamma_parameters(bins, h)
    #gammastr = "Gamma(" + str(round(k, 2)) + "," + str(round(theta, 2))+")"
    #pl.plot(bins, pl.gamma_distribution(bins, k, theta), 4, 1, "Distribución de Riqueza (f dist. uniforme)", "Riqueza", "Densidad de Probabilidad", "lightsalmon", gammastr)


    # Generate Gini Coefficient
    #gini_plot = np.zeros(100)
    #gini = 0
    #for i in range(M):
        #mw = s.sim(N, alpha, beta, T, w, a, b, bins, S, mu, sigma)
        #gini_aux, gini_plot_aux = pl.gini(mw, N, w)
        #gini += gini_aux/M
        #gini_plot += gini_plot_aux/M
    #pl.gini_plot(round(gini, 2), gini_plot)
    #print(gini)


    # Generate Gini vs Sigma and Mu graphs
    #gini_sigma = pl.read_txt("gini_sigma.txt", 2)
    #gini_mu = pl.read_txt("gini_mu.txt", 5)
    #pl.sigma_mu_gini(gini_sigma[0],0.36, "indianred", "Distribución Uniforme")
    #pl.plot(gini_sigma[0], gini_sigma[1], 1.6, 0.5, " ", "\u03C3", "Coeficiente de Gini", "coral", "Distribución Normal con \u03BC = 0.5")
    #pl.sigma_mu_gini(gini_mu[0], gini_mu[1], "lightpink", "Distribución Normal con \u03C3 = 0.125")
    #pl.sigma_mu_gini(gini_mu[0], gini_mu[2], "lightcoral", "Distribución Normal con \u03C3 = 0.25")
    #pl.sigma_mu_gini(gini_mu[0], gini_mu[3], "palevioletred", "Distribución Normal con \u03C3 = 0.375")
    #pl.sigma_mu_gini(gini_mu[0], gini_mu[4], "indianred", "Distribución Normal con \u03C3 = 0.5")
    #pl.plot(gini_mu[0], 0.36, 1, 0.6, " ", "\u03BC", "Coeficiente de Gini", "brown", "Distribución Uniforme")


    # Generate Normal Histogram
    #h = pl.histogram(N, alpha, beta, T, w, a, b, bins, S, M, mu, sigma)
    #k, theta = pl.gamma_parameters(bins, h)
    #gammastr = "Gamma(" + str(round(k,2)) + "," + str(round(theta,2))+")"
    #pl.plot(bins, pl.gamma_distribution(bins, k, theta), 4, 1, "Distribución de riqueza (f dist. normal con \u03C3 = 1.0)", "Riqueza", "Densidad de Probabilidad", "lightsalmon", gammastr)


    # Generate alpha and beta graphs in terms of sigma and mu
    #fgauss_sigma = pl.read_txt("fgauss-sigma-alpha-beta.txt", 3)
    #for i in range(len(fgauss_sigma[2])):
        #fgauss_sigma[2][i] = 1/fgauss_sigma[2][i]
    #pl.alpha_beta_sigma(fgauss_sigma[0], 2)
    #pl.plot(fgauss_sigma[0], fgauss_sigma[1], 10.2, 22, "\u03C9 = 1", "\u03C3", "\u03BA", "coral", "Distribución normal con \u03BC = 0.5")
    #pl.alpha_beta_sigma(fgauss_sigma[0], 2)
    #pl.plot(fgauss_sigma[0], fgauss_sigma[2], 10.2, 22, "\u03C9 = 1", "\u03C3", "\u03B8", "coral", "Distribución normal con \u03BC = 0.5")
    #fgauss_mu = pl.read_txt("fgauss-mu-alpha-beta.txt", 3)
    #pl.plot(fgauss_mu[0], fgauss_mu[1], 0.9, 22, "\u03C9 = 1", "\u03BC", "\u03BA", "coral", "Distribución normal con \u03C3 = 0.125")
    #pl.plot(fgauss_mu[0], fgauss_mu[2], 0.9, 22, "\u03C9 = 1", "\u03BC", "\u03B8", "coral", "Distribución normal con \u03C3 = 0.125")


    # Generate Entropy
    #s.sim(N, alpha, beta, T, w, a, b, bins, S, mu, sigma)
    #entropy = open('entropy.txt', 'w')
    #for i in range(1,T+1):
        #entropy.write('%d %.6f \n' %(i, S[i-1]))
    #pl.plot(range(T), S, T, 1.3, " ", "Iteración","Entropía [bits]", "indianred", "Entropía diferencial")


    # Generate Total Wealth and Price histograms
    #wealth_price = pl.read_txt("TW-P-S-5prom.txt", 3)
    #bins1 = np.arange(1.98, 2.02, 0.001)
    #pl.histograux(bins1, wealth_price[1])
    #pl.plot(bins1, pl.normal_distribution(bins1, 2.00004, 0.00597), 1.98, 2.02, 75, " ", "Riqueza Total", "Densidad de Probabilidad", "lightsalmon", "\u03BC = 2.00004,\u03C3 = 0.00597")
    #bins2 = np.arange(0.98, 1.02, 0.001)
    #pl.histograux(bins2, wealth_price[2])
    #pl.plot(bins2, pl.normal_distribution(bins2, 1.00004, 0.00597), 0.98, 1.02, 75, " ", "Precio", "Densidad de Probabilidad", "lightsalmon", "\u03BC = 1.00004,\u03C3 = 0.00597")


    #Generate Kappa and Theta vs Alpha, Beta and Omega figures
    #kappa_theta = pl.read_txt("beta_kappa_theta.txt", 3)
    #Kappa
    #pl.plot(kappa_theta[0], kappa_theta[1], 5.5, 1.5, " ", "\u03B2", "\u03BA", "steelblue", "Relación entre \u03BA y \u03B2")
    #Theta
    #for i in range(len(kappa_theta[2])):
        #kappa_theta[2][i] = 1/kappa_theta[2][i]
    #pl.kappa_theta(kappa_theta[0], kappa_theta[2], "Relación entre \u03B8 y \u03B2")
    #pl.plot(kappa_theta[0], pl.straight_line(np.arange(0.5, 5.5, 0.5), 0.99786, 0.00404), 5.5, 6, " ", "\u03B2", "\u03B8", "skyblue", "Ajuste Lineal")

    # Equilibrium Time
    #S = pl.read_txt('entropy.txt', 2)
    #pl.sigma_mu_gini(S[0], 1.137307083, "orange", "Valor mínimo")
    #pl.sigma_mu_gini(S[0], 1.283218639, "saddlebrown", "Valor máximo")
    #pl.plot(S[0], S[1], T, 1.35, " ", "Iteración", "Entropía [bits]", "indianred", "Entropía diferencial")

main()
