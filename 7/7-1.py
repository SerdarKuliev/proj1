class Matrix:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def __add__(self):
        mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.l1)):

            for j in range(len(self.l2[i])):
                mat[i][j] = self.l1[i][j] + self.l2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))



mymat = Matrix([[7, 13, 3], [6, 5, 12], [31, 5, 9]], [[33, 17, 17], [4, 5, 8], [9, 25, 11]])

print(mymat.__add__())



