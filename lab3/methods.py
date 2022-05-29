def trapezoid_sum(func, a, b, n):
    h = 1.0 * (b - a) / n
    sum = 0.5 * (func(a) * func(b))
    for i in range(n):
        sum += func(a + i * h)
    return sum * h


def trapezoidal_method(func, a, b, eps):
    k = 2
    n = 10
    h = 1.0 * (b - a) / n
    sum = trapezoid_sum(func, a, b, n) * h
    M = max(1, abs(sum))
    while M > eps:
        prev_sum = sum
        sum = trapezoid_sum(func, a, b, n)
        n *= 2
        M = abs(sum - prev_sum) / (2 ** k - 1)
    return sum, n / 2


def simpson_sum(func, a, b, n):
    h = 1.0 * (b - a) / n
    sum = (func(a) + 4 * func(a + h) + func(b))
    for i in range(1, round(n / 2)):
        sum += 2 * func(a + (2 * i) * h) + 4 * func(a + (2 * i + 1) * h)
    return sum * h / 3


def simpson_method(func, a, b, eps=1e-8):
    k = 4
    n = 4
    sum = simpson_sum(func, a, b, n)
    M = max(1, abs(sum))
    while M > eps:
        prev_sum = sum
        sum = simpson_sum(func, a, b, n)
        M = abs(sum - prev_sum) / (2 ** k - 1)
        n *= 2
    return sum, n / 2
