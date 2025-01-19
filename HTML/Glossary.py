#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

class Glossary():
    """Create Glossary"""

    def __init__(self, filename) -> None:
        self.__filename = filename
        self.__glossaries = [] #['LSE', 'Low Speed External', 'Oscillateur de faible fréquence'), ('', '', '')]

    def parse(self) -> str:
       
        #\addGlossaryInput{SS}{Slave Select}{Broche de contrôle SPI}
        file = open(self.__filename, "r")
        print("PARSE GLS")
        line = file.readline()
        regexCommand = r".*\\addGlossaryInput\{(.*)\}\{(.*)\}\{(.*)\}"
        while(line != ""):

            if(re.match(regexCommand, line)):
                print(">>> Glossary find")
                group = re.compile(r'.*\\addGlossaryInput'+r'\{(.+?)}\{(.+?)\}\{(.+?)\}').findall(line)
                self.__glossaries.append(group)
            line = file.readline()
        return self.__glossaries
