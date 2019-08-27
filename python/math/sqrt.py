#!/usr/bin/env python3

# -*- coding: utf-8 *-

def getSquareRoot(n, deltaThreshold, maxTry):
    """计算大于1的正整数之平方根

    参数:
    n -- 待求的数
    deltaThreshold -- 误差的阈值
    maxTry -- 二分查找的最大次数

    返回值:
    平方根的解
    """
    if n <= 1:
        return 1.0

    min = 1.0
    max = float(n)
    
    i = 0
    while i < maxTry:
        middle = (min + max) / 2;
        square = middle * middle
        delta = abs((square / n) - 1)
        if delta <= deltaThreshold:
            return middle
        else:
            if square > n:
                max = middle
            else:
                min = middle
    return -2.0

if __name__ == '__main__':
    number = 10
    squareRoot = getSquareRoot(number, 0.000001, 1000)
    if squareRoot == -1.0:
        print("请输入大于1的整数")
    elif squareRoot == -2.0:
        print("未能找到解")
    else:
        print(f"{number}的平方根是{squareRoot}")
