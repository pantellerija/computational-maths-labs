import matplotlib.pyplot as plt
import numpy as np


def graph(func, lin_approx, qd_approx, qub_approx, exp_approx, log_approx, pow_approx):
    x_args = func[0]
    y_args = func[1]

    max_x = max(x_args)
    min_x = min(x_args)

    max_y = max(y_args)
    min_y = min(y_args)

    x = np.linspace(min_x - 0.5, max_x + 0.5, 10000)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.plot(x, lin_approx(x), "r", linewidth=2.0, label="linear")
    ax.plot(x, qd_approx(x), "g", linewidth=2.0, label="squad")
    ax.plot(x, qub_approx(x), "b", linewidth=2.0, label="cube")
    if exp_approx is not None:
        ax.plot(x, exp_approx(x), "blue", linewidth=2.0, label="exp")
    x = np.linspace(0.000001, max_x + 0.5, 10000)
    if log_approx is not None:
        log_approx2 = np.vectorize(log_approx)
        ax.plot(x, log_approx2(x), "darkred", linewidth=2.0, label="log")
    if pow_approx is not None:
        pow_approx2 = np.vectorize(pow_approx)
        ax.plot(x, pow_approx2(x), "purple", linewidth=2.0, label="deg")
    ax.legend()
    ax.plot(x_args, y_args, linewidth=0, marker="*", markersize=10, markeredgecolor="black", markerfacecolor="green")

    ax.set(xlim=(min_x - 0.5, max_x + 0.5), xticks=np.arange(min_x, max_x, 0.5),
           ylim=(min_y - 0.5, max_y + 0.5), yticks=np.arange(min_y, max_y, 0.5))

    plt.show()

