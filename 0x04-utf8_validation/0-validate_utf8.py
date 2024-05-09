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

        if data[i] < 0b10000000:  # < 0b 1000 0000
            i += 1
            continue

        # # elif not (192 <= data[i] < 248):
        # elif data[i] & 0b11000000 == 0b10000000 or (data[i] & 0b11111000 ==
        #                                             0b11111000):
        #     # 10xx xxxx (invalid for the first char byte) or
        #     # 1111 1xxx (char > 4 bytes long)
        #     return False

        # if data[i] >= 240:  # 1111 0xxx
        if data[i] >> 3 == 0b11110:  # 1111 0xxx
            c = 3
        # elif data[i] >= 224:  # 1110 xxxx
        elif data[i] >> 4 == 0b1110:  # 1110 xxxx
            c = 2
        # elif data[i] >= 192:  # 110x xxxx
        elif data[i] >> 5 == 0b110:  # 110x xxxx
            c = 1
        else:
            return False

        if i + c >= length:
            return False

        for j in range(c):
            i += 1
            if data[i] & 0b11000000 != 0b10000000:  # not 10xx xxxx
                return False
        i += 1
    return True


print(validUTF8([24, 241, 135, 128, 128, 0, 224, 129,
                 191, 12, 0, 257, 1056, 247]))
