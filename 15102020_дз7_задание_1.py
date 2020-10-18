
class Matrix:
    def __init__(self, matrix):
        self.m = matrix
    def __str__(self):
        return '\n'.join([''.join(['%s\t' % el for el in row]) for row in self.m])

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.m)):
            for j in range(len(self.m[0])):
                summa = other.m[i][j] + self.m[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.m):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


#вывод матрицы
task1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(task1)

#сумма двух матриц
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[11,12,13],[14,15,16],[17,18,19]])
print(m1+m2)


