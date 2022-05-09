import math
from scipy.misc import derivative


def check_init_approx(f, x0):
    return f(x0)*derivative(f, x0, n=2)


def dif_approx(f, cur, prev):
    return (f(cur) - f(prev))/(cur - prev)


def h(f, x0):
    return f(x0)/derivative(f, x0)


def is_root_exist(f, x1, x2):
    return f(x1)*f(x2) < 0


# проблема с отриц интервалом
def secant_method(f, a, b, eps):
    print('-----Метод секущих-----')
    c = math.inf
    c_prev = 0
    k = 0
    if check_init_approx(f, a):
        c_prev = a
    elif check_init_approx(f, b):
        c_prev = b
    c_prev1 = c_prev - h(f, c_prev)
    while abs(c_prev-c_prev1) > eps:
        c = c_prev - f(c_prev)/dif_approx(f, c_prev, c_prev1)
        c_prev1, c_prev = c_prev, c
        k += 1
        print(f'Приближённый корень на {k}-й итерации = %.3f' % c)
    return c, k


def is_pos_der(f, x0):
    return derivative(f, x0) > 0


def get_lambda(a, b):
    if a > b:
        l = -1/abs(a) if a > 0 else 1/abs(a)
    else:
        l = -1/abs(b) if b > 0 else 1/abs(b)
    return l


def check_conv_cond(l, m):
    max_dfi = abs(l*m + 1)
    print(f'Коэффициент сходимости = %.3f' % max_dfi)
    return max_dfi < 1


def iteration_method(f, a, b, eps):
    print('-----Метод простой итерации-----')
    x = math.inf
    k = 0
    x_prev = 0

    if check_init_approx(f, a):
        x_prev = a
    elif check_init_approx(f, b):
        x_prev = b

    a_der = derivative(f, a)
    b_der = derivative(f, b)

    l = get_lambda(a_der, b_der)

    if check_conv_cond(l, max(a_der, b_der)):
        print('Достаточное условие сходимости метода выполняется')
    else:
        print('Достаточное условие сходимости метода не выполняется')

    while abs(x - x_prev) > eps:
        if k != 0:
            x_prev = x
        if not is_pos_der(f, x_prev):
            l = -l
        x = l*f(x_prev) + x_prev
        k += 1
        print(f'Приближённый корень на {k}-й итерации = %.3f' % x)
    return x, k




