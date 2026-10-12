import numpy as np

print("1. Найти индексы ненулевых элементов в заданном массиве")
array1 = np.array([
    [1, 2, 0],
    [0, 5, 6],
    [7, 8, 0]
])
# print(np.where(array1 != 0))
print(np.nonzero(array1))

print("2. Создать nxn единичную матрицу.")
n = 3
# print(np.eye(n))
print(np.identity(3))

print("3. Создать массив nxnxn со случайными значениями")
random = np.random.default_rng()
array2 = random.integers(low=1, high=5, size=(n, n, n))
print(array2)

print("4. Создать вектор (одномерный массив) размера n, заполненный нулями")
vector_size = 5
vector = np.zeros(vector_size)
print(vector)

print("5. Создать вектор размера 1n, заполненный нулями, но пятый элемент равен 1")
vector1 = np.zeros(vector_size)
vector1[4] = 1
print(vector1)

print("6. Создать вектор со значениями от n до m")
vector2 = np.arange(0, 5)  # exclusive
print(vector2)

print("7. Развернуть одномерный массив (первый становится последним)")
array3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array3[::-1])

print("8. Создать матрицу с 0 внутри, и 1 на границах")
matrix = np.zeros((5, 5))
matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1
print(matrix)

print("9. Создать nxn матрицу и заполнить её в шахматном порядке")
chess_matrix = np.zeros((5, 5))
chess_matrix[::2, ::2] = 1
chess_matrix[1::2, 1::2] = 1
print(chess_matrix)

print("10. Заменить максимальный элемент на ноль")
array4 = np.array([1,2,5,10,2,43,53,100,23,43])
array4[np.argmax(array4)] = 0
print(array4)