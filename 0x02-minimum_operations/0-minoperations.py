#!/usr/bin/python3
'''The module provides function definition to calculate the minimum required
operations to reach a given number of characters starting from a single
character and only using "Copy All" and "Paste" operations'''
from __future__ import annotations


def minOperations(n: int) -> int:
    '''The function calculate the minimum required operations to reach a given
    number of characters starting from a single character and only using
    "Copy All" and "Paste" operations'''
    if type(n) != int or n <= 1:
        return 0
    if n == 2:
        return 2

    numOps: int = 2
    completed: int = 2
    clipboard: int = 1
    remaining: int

    while n > completed:
        remaining = n - completed

        if remaining % completed == 0:
            numOps += 2
            clipboard = completed
            completed *= 2
        else:
            numOps += 1
            completed += clipboard

    return numOps
