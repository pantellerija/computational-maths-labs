import math

import numpy as np

from lab4.slau import solve_sys, make_diagonal


def linear_approx(func):
    print('---Линейная аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    s_x = sum(x_args)
    avrg_x = s_x / n

    s_y = sum(y_args)
    avrg_y = s_y / n

    xx_args = [i * i for i in x_args]
    s_xx = sum(xx_args)

    xy_args = [x_args[i] * y_args[i] for i in range(n)]
    s_xy = sum(xy_args)

    delta = s_xx * n - s_x * s_x
    delta1 = s_xy * n - s_x * s_y
    delta2 = s_xx * s_y - s_x * s_xy

    a = delta1 / delta
    b = delta2 / delta

    print('Коэффициент a:', a)
    print('Коэффициент b:', b)
    apprx_func = lambda x: a * x + b

    # Мера отклонения
    S = 0

    k = 0
    num_pirs = 0
    func_arr = [0] * n
    e_arr = [0] * n
    p_arr = [0.0] * n
    xq_dev = [0] * n
    yq_dev = [0] * n
    for i in range(n):
        # Вычисления для коэф-та Пирсона
        x_diff = x_args[i] - avrg_x
        y_diff = y_args[i] - avrg_y
        xq_dev[i] = x_diff * x_diff
        yq_dev[i] = y_diff * y_diff
        xy = x_diff * y_diff
        num_pirs += xy

        # МНК
        func_arr[i] = apprx_func(x_args[i])
        e_arr[i] = func_arr[i] - y_args[i]
        p_arr[i] = e_arr[i] / func_arr[i]
        e_kv = e_arr[i] * e_arr[i]
        S += e_kv
        k += 1
        print(f'{k}-я итерация:')
        print(f'Значение аппроксимирующей функции: {func_arr[i]}')
        print(f'Отклонение: {e_arr[i]}')
        print(f'Оценка относительной погрешности аппроксимации: {p_arr[i]}')
    xq_sum = sum(xq_dev)
    yq_sum = sum(yq_dev)
    sko = math.sqrt(S/n)

    # Коэффициент корреляции Пирсона:
    r = num_pirs / math.sqrt(xq_sum * yq_sum)
    return apprx_func, func_arr, e_arr, p_arr, S, sko, r


def quad_approx(func):
    print('---Квадратичная аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    s_x = sum(x_args)
    s_y = sum(y_args)

    xx_args = [i * i for i in x_args]
    s_xx = sum(xx_args)

    x_3args = [i * i * i for i in x_args]
    s_3x = sum(x_3args)

    xy_args = [x_args[i] * y_args[i] for i in range(n)]
    s_xy = sum(xy_args)

    x_4args = [i * i * i * i for i in x_args]
    s_4x = sum(x_4args)

    xxy_args = [xx_args[i] * y_args[i] for i in range(n)]
    s_xxy = sum(xxy_args)

    matrix = np.array([[n, s_x, s_xx, s_y],
                       [s_x, s_xx, s_3x, s_xy],
                       [s_xx, s_3x, s_4x, s_xxy]])
    solve_sys(matrix)
    make_diagonal(matrix)

    ans = matrix[:, -1]
    a0, a1, a2 = ans[0], ans[1], ans[2]
    print('a0: ', ans[0])
    print('a1: ', ans[1])
    print('a2: ', ans[2])

    apprx_func = lambda x: a0 + a1 * x + a2 * x * x

    func_arr = [0] * n
    e_arr = [0] * n
    p_arr = [0.0] * n
    k = 0
    S = 0  # мера отклонения

    for i in range(n):
        func_arr[i] = apprx_func(x_args[i])
        e_arr[i] = func_arr[i] - y_args[i]
        p_arr[i] = e_arr[i] / func_arr[i]
        e_kv = e_arr[i] * e_arr[i]
        S += e_kv
        k += 1
        print(f'{k}-я итерация:')
        print(f'Значение аппроксимирующей функции: {func_arr[i]}')
        print(f'Отклонение: {e_arr[i]}')
        print(f'Оценка относительной погрешности аппроксимации: {p_arr[i]}')
    sko = math.sqrt(S/n)
    return apprx_func, func_arr, e_arr, p_arr, S, sko


def qubic_approx(func):
    print('---Кубическая аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    s_x = sum(x_args)
    s_y = sum(y_args)

    xx_args = [i * i for i in x_args]
    s_xx = sum(xx_args)

    x_3args = [i * i * i for i in x_args]
    s_3x = sum(x_3args)

    xy_args = [x_args[i] * y_args[i] for i in range(n)]
    s_xy = sum(xy_args)

    x_4args = [i * i * i * i for i in x_args]
    s_4x = sum(x_4args)

    x_5args = [x_4args[i] * x_args[i] for i in range(n)]
    s_5x = sum(x_5args)

    x_6args = [x_5args[i] * x_args[i] for i in range(n)]
    s_6x = sum(x_6args)

    xxy_args = [xx_args[i] * y_args[i] for i in range(n)]
    s_xxy = sum(xxy_args)

    x3y_args = [x_3args * y_args[i] for i in range(n)]
    s_3xy = sum(x3y_args)

    matrix = np.array([[n, s_x, s_xx, s_3x, s_y],
                       [s_x, s_xx, s_3x, s_4x, s_xy],
                       [s_xx, s_3x, s_4x, s_5x, s_xxy],
                       [s_3x, s_4x, s_5x, s_6x, s_3xy]])
    solve_sys(matrix)
    make_diagonal(matrix)

    ans = matrix[:, -1]
    a0, a1, a2, a3 = ans[0], ans[1], ans[2], ans[3]
    print('a0: ', a0)
    print('a1: ', a1)
    print('a2: ', a2)
    print('a3: ', a3)

    apprx_func = lambda x: a0 + a1 * x + a2 * x * x + a3 * x * x * x

    func_arr = [0] * n
    e_arr = [0] * n
    p_arr = [0.0] * n
    k = 0
    S = 0  # мера отклонения
    for i in range(n):
        func_arr[i] = apprx_func(x_args[i])
        e_arr[i] = func_arr[i] - y_args[i]
        p_arr[i] = e_arr[i] / func_arr[i]
        e_kv = e_arr[i] * e_arr[i]
        S += e_kv
        k += 1
        print(f'{k}-я итерация:')
        print(f'Значение аппроксимирующей функции: {func_arr[i]}')
        print(f'Отклонение: {e_arr[i]}')
        print(f'Оценка относительной погрешности аппроксимации: {p_arr[i]}')
    sko = math.sqrt(S/n)
    return apprx_func, func_arr, e_arr, p_arr, S, sko


def exp_approx(func):
    print('---Экспоненциальная аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    for i in y_args:
        if i <= 0:
            raise RuntimeError('Значение функции не удовлетворяет ОДЗ логарифма')

    lny_args = [math.log(i) for i in y_args]
    s_x = sum(x_args)
    s_y = sum(lny_args)

    xx_args = [i * i for i in x_args]
    s_xx = sum(xx_args)

    xy_args = [x_args[i] * lny_args[i] for i in range(n)]
    s_xy = sum(xy_args)

    delta = s_xx * n - s_x * s_x
    delta1 = s_xy * n - s_x * s_y
    delta2 = s_xx * s_y - s_x * s_xy

    a = delta1 / delta
    b = delta2 / delta

    print('Коэффициент a:', a)
    print('Коэффициент b:', b)
    apprx_func = lambda x: a * x + math.log(b)

    # Мера отклонения
    S = 0

    k = 0
    func_arr = [0] * n
    e_arr = [0] * n
    p_arr = [0.0] * n
    for i in range(n):
        # МНК
        func_arr[i] = apprx_func(x_args[i])
        e_arr[i] = func_arr[i] - y_args[i]
        p_arr[i] = e_arr[i] / func_arr[i]
        e_kv = e_arr[i] * e_arr[i]
        S += e_kv
        k += 1
        print(f'{k}-я итерация:')
        print(f'Значение аппроксимирующей функции: {func_arr[i]}')
        print(f'Отклонение: {e_arr[i]}')
        print(f'Оценка относительной погрешности аппроксимации: {p_arr[i]}')
    sko = math.sqrt(S/n)
    return apprx_func, func_arr, e_arr, p_arr, S, sko


def log_approx(func):
    print('---Логарифмическая аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    for i in x_args:
        if i <= 0:
            raise RuntimeError('Значение функции не удовлетворяет ОДЗ логарифма')

    lnx_args = [math.log(i) for i in x_args]
    s_x = sum(x_args)
    s_y = sum(y_args)

    xx_args = [i * i for i in lnx_args]
    s_xx = sum(xx_args)

    xy_args = [lnx_args[i] * y_args[i] for i in range(n)]
    s_xy = sum(xy_args)

    delta = s_xx * n - s_x * s_x
    delta1 = s_xy * n - s_x * s_y
    delta2 = s_xx * s_y - s_x * s_xy

    a = delta1 / delta
    b = delta2 / delta

    print('Коэффициент a:', a)
    print('Коэффициент b:', b)
    apprx_func = lambda x: a * math.log(x) + b

    # Мера отклонения
    S = 0

    k = 0
    func_arr = [0] * n
    e_arr = [0] * n
    p_arr = [0.0] * n
    for i in range(n):
        # МНК
        func_arr[i] = apprx_func(x_args[i])
        e_arr[i] = func_arr[i] - y_args[i]
        p_arr[i] = e_arr[i] / func_arr[i]
        e_kv = e_arr[i] * e_arr[i]
        S += e_kv
        k += 1
        print(f'{k}-я итерация:')
        print(f'Значение аппроксимирующей функции: {func_arr[i]}')
        print(f'Отклонение: {e_arr[i]}')
        print(f'Оценка относительной погрешности аппроксимации: {p_arr[i]}')
    sko = math.sqrt(S/n)
    return func_arr, e_arr, p_arr, S, sko


def pow_approx(func):
    print('---Степенная аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    for i in x_args:
        if i <= 0:
            raise RuntimeError('Значение x не удовлетворяет ОДЗ логарифма')

    for i in y_args:
        if i <= 0:
            raise RuntimeError('Значение y не удовлетворяет ОДЗ логарифма')

    lnx_args = [math.log(i) for i in x_args]
    lny_args = [math.log(i) for i in y_args]
    s_x = sum(lnx_args)
    s_y = sum(lny_args)

    xx_args = [i * i for i in lnx_args]
    s_xx = sum(xx_args)

    xy_args = [lnx_args[i] * lny_args[i] for i in range(n)]
    s_xy = sum(xy_args)

    delta = s_xx * n - s_x * s_x
    delta1 = s_xy * n - s_x * s_y
    delta2 = s_xx * s_y - s_x * s_xy

    a = delta1 / delta
    b = delta2 / delta

    print('Коэффициент a:', a)
    print('Коэффициент b:', b)
    apprx_func = lambda x: a * math.log(x) + math.log(b)

    # Мера отклонения
    S = 0

    k = 0
    func_arr = [0.0] * n
    e_arr = [0] * n
    p_arr = [0.0] * n
    for i in range(n):
        # МНК
        func_arr[i] = apprx_func(x_args[i])
        e_arr[i] = func_arr[i] - y_args[i]
        p_arr[i] = e_arr[i] / func_arr[i]
        e_kv = e_arr[i] * e_arr[i]
        S += e_kv
        k += 1
        print(f'{k}-я итерация:')
        print(f'Значение аппроксимирующей функции: {func_arr[i]}')
        print(f'Отклонение: {e_arr[i]}')
        print(f'Оценка относительной погрешности аппроксимации: {p_arr[i]}')
    sko = math.sqrt(S/n)
    return apprx_func, func_arr, e_arr, p_arr, S, sko

