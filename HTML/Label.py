#!/usr/bin/python
# -*- coding: utf-8 -*-
    
class Label():
    """Create label"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(color, content) -> str:
       
        assert type(color) is str
        assert type(content) is str

        return "<span style='background-color:"+color+";opacity:60%;color:white;' class='badge badge-pill'>"+content+"</span>"
