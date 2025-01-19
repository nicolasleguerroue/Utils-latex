# -*- coding: utf-8 -*-

class LatexContentType():

    TEXT = 0
    CODE = 1

    def __init__(self, type=TEXT):
        self.type = type

class LatexParserStatus():

    RUNNING = 0
    STOPPED = 1

    STATUS_AVAILABLE = ["RUNNING", "STOPPED"]

    def __init__(self, status=STOPPED):
        self.status = status

    def __str__(self):
        return str(LatexParserStatus.STATUS_AVAILABLE[self.status])


class LatexItem():
    """Create generic command"""

    """Flags"""
    COMMAND = 1         #Bold, italic...
    ENVIRONMENT = 2     #Environnement
    FORMULA = 3         #Formula
    INDEX = 4           #Index 
    FOOTNOTE = 5        #Footnote -> use Footnote.py
    NEW_COMMAND = 6     #Specific command
    GLOSSARY = 7        #Glossary

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

