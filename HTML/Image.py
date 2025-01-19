#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from genericpath import isdir, isfile

class Image():
    """Create Image"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(path, legend, size, indexImage=0, figureRef="", wordpress=False) -> str:
       
        assert type(path) is str, "Expected <str>, given <"+str(type(path))+">"
        assert type(legend) is str, "Expected <str>, given <"+str(type(legend))+">"
        assert type(indexImage) is int, "Expected <int>, given <"+str(type(indexImage))+">"
        assert type(figureRef) is str, "Expected <str>, given <"+str(type(figureRef))+">"

        if(wordpress==True): #Path is image/name
            return "<figure id='"+figureRef+"'><div class='cent' style='text-align:center;'><a href='http://www.crepp.org/wp-content/uploads/2022/08/"+path+"'><img src='http://www.crepp.org/wp-content/uploads/2022/08/"+path+"' class='alignnone size-medium' style='max-width:"+str(size)+"%;'></a><figcaption>Figure - "+legend+"</figcaption></div></figure>"
        else:
            return "<figure id='"+figureRef+"'><div class='cent' style='text-align:center;'><img src='"+path+"' class='alignnone size-medium' style='max-width:"+str(size)+"%;'><figcaption>Figure - "+legend+"</figcaption></div></figure>"
   
    @staticmethod
    def findPath(srcImage, imageName, prefixFolder="../") -> str:
       
        assert type(srcImage) is str, "Expected <str>, given <"+str(type(srcImage))+">"
        assert type(imageName) is str, "Expected <str>, given <"+str(type(imageName))+">"

        for d in sorted(os.listdir(srcImage)):
            if(isdir(srcImage+"/"+d)):
                for d2 in  sorted(os.listdir(srcImage+"/"+d)):
                    if(imageName==d2):
                        return (prefixFolder+srcImage+"/"+d+"/"+d2)#.replace(d+"/", "")
        return "empty"

    @staticmethod
    def checkDoublons(imgsDir) -> str:
       
        assert type(imgsDir) is str, "Expected <str>, given <"+str(type(imgsDir))+">"

        allNames = []

        for d in sorted(os.listdir(imgsDir)):

            if(isdir(imgsDir+"/"+d)):
                   for d2 in  sorted(os.listdir(imgsDir+"/"+d)):
                        if(d2 in allNames):
                            print("In >>> "+d)
                            print(">>> Double image found : "+str(d2))
                        else:
                            allNames.append(d2)
        return "empty"