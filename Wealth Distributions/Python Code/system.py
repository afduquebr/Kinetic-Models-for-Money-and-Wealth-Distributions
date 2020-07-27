import numpy as np


def sim(N, alpha, beta, T, w, a, b, bins, S, mu, sigma):
    for i in range(1, T+1):
        f = np.random.uniform(0, 1, N)
        #f = blockednormal(mu,sigma,N)
        p = price(a, b, f)
        m = wealth(a, b, p)
        a = f * m
        b = (1 - f) * m / p
        mw = w * m /(alpha + (beta * p))
        S[i-1] = entropy(mw, bins)
    mw = w * m /(alpha + (beta * p))
    return mw


def price(a, b, f):
    p = np.dot((1 - f), a)
    q = np.dot(f, b)
    return p / q


def wealth(a, b, p):
    w = a + (b * p)
    return w


def entropy(v, bins):
    m, bins = np.histogram(v, bins=bins, density=True)
    return np.sum(np.where(m != 0, - m * np.log2(m) * bins[1], 0))

def blockednormal(mu,sigma,N):
    random = np.zeros(N)
    for i in range(N):
        while True:
            numb = np.random.normal(mu,sigma)
            if (numb >= 0 and numb <= 1):
                break
        random[i] = numb
    return random