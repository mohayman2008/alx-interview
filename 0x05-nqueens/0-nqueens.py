#!/usr/bin/python3
'''The script solves the N queens puzzle which is the challenge
of placingN non-attacking queens on an N×N chessboard.

The program prints every possible solution to the problem, one solution per
line

Usage: 0-nqueens N
N: integer greater or equal to 4
'''
import sys


def is_valid_Q(board, n, x, y):
    '''The function checks if the position of a queen is valid position'''
    assert x < n
    assert y < n

    diff = y - x
    _sum = x + y
    for i in range(x):
        d1_y = i + diff
        if 0 <= d1_y and board[i][d1_y]:
            return False

        d2_y = _sum - i
        if d2_y < n and board[i][d2_y]:
            return False

        if board[i][y]:
            return False
    return True


def get_q_cordinates(board, n, char="Q"):
    '''Returns a list of the queens on "board" of size n*n, where "char" is
    the character used to represent the queen'''
    res = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == char:
                res.append([i, j])
    return res


def nqueens(n, board=None, x=0, solutions=[]):
    '''The function recursevely solves the N queens puzzle using backtracking
    '''
    if not board:
        board = [["" for j in range(n)] for i in range(n)]

    if x >= n:
        solutions.append(get_q_cordinates(board, n))
        return

    for y in range(n):
        if is_valid_Q(board, n, x, y):
            board[x][y] = "Q"
            nqueens(n, board, x + 1, solutions)
            board[x][y] = ""
    return solutions


def main():
    '''main: entry point'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    n = sys.argv[1]
    if not n.isdecimal():
        print("N must be a number")
        exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for row in nqueens(n):
        print(row)


if __name__ == "__main__":
    main()
