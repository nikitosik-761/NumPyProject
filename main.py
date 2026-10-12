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
array4 = np.array([1, 2, 5, 10, 2, 43, 53, 100, 23, 43])
array4[np.argmax(array4)] = 0
print(array4)

print("11. Найти ближайшее к заданному значению число в заданном массиве")
array5 = np.array([1, 2, 3, 5, 6, 7])
value = 3.6
nearest_val_index = np.abs(array5 - value).argmin()
print(array5[nearest_val_index])

print("12. Дан четырехмерный массив, посчитать сумму по последним двум осям")
array6 = np.array([
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ],

    [
        [
            [9, 10],
            [11, 12]
        ],
        [
            [13, 14],
            [15, 16]
        ]
    ]
])
print(np.sum(array6, axis=(2, 3)))

print("13. Определить, есть ли в двумерном массиве нулевые столбцы")
array7 = np.array([
    [1, 2, 0],
    [0, 5, 0],
    [7, 8, 0]
])
print(np.all(array7 == 0, axis=0))

print("14. Отнять среднее из каждой строки в матрице")
array8 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
row_means = array8.mean(axis=1, keepdims=True)  # иначе сделает [2. 5. 8.]
print(row_means)
result = array8 - row_means  # тут бродкастинг будет работать
print(result)

print("15. Создайте вектор с элементами от 10 до 50")
vector3 = np.arange(10, 51)
print(vector3)

print("16. Создайте матрицу (5, 5), заполненую от 0 до 6")
matrix1 = random.integers(0, 7, size=(5, 5))
print(matrix1)

print("17. Умножьте матрицу размерности (5, 3) на (3, 2)")
matrixA = random.integers(low=1, high=11, size=(5, 3))
matrixB = random.integers(low=1, high=11, size=(3, 2))
print(matrixA)
print(matrixB)
print(f"Result: {matrixA @ matrixB}")

print("18. Создайте матрицу (10, 10) так, чтобы на границе были 0, а внтури 1")
matrix2 = np.ones((10, 10))
matrix2[0, :] = 0
matrix2[-1, :] = 0
matrix2[:, 0] = 0
matrix2[:, -1] = 0
print(matrix2)

print("19. Для заданного числа найдите ближайший к нему элемент в векторе")
array9 = np.array([3, 17, 42, 88])
target = 50
index = np.abs(array9 - target).argmin()
print(array9[index])

print("""
20. Дан трёхмерный массив "Цветное изображение", содержащий изображение, размера (height, width, numChannels),
    а также вектор коэффициентов длины numChannels.
    Сложить каналы изображения с указанными весами, и вернуть результат в виде матрицы размера (height, width).
    Реальное изображение не считываем, заполняем трехмерный массив случайными значениями. 
    Преобразуйте цветное изображение в оттенки серого, использовав коэффициенты np.array([0.299, 0.587, 0.114]).
   """)
height = 100
width = 120
numChannels = 3

image = random.integers(0, 256, size=(height, width, numChannels))
gray_cof = np.array([0.299, 0.587, 0.114])
gray = image @ gray_cof
print(gray.shape)