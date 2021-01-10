# class Matrix:
#     def __init__(self, matrix_string):
#         self.matrix_string = matrix_string.split('\n')

#     def row(self, index):
#         return list(int(x) for x in self.matrix_string[index-1].split())

#     def column(self, index):
#         return list(int(x.split()[index-1]) for x in self.matrix_string)

#     # def __init__(self, matrix_string):
#     #     self.matrix_string = matrix_string

#     # def row(self, index=0):
#     #     for i in range(9):
#     #         print(matrix_string[i], end="")
#     #         if i == 2 or i == 5 or i == 8:
#     #             print(" ")

#     # def column(self, index=0):
#     #     pass
# matrix_string = [9, 8, 7, 5, 3, 2, 6, 6, 7]
# x = Matrix
# # x.row(matrix_string)
# x.column(matrix_string)


class Matrix:
    def __init__(self, matrix_string):

        self.matrix = list(map(lambda e: e.split(' '),matrix_string.split('\n')))

    def row(self, index):
        if len(self.matrix) == 1:
            return list(map(lambda e: int(e),self.matrix[index - 1]))
        else:
            return list(map(lambda e: int(e),self.matrix[index - 1]))

    def column(self, index):
        if len(self.matrix) == 1:
            return list(map(lambda e: int(e),self.matrix[index - 1]))
        else:
            columns = []

            for i in range(len(self.matrix)):
                columns.append(self.matrix[i][index - 1])

            return list(map(lambda e: int(e),columns))

#DEBUG
new_matrix = Matrix('1')

print(
    new_matrix.row(1),
    new_matrix.column(1)
)


items = "1 2 3\n4 5\n6"
sqaured = list(map(lambda x : x.split(), items.split('\n')))
# Below is the same method but using lambda to do this
# squared = []
# for i in items: 
#     squared.append(i**2)

for n in range(len(sqaured)):
    pass
    # print(sqaured[n])

print("This is 0 : ", sqaured[0])
print("This is 1 : ", sqaured[1])
print("This is 2 : ", sqaured[2])