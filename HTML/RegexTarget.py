# -*- coding: utf-8 -*-

class RegexTarget():

    BEFORE = 0
    AFTER = 1
    BETWEEN = 2

    def __init__(self, type=BETWEEN, keyword="command", target=["{", "}"], iterations=1):

        self.__type = type
        self.__keyword = keyword
        self.__target = target
        self.__iterations = iterations

        if(len(self.__target) == 1 and (type != RegexTarget.BEFORE or type != RegexTarget.AFTER)):
            print("Target must contains 2 items (start delimiter and end delimiter")

    def keyword(self):
        return self.__keyword

    def type(self):
        return self.__type

    def target(self):
        return self.__target

    def iterations(self):
        return self.__iterations

    def __str__(self):
        return "<RegexTarget.Instance keyword="+self.__keyword+", delim=['"+self.__target[0]+"', '"+self.__target[1]+"']>"

