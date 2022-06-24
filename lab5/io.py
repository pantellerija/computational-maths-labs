def get_data_source():
    while True:
        try:
            data_source_choice = int(input('Введите\n'
                                           '0 -- читать значения с консоли\n'
                                           '1 -- читать значения из файла\n'))
            if data_source_choice < 0 or data_source_choice >= 2:
                print('Ошибка. Введите 0 или 1')
            else:
                break
        except ValueError:
            print('Ошибка. Введите число')
    return data_source_choice


def read_from_console():
    while True:
        try:
            n = int(input('Введите количество значений функции: '))
            if n <= 0:
                print('Количество значений функции -- положительное число')
            else:
                break
        except ValueError:
            print('Ошибка: количество значений функции должно быть целым числом')

    k = 0
    matrix = []
    print('Введите точки (1 строка -- значения функции, 2 строка -- значения аргумента):')
    while k != 2:
        row = list(map(float, input().split()))
        if k == 0:
            matrix = [row]
        else:
            matrix.append(row)
        k += 1

    return n, matrix


def read_from_file():
    with open("file2.txt", 'rt') as file:
        n = int(file.readline())
        matrix = []
        for line in file:
            row = list(map(float, line.strip().split()))
            if len(row) != n:
                raise ValueError(f'Точек должно быть {n}')
            matrix.append(row)
        if len(matrix) != 2:
            raise ValueError(f'Функция двумерная: вводятся только значения x и y')
    return n, matrix


def get_func_type():
    while True:
        try:
            func_choice = int(input('Выберите тип исходных данных\n'
                                           '0 -- набор данных\n'
                                           '1 -- функция y=ln(x)\n'))
            if func_choice < 0 or func_choice >= 2:
                print('Ошибка. Введите 0 или 1')
            else:
                break
        except ValueError:
            print('Ошибка. Введите число')
    return func_choice


def get_boundaries():
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


def get_points(f):
    x_points = []
    y_points = []
    a, b = get_boundaries()
    x_cur = a
    h = 1.5
    while x_cur <= b:
        x_points.append(x_cur)
        y_points.append(f(x_cur))
        x_cur += h
    return x_points, y_points


def get_arg():
    return int(input('Введите аргумент, значение которого хотите найти: '))
