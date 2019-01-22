#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''测试是否对only one真心

Command line usage:
$ ./onlyone.py name1 name2 name3 ...
'''

class MyBeautifulGirl(object):
    
    __instance = None
    __onlyOne = "Jenny"

    def __new__(cls, *names):
        if not cls.__instance:
            MyBeautifulGirl.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *names):
        self.__others = []
        if names:
            for name in names:
                if name.lower() == MyBeautifulGirl.__onlyOne.lower():
                    print("遇见" + MyBeautifulGirl.__onlyOne + ", 我一见钟情")
                else:
                    print("遇见" + name + ", 我置若罔闻")
                    self.__others.append(name)
        else:
            print("遇见" + MyBeautifulGirl.__onlyOne + ", 我一见钟情")

    def getOnlyOne(self):
        return MyBeautifulGirl.__onlyOne

    def showMyHeart(self):
        if self.__others:
            for other in self.__others:
                print("对不起, " + other)
        print(MyBeautifulGirl.__onlyOne + "是我心中的唯一")

def testLove(*names):
    other = MyBeautifulGirl(*names)
    other.showMyHeart()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        testLove()
    else:
        others = sys.argv[1:]
        testLove(*others)
