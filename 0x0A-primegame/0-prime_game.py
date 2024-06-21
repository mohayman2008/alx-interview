#!/usr/bin/python3
'''The module contains the definition of function "isWinner"'''

PLAYER1_NAME = 'Maria'
PLAYER2_NAME = 'Ben'


def isWinner(x, nums):
    '''Returns name of the player that won the most rounds of choosing a prime
    number'''
    p1_rounds = 0
    p2_rounds = 0
    memo = {}
    length = len(nums)

    for i in range(x):
        n = nums[i % length]

        num_moves = memo.get(n)
        if num_moves is None:
            num_moves = primesCount(n)
            memo[n] = num_moves

        if num_moves % 2:
            p1_rounds += 1
        else:
            p2_rounds += 1

    if p1_rounds == p2_rounds:
        return None
    elif p1_rounds > p2_rounds:
        return PLAYER1_NAME
    else:
        return PLAYER2_NAME


def primesCount(n):
    '''Returns name of the player that won the most rounds of choosing a prime
    number'''
    isPrime = [True for i in range(n + 1)]
    count = 0

    i = 2
    while i <= n:
        if isPrime[i]:
            if i * i > n:
                break
            count += 1
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
        i += 1

    for i in range(i, n + 1):
        if isPrime[i]:
            count += 1

    return count
