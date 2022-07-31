#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import copy
import re
import time
from Command import *
from Glossary import *

import os
from os.path import isfile, join


class Color():

    def __init__(self, latexColor, htmlColor) -> None:
        self.latexColor = latexColor
        self.htmlColor = htmlColor

    

class LatexParser():


    def __init__(self, standlone="../../standlone.tex"):

        self.__file = open(standlone, "r")

        self.__glossary = Glossary("../../Make/Glossaries.tex")
        self.__allNewCommands = []

        self.__lineCounter = 0
        self.__lines = []

        self.__genericCommands = [
            Command("bold", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("textbf", 1, Command.COMMAND, ["<b>", "</b>"]),
            Command("textit", 1, Command.COMMAND, ["<u>", "</u>"]),
            Command("italic", 1, Command.COMMAND, ["<i>", "</i>"]),
            Command("emph", 1, Command.COMMAND, ["<i>", "</i>"]),
            Command("underline", 1, Command.COMMAND, ["<u>", "</u>"]),
            Command("ib", 1, Command.COMMAND, ["<b><i>", "</i></b>"]),
            Command("bi", 1, Command.COMMAND, ["<b><i>", "</i></b>"]),
            Command("url", 1, Command.COMMAND, ["<a class=\"alert-link\">", "</a>"]),
            Command("link", 1, Command.COMMAND, ["<a class=\"alert-link\">", "</a>"]),
            Command("nameref", 1, Command.LINK, ["<a href='#url'>", "</a>"]),
            Command("label", 1, Command.ANCHOR, ["<a href='#url'>", "</a>"]),
            Command("file", 1, Command.COMMAND, ["<span class='badge badge-primary'>", "</span>"]),
            Command("loc", 1, Command.COMMAND, ["</br><span class='badge badge-info'>", "</span><br>"]),
            Command("dir", 1, Command.COMMAND, ["<span class='badge badge-light'>", "</span>"]),
            Command("lib", 1, Command.COMMAND, ["<span class='badge badge-success'>", "</span>"]),
            Command("shortcut", 1, Command.COMMAND, ["<span class='badge badge-light'>", "</span>"]),
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

            Command("index", 1, Command.INDEX, []), #Delete Index
            #Command("$$", 1, Command.FORMULA, ["\$", "\$"]),
            Command("\$", 1, Command.FORMULA, ["\\(", "\\)"]),
            Command("newcommand", 2, Command.NEW_COMMAND, ["", ""]),
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

            Command("img", 3, Command.IMAGE, ["../../Images"]),
            Command("imgn", 4, Command.IMAGE, ["../../Images"]),
            Command("imgf", 4, Command.IMAGE, ["../../Images"]),
            Command("messageBox", 5, Command.MESSAGE_BOX, ["", ""]),
            Command("lbl", 3, Command.LABEL, ["", ""]),
            Command("index", 1, Command.INDEX, ["", ""]),
            Command("partImg", 3, Command.PART_IMAGE, ["", ""]),
            Command("_", 0, Command.ESCAPE, ["", ""]),
            Command("%#", 0, Command.COMMENT, ["", ""])

        ]      

        line = self.__file.readline()

        self.__glossaries = self.__glossary.parse()

        while(line != ""):

            self.__lineCounter += 1
            line = self.__file.readline()
            if(line != "\n"):
                self.__lines.append(line)
        #print(">>> "+str(self.__lineCounter)+" lines ")

    def setWorkingDir(self, partFolder, imgFolder):

        self.__partFolder = partFolder
        self.__imgFolder = imgFolder

    def setHeader(self):

        self.__header = """
        <html>
        <head>
        </head>
        """

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

    def parse(self):

        lineCounter = 0

        
        count = 0

        parts = os.listdir(self.__partFolder)
        index = 0
        totalLines = 0
        totalImages = 0
        mainHTML = open("HTML_render/index.html", "w")
        mainHTML.write("<html><head>")
        mainHTML.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
        mainHTML.write("<style></style>")
        mainHTML.write("</head><body style='margin-right:5%;margin-left:5%;margin-top:1%;'><h2>Liste des chapitres générés en HTML</h2><ul>")

        for p in parts:

            outputStrings = []
            subFile = self.concatDirectory(self.__partFolder+"/"+p)
            size = len(subFile)
            count = 0

            #Counters
            imgCounter = 0
            for line in subFile:
                for c in self.__genericCommands:
                    result = c.parse(line, self.__glossaries)
                    flag = c.flag()



                    if(result): #prepare next iteration
                        if(flag==c.IMAGE):
                            imgCounter+=1

                        line = result
                        pass
                    else:
                        pass
                        #print("FAIL")
                        #print(line)
                count+=1
                if(line=="\n"):
                    pass
                else:
                    outputStrings.append(line)
                lineCounter+=1
          
            #print(">>> Iterations : "+str(count)+" in "+p)
            print(">>> Images found : "+str(imgCounter))
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


if(__name__ == "__main__"):

    parser = LatexParser()

    startTime = time.time()
    Image.checkDoublons("../../Images")
    parser.setWorkingDir("../../Parts", "../../Images")
    data = parser.parse()
    print(">>> Parsed in "+str(time.time()-startTime)+" s")
