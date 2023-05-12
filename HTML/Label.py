#!/usr/bin/python
# -*- coding: utf-8 -*-
    
class Label():
    """Create label"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(color_fg, color_bg, content) -> str:
       
        assert type(color_fg) is str
        assert type(color_bg) is str
        assert type(content) is str

        return "<span style='background-color:"+color_bg+";opacity:60%;color:"+color_fg+";' class='badge badge-pill'>"+content+"</span>"
