#!/usr/bin/python
# -*- coding: utf-8 -*-
    
class MessageBox():
    """Create messageBox"""

    def __init__(self, title, textColor, backgroundColor, text) -> None:
        pass

    @staticmethod
    def create(title, backgroundColor,textColor, text) -> str:
       
        assert type(title) is str
        assert type(textColor) is str
        assert type(backgroundColor) is str
        assert type(text) is str

        alertType = "danger"
        print(backgroundColor)
        if(backgroundColor=="blue"):
            alertType="primary"
        elif(backgroundColor=="red"):
            alertType="danger"
        elif(backgroundColor=="green"):
            alertType="success"
        elif(backgroundColor=="orange"):
            alertType="warning"
        else:
            pass

        return "<div class='alert alert-"+alertType+"' ><h4>"+title+"</h4>"+text+"</div>"

    def name(self):
        return self.__name

    def parse(self, content) -> str:
        """Return str with update content"""

        oldContent = copy(content)

        if(self.__type == self.COMMAND):

            regexCommand = r".*\\"+self.__name+"*{(.*)\}"
            iteration = 0

            while(re.match(regexCommand, content)):
                iteration+=1
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'\{(.+?)}').findall(content)
                for group in result:
                    searched = self.__oldTemplate[0]+group+self.__oldTemplate[1]
                    new = self.__replacement[0]+group+self.__replacement[1]
                    content = content.replace(searched, new)
                if(iteration>=6):
                    return content
            if(content==oldContent):
                return None
            else:
                return r""+content.replace("\n","")

        elif(self.__type == self.FORMULA):

            regexCommand = r".*\$(.*)\$"
            if(re.match(regexCommand, content)):
                return content
        elif(self.__type == self.INDEX):

            regexCommand = r".*\\"+self.__name+r"*{(.*)\}"

            while(re.match(regexCommand, content)):
            
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'.*\\index'+r'\{(.+?)}').findall(content)
                for group in result:
                    searched = self.__oldTemplate[0]+group+self.__oldTemplate[1]
                    new = ""
                    content = content.replace(searched, new)
            #return content
            if(content==oldContent):
                return None
            else:
                return r""+content.replace("\n","")

        elif(self.__type == self.NEW_COMMAND):

            regexCommand = r".*\\"+self.__name+"*{(.*)\}"

            while(re.match(regexCommand, content)):
            
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==2):
                
                    commandExists=False
                    for c in self.__allNewCommands:
                        if self.__name in c[0]:
                            commandExists=True
                    if(not commandExists):
                        self.__allNewCommands.append((result[0], result[1]))
                        print(">>> New command found "+result[0]+" - "+result[1])
                        return content
                else:
                    #print(">>> Bad new command format")
                    pass

        elif(self.__type == self.NEWLINE):

            regexCommand = r".*\\"+self.__name+".*"

            while(re.match(regexCommand, content)):
                searched = r"\\"+self.__name
                new = "<br>"
                content = content.replace("\\"+self.__name, "<br>")

            return content

        elif(self.__type == self.GLOSSARY):

            regexCommand = r".*\\"+self.__name+"*{(.*)\}"

            while(re.match(regexCommand, content)):
            
                #print("Match : "+content+ " = "+content+"")
                result = re.compile(r'.*'+self.__name+r'\{(.+?)}').findall(content)
                if(len(result)==1):
                
                    commandExists=False
                    for c in self.__allNewCommands:
                        if self.__name in c[0]:
                            commandExists=True
                    if(not commandExists):

                        for group in result:
                            searched = self.__oldTemplate[0]+group+self.__oldTemplate[1]
                            new = "<a href='#de'>"+group+"</a>"
                            content = content.replace(searched, new)

                        self.__allNewGlossaries.append((result[0]))
                        #print(">>> New glossary found "+result[0])
                        return content
                else:
                    #print(">>> Bad glossary format")
                    pass

        elif(self.__type == self.FOOTNOTE):

            regexCommand = r".*\\"+self.__name+"*{(.*)\}"
            iterration = 0
            while(re.match(regexCommand, content)):
                iterration+=1
                #print(content)
                result = re.compile(r'\{(.+?)}').findall(content)
                #print(len(result))
                if(len(result)==1):
                    commandExists=False
                    for c in self.__allNewFootnotes:
                        if self.__name in c[0]:
                            commandExists=True
                    if(not commandExists):
                        self.__allNewFootnotes.append((result[0]))
                        #print(">>> New footnote found "+result[0])
                        return 
                else:
                    #print(">>> Bad format for footnote"+content)
                    if(iterration>=6):
                        return 

        elif(self.__type == self.BEGIN_LIST):

            regexCommand = r".*\\begin{(.*)\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                #print(">>> Begin List found"+content)
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==3 and (self.__name in result[0])):
                    color = result[1]
                    form = result[2]
                    #print(">>> color="+color+" - "+form)
                    return "<ul>"

        elif(self.__type == self.END_LIST):

            regexCommand = r".*\\end{(.*)\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                return "</ul>"

        elif(self.__type == self.ITEM_LIST):

            regexCommand = r".*\\"+self.__name+"*(.*)"

            if(re.match(regexCommand, content)):

                #print(">>> Line content found" + content)

                return content.replace("\\item", "<li>")+"</li>"


        elif(self.__type == self.BEGIN_CODE):

            regexCommand = r".*\\begin\{Cpp\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                #print(">>> Begin List found"+content)
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==3 and (self.__name in result[0])):
                    color = result[1]
                    form = result[2]
                    #print(">>> color="+color+" - "+form)
                    return "<ul>"

        elif(self.__type == self.IMAGE):

            regexCommand = r".*\\"+self.__name+"(.*)"

            if(re.match(regexCommand, content)):  #Only one list in line
                #print(">>> Begin List found"+content)
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==self.__argumentsNumber):
                    folder = str(result[0])
                    name = folder.split("/")[1]
                    legend = result[1]
                    size = int(float(result[2])*100)
                    #print(">>> folder="+folder+" - legend = "+legend+" - size = "+str(size))
                    folder = ""
                    for d in sorted(os.listdir("../Images")):
                        #print(">>> scan of "+d)
                        if(isdir("../Images/"+d)):
                            for d2 in  sorted(os.listdir("../Images/"+d)):
                                #print(">>> scan of "+d2)
                                if(name==d2):
                                    folder="../../Images"+"/"+d+"/"+d2
                    data = "<figure><div class='cent' style='text-align:center;'><img src='"+folder+"' style='max-width:"+str(size)+"%;'><figcaption>Figure - "+legend+"</figcaption><br></div></figure>"
                    #print(data)
                    return data

        elif(self.__type == self.MESSAGE_BOX):

            regexCommand = r".*\\"+self.__name+r"\{(.*)\}"

            if(re.match(regexCommand, content)):  #Only one list in line
                print(">>> Begin messageBox found"+content)
                result = re.compile(r'\{(.+?)}').findall(content)
                if(len(result)==self.__argumentsNumber): 
                    title = str(result[0])
                    colorframe = result[1]
                    backgroundColor = result[2]
                    text= result[3]
                    print(text)
                    data = "<div class='alert alert-primary' >"+text+"</div>"
                    #print(data)
                    return data    
                else:
                    pass
        else:
            pass

    def exportNewCommand(self):

        if(len(self.__allNewCommands)>=1):
            return self.__allNewCommands[0]

    def replaceShortcut(self, line):
        """Replace new command expression"""


    def footnotes(self):
        return self.__allNewFootnotes