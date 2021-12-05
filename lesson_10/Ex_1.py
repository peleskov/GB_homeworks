class Matrix:
    def __init__(self, in_matrix):
        self.matrix = in_matrix

    def __str__(self):
        width_col = [0 for _ in range(0, len(self.matrix[0]))]
        for x in self.matrix:
            for i, y in enumerate(x):
                width_col[i] = len(str(y)) if len(str(y)) > width_col[i] and i < len(width_col) - 1 else width_col[i]
        return '\n'.join([' | '.join(['{:<{width}}'.format(y, width=width_col[i])
                                      for i, y in enumerate(x)]) for x in self.matrix])

    def __add__(self, other):
        if sum([1 for _ in self.matrix]) != sum([1 for _ in other.matrix]) \
                or sum([1 for x in self.matrix for _ in x]) != sum([1 for x in other.matrix for _ in x]):
            print(f'{self}\n', f'+\n', other, 'Эти матрицы сложить не возможно!', sep='\n')
        else:
            return Matrix([[x+y for x, y in zip(rows1, rows2)] for rows1, rows2 in zip(self.matrix, other.matrix)])


matrix1 = Matrix([[31000, 202, 123], [37, 4354, 501], [1, 8655, 7]])
matrix2 = Matrix([[3, 25, 123], [11, 888, 464], [74, 552, 1]])
matrix3 = Matrix([[37264, 25, 123, 52], [11, 888, 464, 12]])
matrix_sum = matrix1 + matrix2 + matrix1
print(matrix1, matrix2, matrix3, matrix_sum, sep='\n\n')
