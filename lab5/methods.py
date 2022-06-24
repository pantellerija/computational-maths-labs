import numpy as np
from matplotlib import pyplot as plt


def L(x_p, y_p, x):
    n = len(x_p)
    lin_comb = 0
    for i in range(n):
        l = y_p[i]
        for j in range(n):
            if i != j:
                l *= (x - x_p[j]) / (x_p[i] - x_p[j])
        lin_comb += l
    return lin_comb


def N(x_p, y_p, x):
    n = len(x_p)
    fin_diffs = np.zeros([n, n])
    y = np.zeros(n)

    # the first column is y
    for i in range(n):
        fin_diffs[i][0] = y_p[i]

    # divided differences
    for j in range(1, n):
        for i in range(n - j):
            fin_diffs[i][j] = (fin_diffs[i + 1][j - 1] - fin_diffs[i][j - 1]) / (x_p[i + j] - x_p[i])

    a = 1
    y[0] = fin_diffs[0][0]
    for k in range(1, n):
        a = a * (x - x_p[k - 1])
        y2 = y[k - 1] + fin_diffs[0][k] * a
        y[k] = y2
    return y


def graph(x_arr, y_arr, polynom):
    xx = np.linspace(np.min(x_arr) - 2, np.max(x_arr) + 2, 1000)
    yy = [polynom(x_arr, y_arr, i) for i in xx]
    plt.scatter(x_arr, y_arr, color='darkblue', s=30, marker='o')
    plt.plot(xx, yy, linewidth=1.0, color="black")
    plt.grid(True, which='both')
    plt.axvline(x=0, color='k')
    plt.axhline(y=0, color='k')
    plt.show()



