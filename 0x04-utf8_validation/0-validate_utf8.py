#!/usr/bin/python3
'''This module contains the definition of the function "validUTF8"'''


def validUTF8(data):
    '''validUTF8: checks if a list of integers <data> represents a valid UTF-8
    encoding'''
    if not isinstance(data, list) or any((type(x) != int or x < 0
                                          for x in data)):
        return False

    data = data.copy()

    i = 0
    length = len(data)
    while i < length:
        data[i] = data[i] & 0xFF

        if not data[i] >> 7:  # < 0b 1000 0000
            i += 1
            continue

        if data[i] >> 3 == 0b11110:  # 1111 0xxx
            c = 3
        elif data[i] >> 4 == 0b1110:  # 1110 xxxx
            c = 2
        elif data[i] >> 5 == 0b110:  # 110x xxxx
            c = 1
        else:
            return False

        if i + c >= length:
            return False

        i += 1
        for j in range(c):
            if data[i] >> 6 != 0b10:  # not 10xx xxxx
                return False
            i += 1
    return True
