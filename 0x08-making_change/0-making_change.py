#!/usr/bin/python3
'''The module contains the definition of function "makeChange"'''


def makeChange(coins, total):
    '''The function determines the fewest number of coins needed to meet a
    given amount "total", given a pile of "coins" of different values'''
    if total <= 0:
        return 0
    if not len(coins):
        return -1

    coins.sort(reverse=True)
    return calculateChange(coins, total, {})


def calculateChange(coins, total, memo):
    '''The function recursively determines the fewest number of coins needed
    to meet a given amount "total", given a pile of "coins" of different values
    '''
    if total <= 0:
        return 0

    memoized = memo.get(total)
    if memoized is not None:
        return memoized

    min_moves = total + 1
    for coin in coins:
        if coin == total:
            memo[total] = 1
            return 1
        if coin > total:
            break
        rest_moves = calculateChange(coins, total - coin, memo)
        if rest_moves >= 0 and rest_moves < min_moves:
            min_moves = rest_moves + 1

    if min_moves == total + 1:
        min_moves = -1
    memo[total] = min_moves

    return min_moves
