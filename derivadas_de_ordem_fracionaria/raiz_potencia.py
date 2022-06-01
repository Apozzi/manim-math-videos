from manimlib import *
import numpy as np

class Cancel(VGroup):
    CONFIG = {
        "line_kwargs": {"color":RED},
        "buff_text": None,
        "buff_line": 0,
    }
    def __init__(self,text,texmob=None,**kwargs):
        digest_config(self,kwargs)
        VGroup.__init__(self,**kwargs)

        pre_coord_dl = text.get_corner(DL)
        pre_coord_ur = text.get_corner(UR)
        reference_line = Line(pre_coord_dl,pre_coord_ur)
        reference_unit_vector = reference_line.get_unit_vector()
        coord_dl = text.get_corner(DL) - text.get_center() - reference_unit_vector*self.buff_line
        coord_ur = text.get_corner(UR) - text.get_center() + reference_unit_vector*self.buff_line
        self.add(text)
        if texmob == None:
            line = Line(coord_dl,coord_ur,**self.line_kwargs)
            self.add(line)
        else:
            arrow = Arrow(coord_dl,coord_ur,**self.line_kwargs)
            unit_vector = arrow.get_unit_vector()
            if self.buff_text == None:
                self.buff_text = get_norm((texmob.get_center()-texmob.get_critical_point(unit_vector))/2)*2
            texmob.move_to(arrow.get_end()+unit_vector*self.buff_text)
            self.add(arrow,texmob)


class Main(Scene):
    def construct(self):     
        self.scene1()
    
    def scene1(self):

 
        lines_1 = VGroup(
            Tex("{\sqrt{x}}^2"),
        )
        lines_1.arrange(DOWN, buff=LARGE_BUFF)
        
        self.play(Write(lines_1))
        self.wait(2)
        


        
        
        