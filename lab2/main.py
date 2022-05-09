import math
import methods as meth


def get_console_inputs():
    print('hi girls')
    str_flist = [
        'x^5-x-0.2',
        'sin(x)-x*cos(x)',
        'x-sin(x)-0.25'
    ]
    str_mlist = [
        'Метод секущих',
        'Метод простой итерации'
    ]
    work_choice = int(input('Введите\n'
                            '0 -- найти корень нелинейной функции из предложенных\n'
                            '1 -- найти корень предложенной нелинейной системы\n'))
    if work_choice:
        print('Простите это ещё не реализовано')
        exit(0)
    else:
        for i in range(len(str_flist)):
            print(f'{i}-я функция: {str_flist[i]}')
        fnum = int(input('Введите номер выбранной функции: '))
        print(f'Вы выбрали функцию {str_flist[fnum]}')

        print('Выберите метод решенения:')
        for i in range(len(str_mlist)):
            print(f'{i}-й метод решения: {str_mlist[i]}')
        method_num = int(input('Введите номер выбранного метода решения: '))

        l = float(input('Введите левую границу интервала: '))
        r = float(input('Введите правую границу интервала: '))
        return fnum, l, r, method_num


if __name__ == '__main__':
    # 1.045 1m(0.0005) 4.494 1m(0.0001)--[pi;3pi/2] 1.172 2m(0.0025)
    flist = [
        lambda x: x**5 - x - 0.2,
        lambda x: math.sin(x)-x*math.cos(x),
        lambda x: x - math.sin(x) - 0.25
    ]
    mlist = [
        meth.secant_method,
        meth.iteration_method
    ]
    f_ind, a, b, m_id = get_console_inputs()
    y = flist[f_ind]
    # a = 0
    # b = 10
    eps = 0.0005
    if meth.is_root_exist(y, a, b):
        ans, iter_num = mlist[m_id](y, a, b, eps)
        print(f'Найденный корень уравнения = %.3f с точностью ε = {eps}' % ans)
        print(f'Значение функции при x = %.3f: %.d' % (ans, y(ans)))
        print(f'Число итераций: {iter_num}')
    else:
        print(f'У уравнения на отрезке [{a};{b}] нет корней. Поменяйте границы отрезка')