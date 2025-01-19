# -*- coding: utf-8 -*-
import re
from LatexItem import LatexItem, LatexContentType, LatexParserStatus
import time
from RegexTarget import RegexTarget
from RegexRemplacement import RegexReplacement
from Regex import Regex
from Command import Command
#Submodule
from Footnote import Footnote
from Image import Image
from Label import Label
from MessageBox import MessageBox
from Glossary import Glossary

from copy import copy
from Color import Color
import os
from os.path import isfile, join



class Debug():

    #Types
    INFO = "Info"
    ERROR = "Error"
    WARNING = "Warning"
    SUCCESS = "Success"

    def __init__(self):


         #Status
        self.__displayErrors = True
        #Colors
        self.__blueColor = '\033[94m'
        self.__greenColor = '\033[92m'
        self.__orangeColor = '\033[93m'
        self.__redColor = '\033[91m'
        self.__defaultColor = '\033[0m'
        self.__bold = '\033[1m'   

        #prompt
        self.__displayPromptError = "["+self.__redColor+"Error"+self.__defaultColor+"] >>> "
        self.__displayPromptWarning = "["+self.__orangeColor+"Warning"+self.__defaultColor+"] >>> "
        self.__displayPromptSuccess = "["+self.__greenColor+"Success"+self.__defaultColor+"] >>> "
        self.__displayPromptInfo = "["+self.__blueColor+"Info"+self.__defaultColor+"] >>> "
        self.__displayPromptInput = "["+self.__bold+"Input"+self.__defaultColor+"] >>> "

    def displayErrors(self, displayErrorStatus=True):

        self.__displayErrors = displayErrorStatus

    def println(self, message, type=INFO):

        if(not self.__displayErrors):
            return 
        if(type==Debug.INFO):
            print(self.__displayPromptInfo+message)
        elif(type==Debug.ERROR):
            print(self.__displayPromptError+message)
        elif(type==Debug.WARNING):
            print(self.__displayPromptWarning+message)
        elif(type==Debug.SUCCESS):
            print(self.__displayPromptSuccess+message)
        else:
            print(self.__displayPromptError+" Bad type format for type in Debug.println method")


