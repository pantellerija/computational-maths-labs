
eps = 0.00001


def make_diagonal(matrix):
    for i in range(len(matrix) - 1, 0, -1):
        row = matrix[i]
        for upper_row in matrix[:i]:
            fac_row = upper_row[i]
            upper_row[-1] -= fac_row * row[-1]
            upper_row[i] = 0
    return matrix


def solve_sys(matrix):
    for i, row in enumerate(matrix):
        divider = row[i]
        row /= divider
        for lower_row in matrix[i + 1:]:
            k = lower_row[i]
            lower_row -= k * row
    return matrix
