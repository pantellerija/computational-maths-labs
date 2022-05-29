def trapezoid_sum(func, a, b, n):
    h = 1.0 * (b - a) / n
    sum = 0.5 * (func(a) * func(b))
    for i in range(n):
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
    return sum, n / 2


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
    return sum, n/2


# additional

def double_trapezoid(func, a, b, n):
    h = (b-a)/2
    x = a + h/2
    sum = 0
    for i in range(n):
        sum += func(x + i*h)
    return sum*h/2


def simpson_method_with_trap(func, a, b, n, eps):
    k = 4
    tr_prev_sum = trapezoid_sum(func, a, b, n)
    tr_sum = double_trapezoid(func, a, b, n)
    ans = (4*tr_sum-tr_prev_sum)/3
    M = max(1, abs(ans))
    while M > eps:
        prev_ans = ans
        tr_prev_sum = tr_sum
        tr_sum = double_trapezoid(func, a, b, n)
        ans = (4 * tr_sum - tr_prev_sum) / 3
        M = abs(ans - prev_ans)/(2**k-1)
    return ans, n




