import os
import os


class URLHandler():

    def __init__(self, directory):

        self.__lines = []
        self.__lineCounter = 0
        self.__directory = directory

        self.__outputLines = []

        #Read lines
        self.__lines = self.readLines()

    def __str__(self):
        return "<URLHandler.Instance filename='"+self.__filename+"'>"

    def getLines(self):
        return self.__outputLines

    def readLines(self):
        """Read file and make array of Line"""

        os.chdir(self.__directory)
        print(os.getcwd())
        directories = os.listdir(os.getcwd())
        
        for d in directories:
            #print(os.getcwd())
            if(os.path.isdir(d)):
                print(d)
                
                

            # if(not os.path.isdir(d)):
                
            #     print(d)
            #     break
            # else:
            #     os.chdir(d)
            #     files = os.listdir(os.getcwd())
            #     print(d)
            #     #print(files)
            #print(d)
            #os.chdir(d)
            # files = os.listdir(os.getcwd())
            # print(os.getcwd())
            # for f in d:
                
            #     if(".tex" in f):
            #         tmpLines =  []

            #         file = open(f, "r")
            #         line = file.readline().encode("utf-8")

            #         while(line != ""):
            #             self.__lineCounter += 1
            #             line = file.readline()
            #             if(line != "\n"):
            #                 tmpLines.append(line.replace("\n", " "))
            #         self.__lines.append([tmpLines, f])
                    
            #os.chdir("..")
        return self.__lines
    
    def parse(self):

        counter = 0
        commands = []
        for f in self.__lines:
            print(f)
            
            
            
url = URLHandler("Parts")
url.parse()
