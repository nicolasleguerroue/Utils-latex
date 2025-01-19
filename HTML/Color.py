#!/usr/bin/python
# -*- coding: utf-8 -*-
    
class Color():
    """Create Color"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(color, content) -> str:
       
        assert type(color) is str
        assert type(content) is str

        return "<span style='color:"+color+";'>"+content+"</span>"
