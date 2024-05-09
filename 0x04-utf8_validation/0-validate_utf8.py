#!/usr/bin/python3
'''This module contains the definition of the function "validUTF8"'''


def validUTF8(data):
    '''validUTF8: checks if a list of integers <data> represents a valid UTF-8
    encoding'''
    if not isinstance(data, list):
        return False

    i = 0
    length = len(data)
    while i < length:
        c = 0
        j = 0

        if data[i] < 128:
            i += 1
            continue
        elif not (192 <= data[i] < 248):
            # 10xx xxxx (invalid for the first char byte) or
            # 1111 1xxx (char > 4 bytes long)
            return False

        if data[i] >= 240:  # 1111 0xxx
            c = 4
        elif data[i] >= 224:  # 1110 xxxx
            c = 3
        elif data[i] >= 192:  # 110x xxxx
            c = 2

        for j in range(c):
            i += 1
            if not (128 >= data[i] < 192):  # not 10xx xxxx
                return False
    return True
