import matrix  # Используем модуль matrix, который сам написал

a1 = matrix.Matrix(2, 4)
print('Матрица а1')
print(a1)
a2 = matrix.Matrix(2, 3)
a2.data = [[7, 8, 9], [10, 11, 12]]
print('Матрица а2')
print(a2)
print('Сложение матрицы!')
print(a1 + a2.data)
print('Вычитание матрицы!')
print(a1 - a2.data)
c = matrix.Matrix(3, 2)
print('Умножение матрицы!')
print(a1 * c.data)
print('Транспортированная матрица')
print(a1.transpose())
