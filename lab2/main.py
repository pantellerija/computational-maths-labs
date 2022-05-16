import math

import numpy as np
from matplotlib import pyplot as plt

import methods as meth
import sympy as sp

import io_lib

# 1.045 1m(0.0005) -1.8 2m(0.002)--[3.14;4.71] 1.172 2m(0.0025)
flist = [
    lambda x: x**5 - x - 0.2,
    lambda x: x**3 - x + 4,
    lambda x: x - math.sin(x) - 0.25
]

nonlinear_system = [
    lambda x1, x2: 0.1*x1**2 + x1 + 0.2*x2**2 - 0.3,
    lambda x1, x2: 0.2*x1**2 + x2 - 0.1*x1*x2 - 0.7
]

mlist = [
    meth.secant_method,
    meth.iteration_method
]

sys_inplist = [
    io_lib.get_console_intervals,
    io_lib.read_file
]

nonlinear_sys = '0.1x1^2+x1+0.2x2^2-0.3=0,\n' \
                    '0.2xq^2+x2-0.1x1*x2-0.72=0\n'

eps = 0.0005


def build_plot_sys():
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    sp.plot_implicit(sp.Or(sp.Eq(nonlinear_system[0](x, y), 0), sp.Eq(
        nonlinear_system[1](x, y), 0)))


def build_plot_eq(func, left, right, y_l, y_r):
    x = np.linspace(left, right, 10000)
    f = np.vectorize(func)
    x_step = 0.2
    y_step = 20

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.plot(x, f(x), "g", linewidth=2.0)

    ax.set(xlim=(left, right), xticks=np.arange(left, right, x_step),
           ylim=(y_l, y_r), yticks=np.arange(y_l, y_r, y_step))

    plt.show()


if __name__ == '__main__':
    if io_lib.get_choice() == 1:
        print('Система нелинейныйх уравнений: ')
        print(nonlinear_sys)
        a, b = sys_inplist[io_lib.get_data_source()]()
        x1, x2, iter_num = meth.sys_iteration_method(nonlinear_system, a, b, eps)
        print(f'Найденный корень системы уравнений = (%.3f; %.3f) с точностью ε = {eps}' % (x1, x2))
        print(f'Число итераций: {iter_num}')
        build_plot_sys()
    else:
        f_ind, a, b, m_id = io_lib.get_console_inputs_for_eq()
        y = flist[f_ind]
        if meth.is_root_exist(y, a, b):
            ans, iter_num = mlist[m_id](y, a, b, eps)
            print(f'Найденный корень уравнения = %.3f с точностью ε = {eps}' % ans)
            print(f'Значение функции при x = %.3f: %.d' % (ans, y(ans)))
            print(f'Число итераций: {iter_num}')
            build_plot_eq(y, a-0.5, b+0.5, y(a)-0.5, y(b)+0.5)
        else:
            print(f'У уравнения на интервале [{a};{b}] нет корней. Поменяйте границы интервала')
