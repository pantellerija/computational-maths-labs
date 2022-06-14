import math
import numpy as np

from lab4.slau import solve_sys, make_diagonal


def mnk(approx, x, y):
    n = len(x)
    func_arr = [0] * n
    e_arr = [0] * n
    p_arr = [0.0] * n
    k = 0
    S = 0  # мера отклонения

    for i in range(n):
        func_arr[i] = approx(x[i])
        e_arr[i] = func_arr[i] - y[i]
        p_arr[i] = e_arr[i] / func_arr[i]
        e_kv = e_arr[i] * e_arr[i]
        S += e_kv
        k += 1
        print()
        print(f'{k}-я итерация:')
        print(f'Значение аппроксимирующей функции: {round(func_arr[i], 3)}')
        print(f'Отклонение: {round(e_arr[i], 3)}')
        print(f'Мера отклонения: {round(S, 3)}')
        print(f'Оценка относительной погрешности аппроксимации: {round(p_arr[i], 3)}')
    return func_arr, e_arr, p_arr, S


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

    apprx_func = lambda x: a * x + b
    print(f'Аппроксимирующая функция: {round(a, 3)}*x + {round(b, 3)}')

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
    sko = math.sqrt(S / n)

    # Коэффициент корреляции Пирсона:
    r = num_pirs / math.sqrt(xq_sum * yq_sum)
    print(f'Коэффийиент корреляции Пирсона: {round(r, 3)}')
    print()
    print()
    return apprx_func, func_arr, e_arr, p_arr, sko


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
    new_matrix = make_diagonal(solve_sys(np.copy(matrix)))

    ans = new_matrix[:, -1]
    a0, a1, a2 = ans[0], ans[1], ans[2]

    approx = lambda x: a0 + a1 * x + a2 * x * x
    print(f'Аппроксимирующая функция: {round(a0, 3)} + {round(a1, 3)}*x + {round(a2, 3)}*x^2')
    func_arr, e_arr, p_arr, S = mnk(approx, x_args, y_args)
    sko = math.sqrt(S / n)
    print()
    print()
    return approx, func_arr, e_arr, p_arr, sko


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

    x3y_args = [x_3args[i] * y_args[i] for i in range(n)]
    s_3xy = sum(x3y_args)

    matrix = np.array([[n, s_x, s_xx, s_3x, s_y],
                       [s_x, s_xx, s_3x, s_4x, s_xy],
                       [s_xx, s_3x, s_4x, s_5x, s_xxy],
                       [s_3x, s_4x, s_5x, s_6x, s_3xy]])
    m2 = make_diagonal(solve_sys(np.copy(matrix)))
    ans = m2[:, -1]
    a0, a1, a2, a3 = ans[0], ans[1], ans[2], ans[3]

    approx = lambda x: a0 + a1 * x + a2 * x * x + a3 * x * x * x
    print(f'Аппроксимирующая функция: {round(a0, 3)} + {round(a1, 3)}*x + {round(a2, 3)}*x^2 + {round(a3, 3)}*x^3')
    func_arr, e_arr, p_arr, S = mnk(approx, x_args, y_args)
    sko = math.sqrt(S / n)
    print()
    print()
    return approx, func_arr, e_arr, p_arr, sko


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

    approx = lambda x: a * x + math.log(b)
    print(f'Аппроксимирующая функция: {round(a, 3)}*x + ln({round(b, 3)})')
    func_arr, e_arr, p_arr, S = mnk(approx, x_args, y_args)
    sko = math.sqrt(S / n)
    print()
    print()
    return approx, func_arr, e_arr, p_arr, sko


def check_tolerance_range(args):
    for i in args:
        if i <= 0:
            raise RuntimeError('Значение x не удовлетворяет ОДЗ логарифма')


def log_approx(func):
    print('---Логарифмическая аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    check_tolerance_range(x_args)
    lnx_args = [math.log(i) for i in x_args]
    s_x = sum(lnx_args)
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
    approx = lambda x: a * math.log(x) + b
    print(f'Аппроксимирующая функция: {round(a, 3)}*ln(x) + {round(b, 3)}')
    func_arr, e_arr, p_arr, S = mnk(approx, x_args, y_args)
    sko = math.sqrt(S / n)
    print()
    print()
    return approx, func_arr, e_arr, p_arr, sko


def pow_approx(func):
    print('---Степенная аппроксимация---')
    x_args = func[0]
    y_args = func[1]
    n = len(x_args)

    check_tolerance_range(x_args)
    check_tolerance_range(y_args)

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

    approx = lambda x: a * math.log(x) + math.log(b)
    print(f'Аппроксимирующая функция: {round(a, 3)}*ln(x) + ln({round(b, 3)})')
    func_arr, e_arr, p_arr, S = mnk(approx, x_args, y_args)
    sko = math.sqrt(S / n)
    print()
    print()
    return approx, func_arr, e_arr, p_arr, sko
