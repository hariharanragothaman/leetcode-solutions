def spiral_matrix(matrix):
    return matrix and [*matrix.pop(0)] + spiral_matrix(*(zip(*matrix)[::-1]))