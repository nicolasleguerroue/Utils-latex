#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import copy
import re
import time
from Command import *
from Glossary import *
from Runtime.Runtime import Runtime
from LatexParser import LatexParser


if(__name__ == "__main__"):

    timer = Runtime()
    timer.start()
    parser = LatexParser("standlone.tex")
    parser.setWorkingDir("Parts", "Images")

    parser.startParser(parser.getGlossary())
    timer.stop()
    print(timer.runtime())
    # parser.addTarget(
    #     RegexTarget(RegexTarget.BETWEEN, r"\\newcommand",["{", "}"], 2),"newCommand", 
    #     RegexReplacement(latexItem=LatexItem.COMMAND, replacement=[["a",RegexReplacement.KEEP, "a"]]))

    # parser.addTarget(
    #     RegexTarget(RegexTarget.BETWEEN, r"\\newline",["{", "}"], 1),"Newline", 
    #     RegexReplacement(latexItem=LatexItem.NEWLINE, replacement=[["",RegexReplacement.KEEP, ""]]))

    # parser.addTarget(
    #     RegexTarget(RegexTarget.BETWEEN, r"\\badge",["{", "}"], 2),"Simple Image", 
    #     RegexReplacement(latexItem=LatexItem.LABEL, replacement=[["",RegexReplacement.KEEP, ""]]))
