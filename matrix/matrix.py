class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split('\n')

    def row(self, index):
        return list(int(x) for x in self.matrix_string[index-1].split())

    def column(self, index):
        return list(int(x.split()[index-1]) for x in self.matrix_string)

    # def __init__(self, matrix_string):
    #     self.matrix_string = matrix_string

    # def row(self, index=0):
    #     for i in range(9):
    #         print(matrix_string[i], end="")
    #         if i == 2 or i == 5 or i == 8:
    #             print(" ")

    # def column(self, index=0):
    #     pass
matrix_string = [9, 8, 7, 5, 3, 2, 6, 6, 7]
x = Matrix
# x.row(matrix_string)
x.column(matrix_string)
