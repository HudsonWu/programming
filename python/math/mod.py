# -*- coding: utf-8 -*-

DIVIDEND = 7
RAND = 590127

def encrypt(num):
    if not isinstance(num, int):
        raise TypeError("num is not 'int' object")
    # int转为list
    num = map(int, str(num))

    # 每个位数的值加上随机数
    num = map(lambda i:i+RAND, num)
    # 保存商和求余
    quotient, num = zip(*[(i//DIVIDEND, i%DIVIDEND) for i in list(num)])
    # 反转
    num = list(num)[::-1]
    print(list(num))
    # list转回int
    num = map(str, num)
    # num = int(''.join(list(num)))
    num = ''.join(list(num))

    # 返回加密数据和商
    return (num, quotient)

def decrypt(num, quotient):
    # if not isinstance(num, int):
    #     raise TypeError("num is not 'int' object")
    # 转为list
    num = map(int, str(num))

    # 反转
    num = list(num)[::-1]
    # 商和余求值
    for i, v in enumerate(num):
        num[i] = v + quotient[i] * DIVIDEND
    # 每个位数的值减去随机数
    num = map(lambda i:i-RAND, num)

    # list转回int
    num = map(str, num)
    num = int(''.join(list(num)))

    return num

if __name__ == '__main__':
    num = 8251
    print('加密', num)
    en_num, q = encrypt(num)
    print(f'加密后{en_num}, 商为{q}')
    print('解密...')
    de_num = decrypt(en_num, q)
    print(de_num)
