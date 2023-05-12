#!/usr/bin/python
# -*- coding: utf-8 -*-
    
class MessageBox():
    """Create messageBox"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(title, backgroundColor,textColor, text) -> str:
       
        assert type(title) is str
        assert type(textColor) is str
        assert type(backgroundColor) is str
        assert type(text) is str

        alertType = "danger"
        if(backgroundColor=="blue" or backgroundColor=="darkBlue"):
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
