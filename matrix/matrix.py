class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index=0):
        for n in range(1):
            for i in range(len(matrix_string)):
                print(matrix_string[i], end="")
                if i == 2 or i == 5 or i == 8:
                    print(" ")

    def column(self, index):
        for n in range(len(mattrix_string)):


matrix_string = [9, 8, 7, 5, 3, 2, 6, 6, 7]

# for n in range(1):
#     for i in range(len(matrix_string)):
#         print(matrix_string[i], end="")
#         if i == 2 or i == 5 or i == 8:
#             print(" ")

x = Matrix
x.row(0)