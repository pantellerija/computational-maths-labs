def trapezoid_sum(func, a, b, n):
    h = 1.0 * (b - a) / n
    sum = 0.5 * (func(a) + func(b))
    for i in range(1,n-1):
        sum += func(a + i * h)
    return sum * h


def trapezoidal_method(func, a, b, n, eps):
    print('---Метод трапеций---')
    k = 2
    h = 1.0 * (b - a) / n
    sum = trapezoid_sum(func, a, b, n) * h
    M = max(1, abs(sum))
    while M > eps:
        prev_sum = sum
        sum = trapezoid_sum(func, a, b, n)
        n *= 2
        M = abs(sum - prev_sum) / (2 ** k - 1)
    return sum, n / 2, M


def simpson_sum(func, a, b, n):
    h = 1.0 * (b - a) / n
    if n % 2 == 1:
        n += 1
    sum = (func(a) + 4 * func(a + h) + func(b))
    for i in range(1, round(n/2)):
        sum += 2 * func(a + (2 * i) * h) + 4 * func(a + (2 * i + 1) * h)
    return sum * h / 3


def simpson_method(func, a, b, n, eps):
    print('---Метод Симпсона---')
    k = 4
    h = 1.0 * (b - a) / n
    sum = (func(a) + 4 * func(a + h) + func(b))
    M = max(1, abs(sum))
    while M > eps:
        prev_sum = sum
        sum = simpson_sum(func, a, b, n)
        n *= 2
        M = abs(sum - prev_sum) / (2 ** k - 1)
    return sum, n/2, M


def calculate_improper_int(func,method, a, b, bp,n,eps):
    if bp == a:
        return method(func,a+eps,b,n,eps)[0]
    elif bp == b:
        return method(func,a,b-eps,n,eps)[0]
    else:
        return method(func, a, bp+eps, n, eps)[0] + method(func, a, bp-eps, n, eps)[0]



