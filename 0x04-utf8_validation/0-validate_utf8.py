#!/usr/bin/python3
'''This module contains the definition of the function "validUTF8"'''


def validUTF8(data):
    '''validUTF8: checks if a list of integers <data> represents a valid UTF-8
    encoding'''
    if not isinstance(data, list) or any((type(x) != int or x < 0
                                          for x in data)):
        return False

    i = 0
    length = len(data)
    while i < length:
        data[i] = data[i] & 0xFF

        if 0 <= data[i] < 128:
            i += 1
            continue

        elif not (192 <= data[i] < 248):
            # 10xx xxxx (invalid for the first char byte) or
            # 1111 1xxx (char > 4 bytes long) or
            # 1111 01xx where x != 0
            return False

        if data[i] >= 240:  # 1111 0xxx
            c = 3
        elif data[i] >= 224:  # 1110 xxxx
            c = 2
        elif data[i] >= 192:  # 110x xxxx
            c = 1

        if i + c >= length:
            return False

        for j in range(c):
            i += 1
            if not (128 <= data[i] < 192):  # not 10xx xxxx
                return False
        i += 1
    return True
