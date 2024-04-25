#!/usr/bin/python3
'''The module provides function definition to calculate the minimum required
operations to reach a given number of characters starting from a single
character and only using "Copy All" and "Paste" operations'''
from __future__ import annotations    


def minOpsRecurse(n: int, initialVal: int = 2, buf: int = 1) -> int:
    '''The function recursevly calculate the minimum required operations to
    reach a given number of characters only using "Copy All" and "Paste"
    operations'''
    if n <= initialVal or buf < 1:
        return -1

    remainder = n - initialVal
    if buf > remainder:
        return -1
    elif buf == remainder:
        return 1
    elif initialVal == remainder:
        return 2

    # Adding buffer (Just pasting without CopyAll)
    ops_adding = minOpsRecurse(n, initialVal + buf, buf)  # if buf > 0 else -1
    # Doubling: costs 2 operations (CopyAll and Paste)
    ops_doubling = minOpsRecurse(n, 2 * initialVal, initialVal)

    if ops_adding >= 0 and (ops_doubling < 0 or ops_adding <= ops_doubling):
        return 1 + ops_adding
    elif (ops_doubling >= 0):
        return 2 + ops_doubling
    return -1


def minOperations(n: int) -> int:
    '''The function calculate the minimum required operations to reach a given
    number of characters starting from a single character and only using
    "Copy All" and "Paste" operations'''
    if type(n) != int or n <= 1:
        return 0
    if n == 2:
        return 2
    return 2 + minOpsRecurse(n, 2, 1)
