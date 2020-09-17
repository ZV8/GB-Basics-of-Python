class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return ''.join([f'{el[0]}   {el[1]}\n' for el in self.matrix])

    def __add__(self, other):
        sum_matrix = []
        for i, m in enumerate(self.matrix):
            sum_m = []
            for i2 in range(len(m)):
                sum_m.append(self.matrix[i][i2] + other.matrix[i][i2])
            sum_matrix.append(sum_m)
        return Matrix(sum_matrix)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
