import math

from scipy.misc import derivative


def check_init_approx(f, x0):
    return f(x0) * derivative(f, x0, n=2)


def dif_approx(f, cur, prev):
    return (f(cur) - f(prev)) / (cur - prev)


def h(f, x0):
    return f(x0) / derivative(f, x0)


def is_root_exist(f, x1, x2):
    return f(x1) * f(x2) < 0


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
    M = 1
    while M > eps:
        k += 1
        H = dif_approx(f, c_prev, c_prev1)
        if H == 0:
            print('Разностное приближение =  0. Нельзя делить на ноль')
            exit(0)
        c = c_prev - f(c_prev) / H
        c_prev1, c_prev = c_prev, c
        M = abs(c_prev - c_prev1)
        print(f'Приближённый корень на {k}-й итерации = {c}')
    return c, k


def is_pos_der(f, x0):
    return derivative(f, x0) > 0


def get_lambda(a, b):
    if a > b:
        l = -1 / abs(a) if a > 0 else 1 / abs(a)
    else:
        l = -1 / abs(b) if b > 0 else 1 / abs(b)
    return l


def check_conv_cond_for_eq(l, m):
    max_dfi = abs(l * m + 1)
    print(f'Коэффициент сходимости = %.3f' % max_dfi)
    return max_dfi < 1


def iteration_method(f, a, b, eps):
    print('---Метод простой итерации---')
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

    if check_conv_cond_for_eq(l, max(a_der, b_der)):
        print('Достаточное условие сходимости метода выполняется')
    else:
        print('Достаточное условие сходимости метода не выполняется')

    while abs(x - x_prev) > eps:
        if k != 0:
            x_prev = x
        if not is_pos_der(f, x_prev):
            l = -l
        x = l * f(x_prev) + x_prev
        k += 1
        print(f'Приближённый корень на {k}-й итерации = %.3f' % x)
    return x, k


def dfx1(func, x1, x2):
    dx = 1e-6
    return (func(x1 + dx, x2) - func(x1 - dx, x2)) / (2.0 * dx)


def dfx2(func, x1, x2):
    dx = 1e-6
    return (func(x1, x2 + dx) - func(x1, x2 - dx)) / (2.0 * dx)


def get_partial_der_arr(f_arr, x1_init, x2_init):
    # формируем частные производные
    dx1_fi1 = dfx1(f_arr[0], x1_init, x2_init)
    dx2_fi1 = dfx2(f_arr[0], x1_init, x2_init)

    dx1_fi2 = dfx1(f_arr[1], x1_init, x2_init)
    dx2_fi2 = dfx2(f_arr[1], x1_init, x2_init)
    return [dx1_fi1, dx2_fi1, dx1_fi2, dx2_fi2]


def check_conv_for_sys_eq(p_ders):
    first_sum = abs(p_ders[0]) + abs(p_ders[1])
    sec_sum = abs(p_ders[2]) + abs(p_ders[3])
    if max(first_sum, sec_sum) < 1:
        print('Достаточное условие сходимости метода выполняется')
    else:
        print('Достаточное условие сходимости метода не выполняется')


def sys_iteration_method(f_arr, x1_init, x2_init, eps):
    print('--Метод простой итерации---')
    k = 0
    x1, x2 = 0, 0

    fi_arr = [
        lambda _x1, _x2: _x1 - f_arr[0](_x1, _x2),
        lambda _x1, _x2: _x2 - f_arr[1](_x1, _x2)
    ]

    check_conv_for_sys_eq(get_partial_der_arr(fi_arr, x1_init, x2_init))
    x1_prev, x2_prev = x1_init, x2_init
    M = 1

    while M > eps:
        k += 1
        x1 = fi_arr[0](x1_prev, x2_prev)
        x2 = fi_arr[1](x1_prev, x2_prev)
        print(f'Приближённое решение системы на {k}-й итерации (%.3f, %.3f)' % (x1, x2))
        M = max(abs(x1 - x1_prev), abs(x2 - x2_prev))
        x1_prev, x2_prev = x1, x2
    return x1, x2, k