class LatexParser(Debug):

    def __init__(self, filename):

        super().__init__()
        self.__lines = []
        self.__lineCounter = 0
        self.__filename = filename
        self.println("Creating glossary...")
        self.__glossary = Glossary("Make/Glossaries.tex").parse()
        self.println("Creating glossary : <OK>")
        self.__outputLines = []

        self.__greenColor = '\033[92m'
        self.__orangeColor = '\033[93m'
        self.__redColor = '\033[91m'
        self.__defaultColor = '\033[0m'

        #Read lines
        self.__lines = self.readLines()

        #PArser states
        self.__parserState = LatexParserStatus(LatexParserStatus.STOPPED)
        self.__parserContentType = LatexContentType(LatexContentType.TEXT)
        self.__flag = LatexItem.COMMAND

        self.__allNewCommands = []
        self.__genericCommands = [

            Command("bold", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("textbf", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("textit", 1, Command.COMMAND, ["<u>", "</u>"]),
            Command("italic", 1, Command.COMMAND, ["<i>", "</i>"]),
            Command("emph", 1, Command.COMMAND, ["<i>", "</i>"]),
            Command("ldots", 1, Command.COMMAND, ["", ""]),
            Command("underline", 1, Command.COMMAND, ["<u>", "</u>"]),
            Command("ib", 1, Command.COMMAND, ["<b><i>", "</i></b>"]),
            Command("bi", 1, Command.COMMAND, ["<b><i>", "</i></b>"]),
            Command("url", 1, Command.COMMAND, ["<a class=\"alert-link\">", "</a>"]),
            Command("link", 1, Command.COMMAND, ["<a class=\"alert-link\">", ""]),
            Command("nameref", 1, Command.LINK, ["<a href='#url'>", "</a>"]),
            Command("label", 1, Command.ANCHOR, ["<a href='#url'>", "</a>"]),
            Command("badge", 1, Command.COMMAND, ["<span class='badge badge-primary'>", "</span>"]),
            Command("file", 1, Command.COMMAND, ["<span class='badge badge-primary'>", "</span>"]),
            Command("loc", 1, Command.COMMAND, ["</br><span class='badge badge-info'>", "</span><br>"]),
            Command("dir", 1, Command.COMMAND, ["<span class='badge badge-light'>", "</span>"]),
            Command("lib", 1, Command.COMMAND, ["<span class='badge badge-success'>", "</span>"]),
            Command("shortcut", 1, Command.COMMAND, ["<span class='badge badge-light'>", "</span>"]),
            Command("sym", 1, Command.COMMAND, ["<span class='badge badge-info'>", "</span>"]),
            Command("Question", 1, Command.COMMAND, ["<i>", "</i><br>"]),
            Command("Reponse", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("inputPin", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("outputPin", 1, Command.COMMAND, ["<b>", "</b>"]),

            Command("colors", 1, Command.COLOR, [""]),
            Command("textcolor", 1, Command.COLOR, [""]),
            Command("part", 1, Command.COMMAND, ["<h1 class=''>", "</h1>"]),
            Command("chapter", 1, Command.COMMAND, ["<h2 >", "</h2>"]),
            Command("section", 1, Command.COMMAND, ["<h3>", "</h3>"]),
            Command("subsection", 1, Command.COMMAND, ["<h4>", "</h4>"]),
            Command("subsubsection", 1, Command.COMMAND, ["<h4>", "</h4>"]),
            Command("addPartText", 1, Command.COMMAND, ["<h4>", "</h4>"]),

            Command("shortcut", 1, Command.COMMAND, ["<a class=\"alert-link\">", "<a class=\"alert-link\">"]),
            Command("lib", 1, Command.COMMAND, ["<a class=\"alert-primary\">", "<a class=\"alert-link\">"]),
            Command("dir", 1, Command.COMMAND, ["<a class=\"alert-warning\">", "<a class=\"alert-link\">"]),
            Command("file", 1, Command.COMMAND, ["<a class=\"alert-info\">", "<a class=\"alert-link\">"]),
            Command("bold", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("textbf", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("italic", 1, Command.COMMAND, ["<i>", "</i>"]),
            Command("textit", 1, Command.COMMAND, ["<i>", "</i>"]),
            Command("bi", 1, Command.COMMAND, ["<i><b>", "</b></i>"]),
            Command("bi", 1, Command.COMMAND, ["<i><b>", "</b></i>"]),

            Command("index", 1, Command.INDEX, []), #Delete Index
            Command("\$", 1, Command.FORMULA, ["\\(", "\\)"]),
            #Command("newcommand", 2, Command.NEW_COMMAND, ["", ""]),
            Command("glossary", 1, Command.GLOSSARY, ["", ""]),
            Command("gls", 1, Command.GLOSSARY, ["", ""]),
            Command("footnote", 2, Command.FOOTNOTE, ["", ""]),

            Command("items", 3, Command.BEGIN_LIST, ["", ""]),
            Command("items", 3, Command.END_LIST, ["", ""]),

            Command("enumerate", 1, Command.BEGIN_LIST, ["", ""]),
            Command("enumerate", 1, Command.END_LIST, ["", ""]),
            Command("itemize", 1, Command.BEGIN_LIST, ["", ""]),
            Command("itemize", 1, Command.END_LIST, ["", ""]),

            Command("item", 1, Command.ITEM_LIST, ["", ""]),

            Command("Bash", 1, Command.BEGIN_CODE, ["", ""]),
            Command("Bash", 1, Command.END_CODE, ["", ""]),
            Command("Bash", 2, Command.BEGIN_CODE, ["", ""]),
            Command("Bash", 2, Command.END_CODE, ["", ""]),

            Command("Cpp", 2, Command.BEGIN_CODE, ["", ""]),
            Command("Cpp", 2, Command.END_CODE, ["", ""]),
            Command("Cpp", 1, Command.BEGIN_CODE, ["", ""]),
            Command("Cpp", 1, Command.END_CODE, ["", ""]),

            Command("Python", 1, Command.BEGIN_CODE, ["", ""]),
            Command("Python", 1, Command.END_CODE, ["", ""]),
            Command("lstlisting", 1, Command.BEGIN_CODE, ["", ""]),
            Command("lstlisting", 1, Command.END_CODE, ["", ""]),
            Command("lstlisting", 2, Command.BEGIN_CODE, ["", ""]),
            Command("lstlisting", 2, Command.END_CODE, ["", ""]),

            Command("Latex", 2, Command.BEGIN_CODE, ["", ""]),
            Command("Latex", 2, Command.END_CODE, ["", ""]),

            Command("Latex", 1, Command.BEGIN_CODE, ["", ""]),
            Command("Latex", 1, Command.END_CODE, ["", ""]),

            Command("Html", 1, Command.BEGIN_CODE, ["", ""]),
            Command("Html", 1, Command.END_CODE, ["", ""]),

            Command("newline", 1, Command.NEWLINE, ["", ""]),
            Command("newpage", 1, Command.NEWLINE, ["", ""]), #Normal
            Command("nl", 1, Command.NEWLINE, ["", ""]),
            #Command("n", 1, Command.NEWLINE, ["", ""]),
            #Command("", 1, Command.NEWLINE, ["", ""]),

            Command("img", 3, Command.IMAGE, ["Images"]),
            Command("imgn", 4, Command.IMAGE, ["Images"]),
            Command("imgf", 4, Command.IMAGE, ["Images"]),
            Command("messageBox", 5, Command.MESSAGE_BOX, ["", ""]),
            Command("lbl", 3, Command.LABEL, ["", ""]),
            Command("index", 1, Command.INDEX, ["", ""]),
            Command("partImg", 3, Command.PART_IMAGE, ["", ""]),
            Command("_", 0, Command.ESCAPE, ["", ""]),
            Command("%#", 0, Command.COMMENT, ["", ""])

        ] 

    def setWorkingDir(self, partFolder, imgFolder):

        self.__partFolder = partFolder
        self.__imgFolder = imgFolder

    def __str__(self):
        return "<Parser.Instance filename='"+self.__filename+"', Parser status : "+self.__greenColor+str(self.__parserState)+self.__defaultColor+">"

    def getLines(self):
        return self.__outputLines

    def readLines(self):
        """Read file and make array of Line"""

        self.__file = open(self.__filename, "r")
        line = self.__file.readline()

        while(line != ""):
            self.__lineCounter += 1
            line = self.__file.readline()
            if(line != "\n"):
                self.__lines.append(line.replace("\n", " "))
                #print(line.replace("\n", " "))
        return self.__lines

    def concatDirectory(self, directory) -> list:
        """Concat string content of folder with file"""
        items = sorted(os.listdir(directory))
        #print(items)

        strOut = []
        for i in items:

            item = directory+"/"+i
            if(isfile(item)):

                tmpFile = open(item, "r")
                
                line = tmpFile.readline()

                while(line != ""):

                    line = tmpFile.readline()
                    if(line != "\n"):
                        strOut.append(line)
        return strOut

    def getGlossary(self):

        return self.__glossary

    def startParser(self, glossary = []):

        self.__parserState = LatexParserStatus(LatexParserStatus.RUNNING)
        lineCounter = 0
        print(self)
        
        count = 0

        parts = os.listdir(self.__partFolder)
        index = 0
        totalLines = 0
        totalImages = 0
        mainHTML = open("HTML_render/index.html", "w+")
        mainHTML.write("<html><head>")
        mainHTML.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
        mainHTML.write("<style></style>")
        mainHTML.write("</head><body style='margin-right:5%;margin-left:5%;margin-top:1%;'><h2>Liste des chapitres générés en HTML</h2><ul>")

        for p in parts:

            outputStrings = []
            subFile = self.concatDirectory(self.__partFolder+"/"+p)
            size = len(subFile)
            count = 0
            self.println("Parsing "+str(p)+" part")
            #Counters
            imgCounter = 0
            counterLine = 0
            maxLines = len(subFile)
            for line in subFile:
                print(">> "+p+" => "+str(round(counterLine*100/maxLines, 1))+" %")
                counterLine+=1
                for c in self.__genericCommands:
                    

                    #self.parse(c, line)
                    result = self.parse(c, line, glossary)

                    flag = c.flag()
                    #print(result)
                    if(result): #prepare next iteration
                        if(flag==c.IMAGE):
                            imgCounter+=1

                        line = result
                        pass
                    else:
                        pass
                count+=1
                if(line=="\n"):
                    pass
                else:
                    outputStrings.append(line)
                lineCounter+=1
          
            #print(">>> Iterations : "+str(count)+" in "+p)
            #print(">>> Images found : "+str(imgCounter))
            totalLines += size
            totalImages += imgCounter
            mainHTML.write("<hr><li> <a href='"+p+".html'>"+p+"</a> <span style='text-align-right' class='badge badge-success float-right'>"+str(size)+" lignes, "+str(imgCounter)+" images</span></li>")
            file = open("HTML_render/"+p+".html", "w")
            file.write("<html><head>")
            file.write('<style>.cent {  display: block;  margin-left: auto;  margin-right: auto;}</style>')
            
            file.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
            file.write('<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"> </script>')
            file.write("<body style='margin-left:5%;margin-right:5%;margin-top:1%'><h4>Fichier générer depuis les sources Latex</h4><h5>Auteur : Nicolas Le Guerroué</h5><a href='index.html'><button class='btn btn-success' >Revenir au sommaire</button></a><hr>")

            for l in outputStrings:
                file.write(l.replace(r"\\", "")+"\n")  #delete \\ in content

            file.write("</body></html>")
            index+=1

        mainHTML.write("</ul><hr><h3>Statistiques</h3><h5>Nombre de lignes : "+str(totalLines)+"</h5><h5>Nombre d'images : "+str(totalImages)+"</h5></body>")

        return outputStrings


    def parse(self, command, content, glossary=[]) -> str:
        """Return str with update content"""

        assert type(command) is Command

        oldContent = copy(content)
        commandType = command.type()
        commandName = command.name()
        oldTemplate = command.oldTemplate()
        replacement = command.replacement()

        argumentsNumber = command.argumentNumber()

        if(commandType == LatexItem.COMMAND):
            regexCommand = r".*\\"+commandName+"*{(.*)\}"
            iteration = 0

            while(re.match(regexCommand, content)):
                iteration+=1
                result = re.compile(r'\{(.+?)}').findall(content)
                for group in result:
                    searched = oldTemplate[0]+group+oldTemplate[1]
                    new = replacement[0]+group+replacement[1]
                    content = content.replace(searched, new)
                if(iteration>=6):
                    self.__flag = LatexItem.COMMAND
                    return content
            if(content==oldContent):
                return None
            else:
                self.__flag = LatexItem.COMMAND
                return r""+content.replace("\n","")

        if(commandType == LatexItem.ANCHOR):  #

            regexCommand = r".*\\"+commandName+"{(.*)\}"
            iteration = 0

            if(re.match(regexCommand, content)):
                iteration+=1
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'\{(.+?)}').findall(content)
                for group in result:
                    searched = oldTemplate[0]+group+oldTemplate[1]
                    new = "<span id='"+group+"'></span>"
                    content = content.replace(searched, new)
                if(iteration>=6):
                    self.__flag = LatexItem.ANCHOR
                    return content
            if(content==oldContent):
                return None
            else:
                self.__flag = LatexItem.ANCHOR
                return r""+content.replace("\n","")

        if(commandType == LatexItem.LINK): 

            regexCommand = r".*\\"+commandName+"{(.*)\}"
            iteration = 0

            if(re.match(regexCommand, content)):
                iteration+=1
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'\{(.+?)}').findall(content)
                for group in result:
                    searched = oldTemplate[0]+group+oldTemplate[1]
                    new = "<a href='#"+group+"'>"+group+"</a>"
                    content = content.replace(searched, new)
                if(iteration>=6):
                    self.__flag = LatexItem.LINK
                    return content
            if(content==oldContent):
                return None
            else:
                self.__flag = LatexItem.LINK
                return r""+content.replace("\n","")


        if(commandType == LatexItem.COLOR):  #Color

            regexCommand = r".*\\"+commandName+"{(.*)\}"
            iteration = 0
            
            while(re.match(regexCommand, content)):
                iteration+=1
                result = re.compile(r'.*'+commandName+r'\{(.+?)}\{(.+?)}').findall(content)
                #print(result)
                for group in result:
                    if(len(group)==2):
                        #print("OK")
                        color=group[0]
                        text=group[1]
                        data = Color.create(color, text)
                        content = content.replace("\\colors{"+color+"}{"+text+"}", data)
                        #print(content)
                self.__flag = LatexItem.COLOR
                return content

        if(commandType == LatexItem.LABEL): 

            regexCommand = r".*\\"+commandName+"{(.*)\}"
            iteration = 0
            
            while(re.match(regexCommand, content)):
                iteration+=1
                result = re.compile(r'.*'+commandName+r'\{(.+?)}\{(.+?)}\{(.+?)}').findall(content)
                #print(result)
                for group in result:
                    if(len(group)==argumentsNumber):
                        #print("OK")
                        color=group[0]
                        id=group[1]
                        text=group[2]
                        data = Label.create(color,color, text)
                        content = content.replace("\\lbl{"+color+"}{"+id+"}{"+text+"}", data)
                        #print(content)
                self.__flag = LatexItem.LABEL
                return content

        if(commandType == LatexItem.PART_IMAGE): 

            regexCommand = r".*\\"+commandName+"{(.*)\}"
            iteration = 0
            
            while(re.match(regexCommand, content)):
                iteration+=1
                result = re.compile(r'.*'+commandName+r'\{(.+?)}\{(.+?)}\{(.+?)}').findall(content)
                #print(result)
                for group in result:
                    if(len(group)==argumentsNumber):
                        #print("OK")
                        color=group[0]
                        id=group[1]
                        text=group[2]
                        content = content.replace("\\"+commandName+"{"+color+"}{"+id+"}{"+text+"}", " ")
                        #print(content)
                self.__flag = LatexItem.PART_IMAGE
                return content

        elif(commandType == LatexItem.FORMULA):

            regexCommand = r".*\$(.*)\$"
            if(re.match(regexCommand, content)):
                #print(">>> MATH found"+content)
                while(re.match(regexCommand, content)):
                
                    result = re.compile(r'\$(.+?)\$').findall(content)
                    #print(result)
                    for r in result:
                        content = content.replace(r, "\("+r+"\)")
                # if(iteration>=6):
                #     return content
                    self.__flag = LatexItem.FORMULA
                    return content.replace("$","")
            if(content==oldContent):
                return None
            else:
                self.__flag = LatexItem.FORMULA
                return r""+content.replace("\n","")


        elif(commandType == LatexItem.INDEX):

            regexCommand = r".*\\"+commandName+"{(.*)\}"

            while(re.match(regexCommand, content)):
            
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'.*\\index'+r'\{(.+?)}').findall(content)
                for group in result:
                    
                    searched = oldTemplate[0]+group+oldTemplate[1]
                    new = " "
                    content = content.replace(searched, new)
            #return content
            if(content==oldContent):
                return None
            else:
                self.__flag = LatexItem.INDEX
                return r""+content.replace("\n","")

        elif(commandType == LatexItem.NEW_COMMAND):

            regexCommand = r".*\\"+commandName+"*{(.*)\}"

            while(re.match(regexCommand, content)):
            
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==2):
                
                    commandExists=False
                    for c in self.__allNewCommands:
                        if commandName in c[0]:
                            commandExists=True
                    if(not commandExists):
                        self.__allNewCommands.append((result[0], result[1]))
                        #print(">>> New command found "+result[0]+" - "+result[1])
                        self.__flag = LatexItem.NEW_COMMAND
                        return content
                else:
                    #print(">>> Bad new command format")
                    pass

        elif(commandType == LatexItem.NEWLINE):

            regexCommand = r".*\\"+commandName+".*"

            while(re.match(regexCommand, content)):
                searched = r"\\"+commandName
                new = "<br>"
                content = content.replace("\\"+commandName, "<br>")
            self.__flag = LatexItem.NEWLINE
            return content

        elif(commandType == LatexItem.COMMENT):

            regexCommand = r".*"+commandName+"(.*)"

            if(re.match(regexCommand, content)):
                result = re.compile( r".*"+commandName+"(.*)").findall(content)
                
                searched = r""+commandName
                content = content.replace(commandName, "")
                content = content.replace(result[0], " ")
            self.__flag = LatexItem.NEWLINE
            return content

        elif(commandType == LatexItem.GLOSSARY):

            regexCommand = r".*\\"+commandName+"*{(.*)\}"

            while(re.match(regexCommand, content)):
            
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'.*'+commandName+r'\{(.+?)}').findall(content)
                if(len(result)==1):
                    searched = oldTemplate[0]+result[0]+oldTemplate[1]
                    for g in glossary:
                        if(len(g)>0):
                            #print(len(g))
                            if g[0][0] == result[0]:
                                gls = g[0]
                                new = "<span title=\""+gls[1]+" : "+gls[2]+"\" style='color:blue;'>"+gls[0]+"</span>"
                                content = content.replace(searched, new)
                        #print(">>> New glossary found "+result[0])
                    self.__flag = LatexItem.GLOSSARY
                    return content
                else:
                    #print(">>> Bad glossary format")
                    pass


        elif(commandType == LatexItem.BEGIN_LIST):

            regexCommand = r".*\\begin\{"+commandName+"\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                #print(">>> Begin List found"+content)
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==argumentsNumber and (commandName in result[0])):
                    self.__flag = LatexItem.BEGIN_LIST

                    return "<ul>"

        elif(commandType == LatexItem.END_LIST):

            regexCommand = r".*\\end\{("+commandName+r")\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                self.__flag = LatexItem.END_LIST
                return "</ul>"

        elif(commandType == LatexItem.ITEM_LIST):

            regexCommand = r".*\\"+commandName+"*(.*)"

            if(re.match(regexCommand, content)):

                #print(">>> Line content found" + content)
                self.__flag = LatexItem.ITEM_LIST
                return content.replace("\\item", "<li>")+"</li>"


        elif(commandType == LatexItem.BEGIN_CODE):

            regexCommand = r".*\\begin\{"+commandName+"\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==argumentsNumber):
                    self.__flag = LatexItem.BEGIN_CODE
                    return "<hr><pre style='background-color:#F5F5F5;padding-left:1em;'><code>"

        elif(commandType == LatexItem.END_CODE):

            regexCommand = r".*end\{"+commandName+r".*\}"
            if(re.match(regexCommand, content)):  #Only one list in line
                if(commandName in content):
                    self.__flag = LatexItem.END_CODE
                    return "</code></pre><hr>"

        elif(commandType == LatexItem.FOOTNOTE):

            regexCommand = r".*\\"+commandName+"*{(.*)\}"

            while(re.match(regexCommand, content)):
            
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'.*'+commandName+r'\{(.+?)}').findall(content)
                if(len(result)==1):
                    searched = oldTemplate[0]+result[0]+oldTemplate[1]
                   
                    #new = "<span title=\""+result[0]+"\" style='color:grey;'><sup>"+""+"[note]</sup></span>"
                    content = content.replace(searched, Footnote(result[0]).create())
                        #print(">>> New glossary found "+result[0])
                    self.__flag = LatexItem.FOOTNOTE
                    return content
                else:
                    #print(">>> Bad glossary format")
                    pass

        elif(commandType == LatexItem.IMAGE):

            regexCommand = r".*\\"+commandName+"(.*)"

            if(re.match(regexCommand, content)):  #Only one list in line
                #print(">>> Begin List found"+content)
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==argumentsNumber):
                    folder = str(result[0])
                    name = folder.split("/")[1]
                    legend = result[1]
                    size = int(float(result[2])*100)

                    folder = Image.findPath(replacement[0], name, "")
                    #print(folder)
                    self.__flag = LatexItem.IMAGE
                    return Image.create(folder.replace(replacement[0], ""), legend, size)

        elif(commandType == LatexItem.MESSAGE_BOX):

            regexCommand = r".*\\"+commandName+r"\{(.*)\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==argumentsNumber): 
                    title = str(result[0])
                    colorframe = result[2]
                    backgroundColor = result[1]
                    text= result[3]
                    data = MessageBox.create(title, backgroundColor,colorframe, text)
                    self.__flag = LatexItem.MESSAGE_BOX
                    return data    
                else:
                    print(">>> MessageBox Error"+content)
                    pass
        elif(commandType == LatexItem.ESCAPE):

            regexCommand = r".*\\"+commandName

            if(re.match(regexCommand, content)):  #Only one list in line

                result = re.compile(r'\{(.+?)}').findall(content)
                searched = r"\_"
                new = " "
                content = content.replace(searched, new)
                return content
        else:
            pass


    # def parse(self, command, line):

    #     assert type(command) is Command

    #     regexSearchCommand = command.name()
    #     print(regexSearchCommand)
        # match = re.match(r".*"+regex.target().keyword(), l)

        #         if(match==None):
        #             #print(l)
        #             pass

        #         while(match):
        #             passed = True


   

        #             elif(regex.replacement().latexItem()==LatexItem.LABEL):

        #                 content = r".*"+regex.target().keyword()+r'{(.+?)}{(.+?)}{(.+?)}'
        #                 result = re.compile(content).findall(l)
        #                 if(result):
        #                     color_fg = str(result[0][0])
        #                     color_bg = str(result[0][1])
        #                     content = str(result[0][2])
                            
        #                     oldContent = regex.target().keyword()+regex.target().target()[0]+result[0][0]+regex.target().target()[1]+regex.target().target()[0]+result[0][1]+regex.target().target()[1]+regex.target().target()[0]+result[0][2]+regex.target().target()[1]
        #                     l = l.replace(oldTemplate[1:], Label.create(color_fg, color_bg, content))

        #                 else:
        #                     break


        #             elif(regex.replacement().latexItem()==LatexItem.NEWLINE):

        #                 break
        #             else:
        #                 match = re.match(r".*"+regex.target().keyword(), l)
        #                 break

        #             #Update match
        #             match = re.match(r".*"+regex.target().keyword(), l)

        #     if(not passed):
        #         l = l.replace("\\", "<br>")
        #         l = l.replace("<br><br>", "<br>")
        #         self.__newLines.append(l)
        #     else:
        #         self.__newLines.append(l)
        #         pass

        mainHTML = open("index.html", "w")
        mainHTML.write("<html><head>")
        mainHTML.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
        mainHTML.write('<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>')

        
        mainHTML.write("<style></style>")
        mainHTML.write("</head><body style='margin-right:5%;margin-left:5%;margin-top:1%;'><h2>Liste des chapitres générés en HTML</h2><ul>")

        # for l in self.__newLines:
        #     #print(l)
        #     mainHTML.write(l+"\n")
