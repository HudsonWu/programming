# -*- coding: utf-8 -*-

def int3binary(num):
    result = []
    while num != 0:
        result.append(num & 1)
        num = num >> 1
    result.reverse()
    return result

print(*int3binary(-10))
