# -*- coding: utf-8 -*-
from RegexRemplacement import RegexReplacement
from RegexTarget import RegexTarget

class Regex():

    def __init__(self, target, reference, replacement):

        assert(type(target))is RegexTarget
        assert(type(reference)) is str
        assert(type(replacement)) is RegexReplacement

        self.__target = target
        self.__reference = reference
        self.__replacement = replacement

    def __str__(self):
        data =  "<Regex.Instance '"+self.__reference+"'>\n"
        data += "\t"+str(self.__target)+"\n"
        data += "\t"+str(self.__replacement)
        return data

    def target(self):
        return self.__target
    
    def reference(self):
        return self.__reference

    def replacement(self):
        return self.__replacement 