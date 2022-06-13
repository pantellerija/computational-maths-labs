import numpy as np

eps = 0.001


def make_diagonal(matrix):
    for nrow in range(len(matrix)-1, 0,-1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            fac = upper_row[nrow]
            upper_row[-1] -= fac*row[-1]
            upper_row[nrow] = 0
    return matrix


def solve_sys(matrix):
    for i in range(len(matrix)):
        # i -- номер строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки i. Поэтому нужно прибавить i к результату
        pivot = i + np.argmax(abs(matrix[i:, i]))
        if pivot != i:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
            # нужно переставлять строки именно так, как написано ниже
            # matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
            matrix[i], matrix[pivot] = matrix[pivot], np.copy(matrix[i])
        row = matrix[i]
        divider = row[i] # диагональный элемент
        if abs(divider) < eps:
            # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
            raise ValueError("Матрица несовместна")
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[i+1:]:
            factor = lower_row[i] # элемент строки в колонке nrow
            lower_row -= factor*row # вычитаем, чтобы получить ноль в колонке nrow
    return matrix
