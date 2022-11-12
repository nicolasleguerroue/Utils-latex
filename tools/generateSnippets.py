# -*- coding: utf-8 -*-
import re
import time
import os


class Command():

    NEWCOMMAND = 0
    ENVIRONMENT = 1
    THEOREM = 1

    def __init__(self, name, description, args=[], type=NEWCOMMAND, file=""):

        self.__name = name
        self.__description = description
        self.__args = args
        self.__type = type
        self.__file = file

    def __str__(self):

        return "<Command : "+self.__name+" des='"+self.__description+"'>"

    def type(self):
        return self.__type

    def create(self):

        if(self.__description==""):
            return None
        content = ""
        if(self.__type == Command.NEWCOMMAND):
            content += "\""+self.__description+"\": {\n"
            content += "\t \"scope\" : \"tex, latex\",\n"
            content += "\t \"prefix\" : \"Latex."+self.__file.replace(".sty", "")+"."+self.__name+"\",\n"
            content += "\t \"body\" : [\n"
            content += "\t \"\\\\"+self.__name
            c=1
            for a in self.__args:
                content += "{${"+str(c)+":"+a+"}}"
                c+=1
            content += "\"\n\t ], \n"
            content += "\t \"description\" : \""+self.__description+"\",\n"
            content += "},\n"
            return content

        elif(self.__type == Command.ENVIRONMENT):
            content += "\""+self.__description+"\": {\n"
            content += "\t \"scope\" : \"tex, latex\",\n"
            content += "\t \"prefix\" : \"Latex."+self.__file.replace(".sty", "")+"."+self.__name+"\",\n"
            content += "\t \"body\" : [\n"
            content += "\t \"\\\\begin{"+self.__name+"}"
            c=1

            if("tabular" in self.__name or "Array" in self.__name):
                if(len(self.__args)==1):
                    content += "{|c|c|c|}\\\\hline"
            else:
                for a in self.__args:
                    content += "{${"+str(c)+":"+a+"}}"
                    c+=1
            if("items" in self.__name or "List" in self.__name or "itemize" in self.__name or "enumerate" in self.__name):
                content += "\\n\\\\item\\n\\\\item"
            if("tabular" in self.__name or "Array" in self.__name):
                content += "\\n Header1 & Header2 & header"+r"\\"+r"\\\\"+" \\\\hline"+r"\n"
                content += "A & B & C"+r"\\"+r"\\\\"+r"\n"
                content += "D & E & F"+r"\\"+r"\\\\"+" \\\\hline"
            content += "\\n\\\\end{"+self.__name+"}\"\t \n], \n"
            content += "\t \"description\" : \""+self.__description+"\",\n"
            content += "},\n"
            return content
        return ""

class Snippet():

    def __init__(self, directory):

        self.__lines = []
        self.__lineCounter = 0
        self.__directory = directory

        self.__outputLines = []

        #Read lines
        self.__lines = self.readLines()

    def __str__(self):
        return "<Snippet.Instance filename='"+self.__filename+"'>"

    def getLines(self):
        return self.__outputLines

    def readLines(self):
        """Read file and make array of Line"""


        os.chdir(self.__directory)
        files = os.listdir(os.getcwd())
        for f in files:
            
            if(".sty" in f):
                tmpLines =  []

                file = open(f, "r")
                line = file.readline().encode("utf-8")

                while(line != ""):
                    self.__lineCounter += 1
                    line = file.readline()
                    if(line != "\n"):
                        tmpLines.append(line.replace("\n", " "))
                self.__lines.append([tmpLines, f])
        return self.__lines

    def __getName(self, l):

        name = l.split("{")[1].split("}")[0]
        if(name[0]=="\\"):
            return name[1:]
        else:
            return name

    def __getDescription(self, l):
        if("%" in l):
            return l.split("%")[1].split("#")[0]
        return ""

    def __getArgs(self, l):

        if("%" in l and "#" in l):
            return l.split("#")[1].split()
        else:
            return {}


    def parse(self, output):

        counter = 0
        commands = []
        for f in self.__lines:
            
            for l in f[0]:

                filename = f[1]
                #New Command
                if("newcommand" in l):

                    commands.append(Command(self.__getName(l), self.__getDescription(l), self.__getArgs(l), Command.NEWCOMMAND, filename))
                    counter+=1
                    
                elif("newtheorem" in l):
                    counter += 1
                    commands.append(Command(self.__getName(l), self.__getDescription(l),  self.__getArgs(l), Command.THEOREM, filename))

                elif("newcommand" in l):
                    counter += 1
                    commands.append(Command(self.__getName(l), self.__getDescription(l),  self.__getArgs(l), Command.NEWCOMMAND, filename))

                elif("newtcbox" in l):
                    counter += 1
                    commands.append(Command(self.__getName(l), self.__getDescription(l),  self.__getArgs(l), Command.NEWCOMMAND, filename))


                elif("newenvironment" in l):
                    counter += 1
                    commands.append(Command(self.__getName(l), self.__getDescription(l),  self.__getArgs(l), Command.ENVIRONMENT, filename))

        print("Command Counter : "+str(counter))

        data = "{\n"
        for c in commands:
            r = c.create()
            if(r):
                data+=r
        data+="\n}"
        ofile = open(output, "w")
        ofile.write(data)
        ofile.close()

  

parser = Snippet("Utils")
parser.parse("../.vscode/output.code-snippets")
