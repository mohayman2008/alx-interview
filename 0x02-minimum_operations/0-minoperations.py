#!/usr/bin/python3
'''The module provides function definition to calculate the minimum required
operations to reach a given number of characters starting from a single
character and only using "Copy All" and "Paste" operations'''
from __future__ import annotations


def minOpsRecurse(n: int, initialVal: int = 2, buf: int = 1) -> int:
    '''The function recursevly calculate the minimum required operations to
    reach a given number of characters only using "Copy All" and "Paste"
    operations'''
    if n < initialVal or buf < 1:
        return -1
    if n == initialVal:
        return 0

    remainder = n - initialVal

    if remainder % initialVal == 0:
        return 2 + minOpsRecurse(n, 2 * initialVal, initialVal)
    return 1 + minOpsRecurse(n, initialVal + buf, buf)


def minOperations(n: int) -> int:
    '''The function calculate the minimum required operations to reach a given
    number of characters starting from a single character and only using
    "Copy All" and "Paste" operations'''
    if type(n) != int or n <= 1:
        return 0
    if n == 2:
        return 2
    return 2 + minOpsRecurse(n, 2, 1)
