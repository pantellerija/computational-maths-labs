import math

from lab3 import methods

func_list = [
    lambda x: x ** 2,
    lambda x: x ** 3,
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
    n = 0
    ans, num = methods.trapezoidal_method(func_list[2], a, b, eps)
    print(f'Значение интеграла: %.3f' % ans)
    print(f'Число разбиений: %3.f' % num)
