# -*- coding: utf-8 -*-

from LatexItem import LatexItem


class RegexReplacement():

    KEEP = 0
    DELETE = 1

    def __init__(self, latexItem=LatexItem.COMMAND, replacement=[["#", KEEP, "#"]]):

        self.__latexItem = latexItem
        self.__replacement = replacement
 
    def latexItem(self):
        return self.__latexItem

    def replacement(self):
        return self.__replacement

    def __str__(self):
        data = ""
        for a in self.__replacement:
            data+=str(a)
        return "<RegexReplacement.Instance latexItem='"+str(self.__keepKeyword)+"', data='"+data+"'>"

