#!/usr/bin/python3
'''The module provides function definition to calculate the minimum required
operations to reach a given number of characters starting from a single
character and only using "Copy All" and "Paste" operations'''
from typing import Optional


def minOperations(n: int, initialVal: int = 1, buf: int = 0) -> int:
    '''The function calculate the minimum required operations to reach a given
    number of characters starting from a single character and only using
    "Copy All" and "Paste" operations'''
    if n <= 1:
        return 0

    remainder = n - initialVal
    if buf > remainder:
        return -1
    elif buf == remainder:
        return 1
    elif initialVal == remainder:
        return 2

    # Adding buffer (Just pasting without CopyAll)
    ops_adding = minOperations(n, initialVal + buf, buf) if buf > 0 else -1
    # Doubling: costs 2 operations (CopyAll and Paste)
    ops_doubling = minOperations(n, 2 * initialVal, initialVal)

    if ops_adding >= 0 and (ops_doubling < 0 or ops_adding <= ops_doubling):
        return 1 + ops_adding
    elif (ops_doubling >= 0):
        return 2 + ops_doubling
    return -1
