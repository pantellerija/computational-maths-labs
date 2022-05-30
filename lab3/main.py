import math

from lab3 import methods
import io_lib

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
    fnum, a, b, mnum = io_lib.get_console_inputs()
    eps = 0.001
    n = 4
    ans, num, err = meth_list[mnum](func_list[fnum], a, b, n, eps)
    print(f'Значение интеграла: %.4f' % ans)
    print(f'Число разбиений: %.d' % num)
    print(f'Погрешность: %.10f' % err)

