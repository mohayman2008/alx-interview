#!/usr/bin/python3
'''The module contains the definition of function "makeChange"'''


def makeChange(coins, total):
    '''The function determines the fewest number of coins needed to meet a
    given amount "total", given a pile of "coins" of different values'''
    if len(coins) == 0 or type(total) != int:
        return -1
    if total < 1:
        return 0

    coins.sort(reverse=True)

    minimums = [total + 1 for _ in range(total + 1)]
    minimums[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin == i:
                minimums[i] = 1
            elif coin < i and minimums[i - coin] >= 0:
                min_moves = 1 + minimums[i - coin]
                if min_moves < minimums[i]:
                    minimums[i] = min_moves
        if minimums[i] > total:
            minimums[i] = -1

    print(minimums)
    return minimums[total]
