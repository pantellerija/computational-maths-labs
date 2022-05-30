
fp_list = [
    'x^2',
    '1/(1+x^2)',
    '(2x+1/sqrt(x+1/16))'
]

mp_list = [
    'Метод трапеций',
    'Метод Симпсона'
]


def get_console_intervals():
    while True:
        try:
            l = float(input('Введите левую границу интервала: '))
            r = float(input('Введите правую границу интервала: '))
            if l > r:
                print('Левая граница интервала не должна быть больше правой')
            else:
                break
        except ValueError:
            print('Ошибка. Введите число.')
    return l, r


def get_func_num():
    while True:
        try:
            n = int(input('Введите номер выбранной функции: '))
            if n >= 3 or n < 0:
                print('Ошибка. Нумерация от 0 до 2')
            else:
                break
        except ValueError:
            print('Ошибка. Введите целое положительное число')
    return n


def get_meth_num():
    while True:
        try:
            n = int(input('Введите номер выбранного метода решения: '))
            if n >= 2 or n < 0:
                print('Ошибка. Нумерация от 0 до 1')
            else:
                break
        except ValueError:
            print('Ошибка. Введите целое положительное число')
    return n


def get_console_inputs():
    print('Выберете функцию для интегрированию по номеру:')

    for i in range(len(fp_list)):
        print(f'{i}-я функция: {fp_list[i]}')

    fnum = get_func_num()
    print(f'Вы выбрали функцию {fp_list[fnum]}')

    print('Выберите метод решенения по номеру:')
    for i in range(len(mp_list)):
        print(f'{i}-й метод решения: {mp_list[i]}')

    meth_num = get_meth_num()
    print(f'Вы выбрали {mp_list[meth_num]}')

    l, r = get_console_intervals()

    return fnum, l, r, meth_num
