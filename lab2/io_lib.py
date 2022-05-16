

def get_data_source():
    while True:
        try:
            data_source_choice = int(input('Введите\n'
                        '0 -- читать границы интервалов с консоли\n'
                        '1 -- читать границы интервалов из файла\n'))
            if data_source_choice < 0 or data_source_choice >= 2:
                print('Ошибка. Введите 0 или 1')
            else:
                break
        except ValueError:
            print('Ошибка. Введите число')
    return data_source_choice


def read_file():
    with open("data.txt", 'rt') as file:
        l = float(file.readline())
        r = float(file.readline())
    return l, r


def write_file(*results):
    with open('res.txt', 'w') as f:
        for res in results:
            f.write(res)
            f.write('\n')


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


def get_choice():
    while True:
        try:
            work_choice = int(input('Введите\n'
                            '0 -- найти корень нелинейной функции из предложенных\n'
                            '1 -- найти корень предложенной нелинейной системы\n'))
            if work_choice < 0 or work_choice >= 2:
                print('Ошибка. Нумерация от 0 до 1')
            else:
                break
        except ValueError:
            print('Ошибка. Введите целое число')
    return work_choice


def get_out_choice():
    while True:
        try:
            output_choice = int(input('Введите\n'
                            '0 -- вывести результаты на экран\n'
                            '1 -- вывести результаты в файл\n'))
            if output_choice < 0 or output_choice >= 2:
                print('Ошибка. Можно выбрать 0 или 1')
            else:
                break
        except ValueError:
            print('Ошибка. Введите целое число')
    return output_choice


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


# примерно 0.2, 0.6
str_flist = [
        'x^5-x-0.2',
        'x^3-x+4',
        'x-sin(x)-0.25'
    ]


def get_console_inputs_for_eq():
    str_mlist = [
        'метод секущих',
        'метод простой итерации'
    ]
    for i in range(len(str_flist)):
        print(f'{i}-я функция: {str_flist[i]}')

    fnum = get_func_num()
    print(f'Вы выбрали функцию {str_flist[fnum]}')

    print('Выберите метод решенения:')
    for i in range(len(str_mlist)):
        print(f'{i}-й метод решения: {str_mlist[i]}')

    meth_num = get_meth_num()
    print(f'Вы выбрали {str_mlist[meth_num]}')

    if get_data_source() == 0:
        l, r = get_console_intervals()
    else:
        l, r = read_file()

    outp_num = get_out_choice()

    return fnum, l, r, meth_num, outp_num
