# -*- coding: utf-8 -*-

class Title():

    PART = 0
    H1 = 1
    H2 = 2
    H3 = 3
    H4 = 4
    H5 = 5

    ALL = []

    def __init__(self, type, content):

        self.__type = type
        self.__content = content

        Title.ALL.append(type, content)


    def create(self):

        if(self.__type==Title.H1):
            return "<h1>"+self.__content+"</h1>"
        if(self.__type==Title.H2):
            return "<h2>"+self.__content+"</h2>"
        if(self.__type==Title.H3):
            return "<h3>"+self.__content+"</h3>"
        if(self.__type==Title.H4):
            return "<h4>"+self.__content+"</h4>"
        if(self.__type==Title.H5):
            return "<h5>"+self.__content+"</h5>"

    def tocItem(self, content):

        if(self.__type==Title.H1):
            return "\t"+content
        if(self.__type==Title.H2):
            return "\t\t"+content
        if(self.__type==Title.H3):
            return "\t\t"+content
        if(self.__type==Title.H4):
            return "\t\t"+content
        if(self.__type==Title.H5):
            return "\t\t"+content

    # def generateTableOfContent(self):

    #     toc = "Table of Content"
    #     for t in Title.ALL:
    #         toc += self.tocItem(t)
    #     return toc


