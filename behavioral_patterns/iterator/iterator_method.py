class MatrixRowIterator:
    def __init__(self, matrix: list):
        self._matrix = matrix
        self._row = 0
        self._col = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._row >= len(self._matrix):
            raise StopIteration

        value = self._matrix[self._row][self._col]

        self._col += 1
        if self._col >= len(self._matrix[self._row]):
            self._col = 0
            self._row += 1

        return value

class MatrixColIterator:
    def __init__(self, matrix: list):
        self._matrix = matrix
        self._row = 0
        self._col = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._col >= len(self._matrix):
            raise StopIteration

        value = self._matrix[self._row][self._col]

        self._row += 1
        if self._row >= len(self._matrix):
            self._row = 0
            self._col += 1

        return value




class Matrix:
    def __init__(self, data):
        self._data = data

    def in_row(self):
        return MatrixRowIterator(self._data)

    def in_col(self):
        return MatrixColIterator(self._data)



if __name__ == "__main__":
    matrix_data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

matrix = Matrix(matrix_data)

print("Построковий перебір:")
for x in matrix.in_row():
    print(x)

print("*" * 25)

print("Поколонний перебір:")
for x in matrix.in_col():
    print(x)
