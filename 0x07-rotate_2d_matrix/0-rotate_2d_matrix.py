#!/usr/bin/python3
'''The module contains the definition of "rotate_2d_matrix" the function that
rotates a square matrix 90-degrees clockwise, in-place'''


def rotate_2d_matrix(matrix):
    '''The function rotates a square matrix "matrix" 90-degrees clockwise,
    in-place'''
    n = len(matrix)
    if n > 0:
        assert len(matrix[0]) == n

    for i in range(n):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        matrix[i].reverse()
