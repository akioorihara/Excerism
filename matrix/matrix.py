class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        pass

    def column(self, index):
        pass


matrix_string = [9, 8, 7, 5, 3, 2, 6, 6, 7]

for n in range(1):
    print("  |----")
    for i in range(len(matrix_string)):
        # print(i)  # printing the list using loop
        if i == 0 or i == 3 or i == 6:
            print(n, "|", end="")
        print(matrix_string[i], end="")
        if i == 2 or i == 5 or i == 8:
            print(" ")
