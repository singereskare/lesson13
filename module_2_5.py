def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input('Введите кол-во строк матрицы: '))
m = int(input('Введите кол-во столбов матрицы: '))
value = int(input('Задайте значение матрицы: '))
print('-------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print("Ввели неверное кол-во строк:", n)
elif m <= 0:
    print("Ввели неверное кол-во столбцов:", m)
else:
    print("Отлично!")
    for i in matrix:
        print(*i)
