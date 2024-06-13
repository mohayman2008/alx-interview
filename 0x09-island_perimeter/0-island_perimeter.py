#!/usr/bin/python3
'''The module contains the definition of function "island_perimeter"'''


def island_perimeter(grid):
    '''Returns the perimeter of the island described in grid'''
    total = 0

    i = 0
    for row in grid:
        j = 0
        for cell in row:
            if cell == 1:
                total += 4
                if j > 0 and grid[i][j - 1]:
                    total -= 2
                if i > 0 and grid[i - 1][j]:
                    total -= 2
            j += 1
        i += 1
    return total
