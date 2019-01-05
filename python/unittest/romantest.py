'''Unit test for roman.py

This program is part of 'Dive Into Python 3', a free Python book for
experienced programmers. Visit http://diveintopython3.org/ for the
latest version.
'''

import roman
import unittest

class KnownValues(unittest.TestCase):
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman.to_roman(integer)
            self.assertEqual(numeral, result)

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 4000)

    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)

    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, -1)

    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(roman.NotIntegerError, roman.to_roman, 0.5)


if __name__ == '__main__':
    unittest.main()

# 使用-v命令行参数, 会有更详细的输出: python romantest1.py -v

# 运行脚本就会执行unittest.main(), 该方法执行了每一条测试用例
# 而每一条测试用例都是romantest.py中的类方法, 这些测试类没有必要的组织要求
# 它们每一个都包括一个独立的测试方法, 或者你也可以编写一个含有多个测试方法的类
# 唯一的要求就是每一个测试类都必须继承unittest.TestCase

# 对于每一个失败的测试用例, unittest模块会打印出测试方法的docstring
# 对于每一个失败的测试用例, unittest模块会打印出详细的跟踪信息
# 在说明每个用例的详细执行结果之后, unittest打印出一个简述来说明"多少用例被执行了"和"测试执行了多长时间"

# unittest可以区别用例执行失败跟程序错误, 像assertXYZ, assertRaises这样的assertEqual方法的失败是因为被声明的条件不是为真, 或者预期的异常没有抛出
# 错误, 则是另一种异常, 它是因为被测试的代码或单元测试用例本身的代码问题而引起的

# unittest提供了assertRaises方法, 该方法需要的参数: 期望的异常, 测试的方法, 传入给方法的参数

