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
    with open("file1.txt", 'rt') as file:
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
