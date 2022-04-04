import copy
import math

MAX_I = 1000


def check_predominance_of_diagonal(matrix):
    is_predominated = False
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(len(matrix[i])):
            if j + 1 == len(matrix[i]):
                break
            if i != j:
                row_sum += abs(matrix[i][j])
        if abs(matrix[i][i]) < row_sum:
            return False
        if abs(matrix[i][i]) > row_sum:
            is_predominated = True
    return is_predominated


def find_max(a):
    maximum = abs(a[0])
    index = 0
    for i in range(len(a)):
        if i + 1 == len(a):
            break
        if abs(a[i]) > maximum:
            maximum = abs(a[i])
            index = i
    return index


# i -- current row number
# max_index -- column number of maximum
def swap_columns(i, max_index, a):
    # k -- current column number
    for k in range(len(a)):
        a[k][max_index], a[k][i] = a[k][i], a[k][max_index]


def get_diagonal_predominance_matrix(a):
    ans_vec = [i for i in range(len(a))]
    for i in range(len(a)):
        max_index = find_max(a[i])
        if max_index != i and abs(a[i][max_index]) != abs(a[i][i]):
            swap_columns(i, max_index, a)
            ans_order[i], ans_order[max_index] = ans_order[max_index], ans_order[i]
        if check_predominance_of_diagonal(a):
            break
    if not check_predominance_of_diagonal(a):
        print('Не удалось выполнить условие диагонального преобладания в матрице')
    for i in range(len(a)):
        if a[i][i] == 0:
            print('На главной диагонали есть 0.')
            exit(0)
    return a, ans_vec


def print_matrix(matrix):
    print('Матрица:')
    for row in matrix:
        print(*row)


def split_array(a):
    vector = [[]]
    mk = []
    for i in range(len(a)):
        vector[0].append(a[i][-1])
        mk.append(copy.copy(a[i]))
        mk[i].pop(-1)
    return vector, mk


def get_sum(mk, x_prev, i):
    sum = 0
    for j in range(len(mk)):
        if i != j:
            sum += mk[i][j] * x_prev[j]
    return sum


# x_vec == [x1, x2, x3] x_prev -- prev x_vec
def get_max_dif(x_vec, x_prev, n):
    max_dif = 0.0
    for j in range(n):
        if abs(x_prev[j] - x_vec[j]) > max_dif:
            max_dif = abs(x_prev[j] - x_vec[j])
    return max_dif


# метод прямых итераций

# mk -- koeff matrix
# mf -- freedom members matrix
# e -- accuracy
# zero approximation is given by zeros and is not considered (skip 1st iteration)
def execute_iterations(mk, mf, e, ans_order):
    n = len(mk)
    max_dif = math.inf
    # list of all iterations
    iter_list = []
    x_vec = [0] * n
    err_vec = [0]*n
    iter_list.append([0] * n)
    b = mf[0]
    k = 0
    while max_dif > e:
        k += 1
        x_prev = iter_list[-1]
        for i in range(n):
            x_vec[i] = (1/float(mk[i][i]))*(b[i] - get_sum(mk, x_prev, i))
            err_vec[i] = abs(x_prev[ans_order[i]] - x_vec[ans_order[i]])
        iter_list.append(copy.copy(x_vec))
        # print(iter_list)
        if k != 1:
            max_dif = get_max_dif(x_vec, x_prev, n)
            if max_dif is None or max_dif == math.inf:
                raise (RuntimeError('Итерации не сходятся!'))
        if k > MAX_I:
            raise (RuntimeError('Не удалось получить ответ за максимальное число итераций'))
    return iter_list, k - 1, err_vec


def read_from_console():
    while True:
        try:
            n = int(input('Введите порядок матрицы:'))
            if n <= 0 or n > 20:
                print('Порядок матрицы -- положительное число не более 20')
            else:
                break
        except ValueError:
            print('Ошибка: порядок матрицы должен быть целым числом')

    k = 0
    matrix = []
    print('Введите матрицу:')
    while k != n:
        row = list(map(float, input().split()))
        if k == 0:
            matrix = [row]
        else:
            matrix.append(row)
        k += 1

    while True:
        try:
            eps = float(input('Введите точность: '))
            if eps <= 0:
                print('Точность матрицы -- положительное число!')
            else:
                break
        except ValueError:
            print('Точность матрицы -- число!')
    return n, matrix, eps


def read_file():
    with open("in.txt", 'rt') as file:
        try:
            n = int(file.readline())
            e = float(file.readline())
            matrix = []
            for line in file:
                row = list(map(float, line.strip().split()))
                if len(row) != n+1:
                    raise ValueError
                matrix.append(row)
            if len(matrix) != n:
                raise ValueError
        except ValueError:
            return None
    return n, matrix, e


def check_answer(a, x_answ):
    for i in range(len(a)):
        sum = 0
        for j in range(len(a[i])):
            sum += a[i][j]*x_answ[j]
        print('each answer: ', sum)


if __name__ == '__main__':
    ans = input('Нажмите Enter, если хотите вводить значения с консоли.'
                ' Если хотите читать значения из файла in.txt введите любой символ:\n')
    if ans == '':
        p, new_arr, acc = read_from_console()
    else:
        p, new_arr, acc = read_file()
    ans_order = [i for i in range(p)]
    if not check_predominance_of_diagonal(new_arr):
        print('В матрице нарушено диагональное преобладание')
        new_arr, ans_order = get_diagonal_predominance_matrix(new_arr)
    # vec == [[x_i, x_i+1,..., x_n]]
    print_matrix( new_arr )
    vec, k_matrix = split_array( new_arr )
    try:
        res_list, iterations, errors = execute_iterations(k_matrix, vec, acc, ans_order)
        print('Количество итераций: ', iterations)
        print('Вектор неизвестных:', *res_list[-1])
        print('Вектор погрешностей: ', *errors)
    except RuntimeError as r:
        print(r)
