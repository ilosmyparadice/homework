list1 = [
    [1,2,3],
    [1,2,3]
]
list2 = [
    [5123,2,3],
    [1,2,-1336]
]
list3 = [
    [1,2,3],
    [1,2,3]
]

class Matrix:
    def __init__(self, m):
        self.__m = m
        self.__width = len(m[0])
        self.__height = len(m)

    def __str__(self):
        text = ''
        max_elem = max([max(map(abs,row)) for row in self.__m])
        max_elem = len(str(max_elem)) + 2

        for row in self.__m:
            text += "|"
            for elem in row:
                text += f"{elem:>{max_elem}}"
            text += "|\n"

        return text

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.__m == other.__m

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Объекты не являются матрицами!")
        if self.__width != other.__width or self.__height != other.__height:
            raise ValueError("Размеры матриц не совпадают!")
        else:
            result = []
            for i in range(self.__height):
                new_row = []
                for j in range(self.__width):
                    new_row.append(self.__m[i][j] + other.__m[i][j])
                result.append(new_row)

        return Matrix(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Объекты не являются матрицами!")
        if self.__width != other.__width or self.__height != other.__height:
            raise ValueError("Размеры матриц не совпадают!")
        else:
            result = []
            for i in range(self.__height):
                new_row = []
                for j in range(self.__width):
                    new_row.append(self.__m[i][j] - other.__m[i][j])
                result.append(new_row)

        return Matrix(result)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError("Объекты не являются числами!")

        result = []
        for i in range(self.__height):
            new_row = []
            for j in range(self.__width):
                new_row.append(self.__m[i][j] * other)
            result.append(new_row)

        return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def transpose(self) -> 'Matrix':
        new_matrix = []
        for i in range(self.__width):
            new_row = []
            for j in range(self.__height):
                new_row.append(self.__m[j][i])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    @classmethod
    def eye(cls, dim: int) -> 'Matrix':
        pos = 0
        new_matrix = []
        for i in range(dim):
            new_row = [0] * dim
            new_row[pos] = 1
            pos += 1
            new_matrix.append(new_row)

        return cls(new_matrix)

    @classmethod
    def zero(cls, m: int, n: int) -> 'Matrix':
        new_matrix = []
        for i in range(m):
            new_matrix.append([0] * n)
        return cls(new_matrix)

    @classmethod
    def diag(cls, elems: list[int | float]) -> "Matrix":
        new_matrix = []
        for i in range(len(elems)):
            new_row = []
            for j in range(len(elems)):
                if i == j:
                    new_row.append(elems[j])
                else:
                    new_row.append(0)
            new_matrix.append(new_row)
        return cls(new_matrix)

    def getsize(self) -> tuple[int, int]:
        return self.__height, self.__width

    def getcountelements(self) -> int:
        return self.__height * self.__width

    def getsumelements(self) -> int:
        result = 0
        for row in self.__m:
            for elem in row:
                result += elem
        return result

    def eleminatenegative(self):
        new_matrix = []
        for row in self.__m:
            new_row = []
            for elem in row:
                if elem < 0:
                    new_row.append(0)
                else:
                    new_row.append(elem)
            new_matrix.append(new_row)
        return Matrix(new_matrix)



zero = Matrix.zero(2, 4)
print(zero)
diag = Matrix.diag([1, 2, 3])
print(diag)
m = Matrix(list1)
print(m * 3)
m1 = Matrix(list2)
print(m1 + m)
eye = Matrix.eye(4)
print(eye)
m3 = Matrix(list3)
print(m == m3)
print(m == m1)
print(m.getsize())
print(m.getsumelements())
print(m1.eleminatenegative())