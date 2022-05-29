import math

from lab3 import methods

func_list = [
    # 2.33 от 1 до 2
    lambda x: x ** 2,
    # 0.786 от 0 до 1
    lambda x: 1 / (1 + x ** 2),
    # 4.250 от 0 до 1.5
    lambda x: 2 * x + 1 / math.sqrt(x + 1 / 16)
]

meth_list = [
    methods.trapezoidal_method,
    methods.simpson_method
]

if __name__ == '__main__':
    a = 0
    b = 1.5
    eps = 0.0001
    n = 10
    ans, num = methods.simpson_method(func_list[2], a, b, n, eps)
    print(f'Значение интеграла: %.4f' % ans)
    print(f'Число разбиений: %.d' % num)
