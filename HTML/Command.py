# -*- coding: utf-8 -*-

from copy import copy
from genericpath import isdir, isfile
import re

from MessageBox import *
from Color import *
from Image import *
from Label import *
from Footnote import *
    
class Command():
    """Create generic command"""

    """Flags"""
    COMMAND = 1
    ENVIRONMENT = 2
    FORMULA = 3
    INDEX = 4
    FOOTNOTE = 5
    NEW_COMMAND = 6
    GLOSSARY = 7

    BEGIN_LIST = 8
    END_LIST = 9
    ITEM_LIST = 10


    IMAGE = 11
    NEWLINE = 12

    BEGIN_CODE = 13
    END_CODE = 14

    MESSAGE_BOX = 15
    ANCHOR = 16
    LINK = 17

    COLOR = 18
    LABEL = 19

    PART_IMAGE = 20
    ESCAPE = 21
    COMMENT = 22


    def __init__(self, name, argumentsNumber, type, replacement) -> None:

        self.__name = name
        self.__argumentsNumber = argumentsNumber
        self.__type = type
        self.__replacement = replacement

        #New commands
        self.__allNewCommands = []

        #Footnote
        self.__allNewFootnotes = []  

        self.__oldTemplate = ["\\"+self.__name+"{", "}"]

        self.__flag = 1000

    def flag(self):
        return self.__flag

    def type(self):
        return self.__type
    
    def replacement(self):
        return self.__replacement
    
    def oldTemplate(self):
        return self.__oldTemplate

    def name(self):
        return self.__name

    def argumentNumber(self):
        return self.__argumentsNumber

    def parse(self, content, glossary=[]) -> str:
        """Return str with update content"""

        oldContent = copy(content)

        # if(self.__type == self.COMMAND):

        #     regexCommand = r".*\\"+self.__name+"*{(.*)\}"
        #     iteration = 0

        #     while(re.match(regexCommand, content)):
        #         iteration+=1
        #         #print("Match : "+content+ " = "+content+"")
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         for group in result:
        #             searched = self.__oldTemplate[0]+group+self.__oldTemplate[1]
        #             new = self.__replacement[0]+group+self.__replacement[1]
        #             content = content.replace(searched, new)
        #         if(iteration>=6):
        #             self.__flag = self.COMMAND
        #             return content
        #     if(content==oldContent):
        #         return None
        #     else:
        #         self.__flag = self.COMMAND
        #         return r""+content.replace("\n","")

        # if(self.__type == self.ANCHOR):  #

        #     regexCommand = r".*\\"+self.__name+"{(.*)\}"
        #     iteration = 0

        #     if(re.match(regexCommand, content)):
        #         iteration+=1
        #         #print("Match : "+content+ " = "+content+"")
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         for group in result:
        #             searched = self.__oldTemplate[0]+group+self.__oldTemplate[1]
        #             new = "<span id='"+group+"'></span>"
        #             content = content.replace(searched, new)
        #         if(iteration>=6):
        #             self.__flag = self.ANCHOR
        #             return content
        #     if(content==oldContent):
        #         return None
        #     else:
        #         self.__flag = self.ANCHOR
        #         return r""+content.replace("\n","")

        # if(self.__type == self.LINK): 

        #     regexCommand = r".*\\"+self.__name+"{(.*)\}"
        #     iteration = 0

        #     if(re.match(regexCommand, content)):
        #         iteration+=1
        #         #print("Match : "+content+ " = "+content+"")
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         for group in result:
        #             searched = self.__oldTemplate[0]+group+self.__oldTemplate[1]
        #             new = "<a href='#"+group+"'>"+group+"</a>"
        #             content = content.replace(searched, new)
        #         if(iteration>=6):
        #             self.__flag = self.LINK
        #             return content
        #     if(content==oldContent):
        #         return None
        #     else:
        #         self.__flag = self.LINK
        #         return r""+content.replace("\n","")


        # if(self.__type == self.COLOR):  #Color

        #     regexCommand = r".*\\"+self.__name+"{(.*)\}"
        #     iteration = 0
            
        #     while(re.match(regexCommand, content)):
        #         iteration+=1
        #         result = re.compile(r'.*'+self.__name+r'\{(.+?)}\{(.+?)}').findall(content)
        #         #print(result)
        #         for group in result:
        #             if(len(group)==2):
        #                 #print("OK")
        #                 color=group[0]
        #                 text=group[1]
        #                 data = Color.create(color, text)
        #                 content = content.replace("\\colors{"+color+"}{"+text+"}", data)
        #                 #print(content)
        #         self.__flag = self.COLOR
        #         return content

        # if(self.__type == self.LABEL): 

        #     regexCommand = r".*\\"+self.__name+"{(.*)\}"
        #     iteration = 0
            
        #     while(re.match(regexCommand, content)):
        #         iteration+=1
        #         result = re.compile(r'.*'+self.__name+r'\{(.+?)}\{(.+?)}\{(.+?)}').findall(content)
        #         #print(result)
        #         for group in result:
        #             if(len(group)==self.__argumentsNumber):
        #                 #print("OK")
        #                 color=group[0]
        #                 id=group[1]
        #                 text=group[2]
        #                 data = Label.create(color, text)
        #                 content = content.replace("\\lbl{"+color+"}{"+id+"}{"+text+"}", data)
        #                 #print(content)
        #         self.__flag = self.LABEL
        #         return content

        # if(self.__type == self.PART_IMAGE): 

        #     regexCommand = r".*\\"+self.__name+"{(.*)\}"
        #     iteration = 0
            
        #     while(re.match(regexCommand, content)):
        #         iteration+=1
        #         result = re.compile(r'.*'+self.__name+r'\{(.+?)}\{(.+?)}\{(.+?)}').findall(content)
        #         #print(result)
        #         for group in result:
        #             if(len(group)==self.__argumentsNumber):
        #                 #print("OK")
        #                 color=group[0]
        #                 id=group[1]
        #                 text=group[2]
        #                 content = content.replace("\\"+self.__name+"{"+color+"}{"+id+"}{"+text+"}", " ")
        #                 #print(content)
        #         self.__flag = self.PART_IMAGE
        #         return content

        # elif(self.__type == self.FORMULA):

        #     regexCommand = r".*\$(.*)\$"
        #     if(re.match(regexCommand, content)):
        #         #print(">>> MATH found"+content)
        #         while(re.match(regexCommand, content)):
                
        #             result = re.compile(r'\$(.+?)\$').findall(content)
        #             #print(result)
        #             for r in result:
        #                 content = content.replace(r, "\("+r+"\)")
        #         # if(iteration>=6):
        #         #     return content
        #             self.__flag = self.FORMULA
        #             return content.replace("$","")
        #     if(content==oldContent):
        #         return None
        #     else:
        #         self.__flag = self.FORMULA
        #         return r""+content.replace("\n","")


        # elif(self.__type == self.INDEX):

        #     regexCommand = r".*\\"+self.__name+"{(.*)\}"

        #     while(re.match(regexCommand, content)):
            
        #         #print("Match : "+content+ " = "+content+"")
        #         result = re.compile(r'.*\\index'+r'\{(.+?)}').findall(content)
        #         for group in result:
                    
        #             searched = self.__oldTemplate[0]+group+self.__oldTemplate[1]
        #             new = " "
        #             content = content.replace(searched, new)
        #     #return content
        #     if(content==oldContent):
        #         return None
        #     else:
        #         self.__flag = self.INDEX
        #         return r""+content.replace("\n","")

        # elif(self.__type == self.NEW_COMMAND):

        #     regexCommand = r".*\\"+self.__name+"*{(.*)\}"

        #     while(re.match(regexCommand, content)):
            
        #         #print("Match : "+content+ " = "+content+"")
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         if(len(result)==2):
                
        #             commandExists=False
        #             for c in self.__allNewCommands:
        #                 if self.__name in c[0]:
        #                     commandExists=True
        #             if(not commandExists):
        #                 self.__allNewCommands.append((result[0], result[1]))
        #                 #print(">>> New command found "+result[0]+" - "+result[1])
        #                 self.__flag = self.NEW_COMMAND
        #                 return content
        #         else:
        #             #print(">>> Bad new command format")
        #             pass

        # elif(self.__type == self.NEWLINE):

        #     regexCommand = r".*\\"+self.__name+".*"

        #     while(re.match(regexCommand, content)):
        #         searched = r"\\"+self.__name
        #         new = "<br>"
        #         content = content.replace("\\"+self.__name, "<br>")
        #     self.__flag = self.NEWLINE
        #     return content

        # elif(self.__type == self.COMMENT):

        #     regexCommand = r".*"+self.__name+"(.*)"

        #     if(re.match(regexCommand, content)):
        #         result = re.compile( r".*"+self.__name+"(.*)").findall(content)
                
        #         searched = r""+self.__name
        #         content = content.replace(self.__name, "")
        #         content = content.replace(result[0], " ")
        #     self.__flag = self.NEWLINE
        #     return content

        # elif(self.__type == self.GLOSSARY):

        #     regexCommand = r".*\\"+self.__name+"*{(.*)\}"

        #     while(re.match(regexCommand, content)):
            
        #         #print("Match : "+content+ " = "+content+"")
        #         result = re.compile(r'.*'+self.__name+r'\{(.+?)}').findall(content)
        #         if(len(result)==1):
        #             searched = self.__oldTemplate[0]+result[0]+self.__oldTemplate[1]
        #             for g in glossary:
        #                 if(len(g)>0):
        #                     #print(len(g))
        #                     if g[0][0] == result[0]:
        #                         #print("FOund glossary")
        #                         gls = g[0]
        #                         new = "<span title=\""+gls[1]+" : "+gls[2]+"\" style='color:blue;'>"+gls[0]+"</span>"
        #                         content = content.replace(searched, new)
        #                 #print(">>> New glossary found "+result[0])
        #             self.__flag = self.GLOSSARY
        #             return content
        #         else:
        #             #print(">>> Bad glossary format")
        #             pass


        # elif(self.__type == self.BEGIN_LIST):

        #     regexCommand = r".*\\begin\{"+self.__name+"\}"

        #     if(re.match(regexCommand, content)):  #Only one list in line
        #         #print(">>> Begin List found"+content)
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         if(len(result)==self.__argumentsNumber and (self.__name in result[0])):
        #             self.__flag = self.BEGIN_LIST

        #             return "<ul>"

        # elif(self.__type == self.END_LIST):

        #     regexCommand = r".*\\end\{("+self.__name+r")\}"

        #     if(re.match(regexCommand, content)):  #Only one list in line
        #         self.__flag = self.END_LIST
        #         return "</ul>"

        # elif(self.__type == self.ITEM_LIST):

        #     regexCommand = r".*\\"+self.__name+"*(.*)"

        #     if(re.match(regexCommand, content)):

        #         #print(">>> Line content found" + content)
        #         self.__flag = self.ITEM_LIST
        #         return content.replace("\\item", "<li>")+"</li>"


        # elif(self.__type == self.BEGIN_CODE):

        #     regexCommand = r".*\\begin\{"+self.__name+"\}"

        #     if(re.match(regexCommand, content)):  #Only one list in line
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         if(len(result)==self.__argumentsNumber):
        #             self.__flag = self.BEGIN_CODE
        #             return "<hr><pre style='background-color:#F5F5F5;padding-left:1em;'><code>"

        # elif(self.__type == self.END_CODE):

        #     regexCommand = r".*end\{"+self.__name+r".*\}"
        #     if(re.match(regexCommand, content)):  #Only one list in line
        #         if(self.__name in content):
        #             self.__flag = self.END_CODE
        #             return "</code></pre><hr>"

        # elif(self.__type == self.IMAGE):

        #     regexCommand = r".*\\"+self.__name+"(.*)"

        #     if(re.match(regexCommand, content)):  #Only one list in line
        #         #print(">>> Begin List found"+content)
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         if(len(result)==self.__argumentsNumber):
        #             folder = str(result[0])
        #             name = folder.split("/")[1]
        #             legend = result[1]
        #             size = int(float(result[2])*100)

        #             folder = Image.findPath(self.__replacement[0], name, "")
        #             #print(folder)
        #             self.__flag = self.IMAGE
        #             return Image.create(folder.replace(self.__replacement[0], ""), legend, size)

        # elif(self.__type == self.MESSAGE_BOX):

        #     regexCommand = r".*\\"+self.__name+r"\{(.*)\}"

        #     if(re.match(regexCommand, content)):  #Only one list in line
        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         if(len(result)==self.__argumentsNumber): 
        #             title = str(result[0])
        #             colorframe = result[2]
        #             backgroundColor = result[1]
        #             text= result[3]
        #             data = MessageBox.create(title, backgroundColor,colorframe, text)
        #             self.__flag = self.MESSAGE_BOX
        #             return data    
        #         else:
        #             print(">>> MessageBox Error"+content)
        #             pass
        # elif(self.__type == self.ESCAPE):

        #     regexCommand = r".*\\"+self.__name

        #     if(re.match(regexCommand, content)):  #Only one list in line

        #         result = re.compile(r'\{(.+?)}').findall(content)
        #         searched = r"\_"
        #         new = " "
        #         content = content.replace(searched, new)
        #         return content
        # else:
        #     pass

    def exportNewCommand(self):

        if(len(self.__allNewCommands)>=1):
            return self.__allNewCommands[0]

    def replaceShortcut(self, line):
        """Replace new command expression"""


    def footnotes(self):
        return self.__allNewFootnotes