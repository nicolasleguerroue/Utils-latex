# -*- coding: utf-8 -*-
    
from tkinter import CURRENT


class Footnote():
    """Create footnote : Replace " by ' in footnote"""

    COUNTER = 0
    COLOR = "grey"

    def __init__(self, content) -> None:

        Footnote.COUNTER +=1
        self.__content = content
        if("\"" in self.__content):
            self.__content = self.__content.replace("\"", "'")
    def create(self) -> str:

        return "<span title=\""+self.__content+"\" style='color:"+Footnote.COLOR+";'><sup>[Note "+str(Footnote.COUNTER)+"]</sup></span>"

def main():

    d1 = Footnote("\"Footnote1\"").create()
    d2 = Footnote("Footnote2").create()

    file = open("footnote.html", "w")
    file.write(d1+d2)
    file.close()






if(__name__ == "__main__"):

    main()