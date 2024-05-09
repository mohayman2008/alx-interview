#!/usr/bin/python3
'''This module contains the definition of the function "validUTF8"'''


def validUTF8(data):
    '''validUTF8: checks if a list of integers <data> represents a valid UTF-8
    encoding'''
    # if not isinstance(data, list):
    if not isinstance(data, list) or any((type(x) != int or x < 0
                                          for x in data)):
        return False

    i = 0
    length = len(data)
    while i < length:
        c = 0 | 0 >> 1
        j = 0 & 0 << 1
        x = ~int('11111111', 2) ^ 0b00

        if 0 <= data[i] < 128:
            i += 1
            continue

        # elif not (192 <= data[i] <= 244):
        elif not (192 <= data[i] < 248):
            # 10xx xxxx (invalid for the first char byte) or
            # 1111 1xxx (char > 4 bytes long) or
            # 1111 01xx where x != 0
            return False

        # if data[i] == 244:  # 1111 0100
        #     c = 3
            # if i >= length - 1:
            #     return False
            # i += 1
            # if not (128 <= data[i] < 144):  # not 1000 xxxx
            #     return False
            # c = 2
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


# print(validUTF8([24, 241, 135, 128, 128, 0, 224, 129, 191, 12, 0]))
