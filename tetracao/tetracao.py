from tkinter import CENTER
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


        
        eq_1 = Tex("3\\times 3", "=", "3+3+3")
        eq_2 = Tex("3^{3}", "=", "3\\times 3\\times 3")
        eq_3 = Tex("a+3", "=", "a+1+1+1")
        
        lines_4 = VGroup(
            eq_1,
        )
        lines_4.arrange(DOWN, buff=LARGE_BUFF)
        
        self.wait(4)
        self.play(Write(lines_4))
        
        lines_5 = eq_2
        lines_5.next_to(lines_4, DOWN, buff=0.9)
        
        self.wait(4)
        self.play(TransformFromCopy(lines_4, lines_5))
        
        lines_6 = eq_3
        lines_6.next_to(lines_5, UP, buff=2.3)
        
        self.wait(4)
        self.play(TransformFromCopy(lines_5, lines_6))
        
        self.wait(4)
        self.remove(*self.mobjects)

        inicial = Tex("{^{3}3}" ,"=","3^{3^{3}}")
        self.wait(8)
        self.play(Write(inicial))

        eq_1 = Tex("(3^{3})^{3}")
        eq_2 = Tex("3^{(3^{3})}")

        equacoes = VGroup(
            eq_1,
            eq_2
        )
        equacoes.arrange(DOWN, buff=LARGE_BUFF)
        self.play(TransformFromCopy(inicial, equacoes))
        self.remove(inicial)
        self.wait(4)


        eq_1_2 = Tex("(3^{3})^{3}", "=", "3^{3} \\times 3^{3} \\times 3^{3}")
        eq_2_2 = Tex("3^{(3^{3})}")

        equacoes_2 = VGroup(
            eq_1_2,
            eq_2_2
        )
        equacoes_2.arrange(DOWN, buff=LARGE_BUFF)

        self.play(FadeTransform(equacoes, equacoes_2))
        self.wait(4)

        eq_1_3 = Tex("(3^{3})^{3}", "=", "3^{3+3+3}")
        eq_2_3 = Tex("3^{(3^{3})}")

        equacoes_3 = VGroup(
            eq_1_3,
            eq_2_3
        )
        equacoes_3.arrange(DOWN, buff=LARGE_BUFF)

        self.play(FadeTransform(equacoes_2, equacoes_3))
        self.wait(4)


        eq_1_4 = Tex("(3^{3})^{3}", "=", "3^{3+3+3}", "=", "3^9")
        eq_2_4 = Tex("3^{(3^{3})}")

        equacoes_4 = VGroup(
            eq_1_4,
            eq_2_4
        )
        equacoes_4.arrange(DOWN, buff=LARGE_BUFF)

        self.play(FadeTransform(equacoes_3, equacoes_4))
        self.wait(4)

        eq_1_5 = Tex("(3^{3})^{3}", "=", "3^{3+3+3}", "=", "3^9")
        eq_2_5 = Tex("3^{(3^{3})}", "=", "3^{27}" )

        equacoes_5 = VGroup(
            eq_1_5,
            eq_2_5
        )
        equacoes_5.arrange(DOWN, buff=LARGE_BUFF)

        self.play(FadeTransform(equacoes_4, equacoes_5))
        self.wait(4)

        equacoes_6 = VGroup(
            Tex("{^{3}3}", "=", "3^{(3^{3})}", "=", "3^{27}" )
        )
        equacoes_6.arrange(DOWN, buff=LARGE_BUFF)

        self.play(FadeTransform(equacoes_5, equacoes_6))
        self.wait(9)
        self.remove(*self.mobjects)

        equacoes_7 = VGroup(
            Tex("{^{1}1}", "=", "1" ),
            Tex("{^{2}2}", "=", "2^{2}" ),
            Tex("{^{3}3}", "=", "3^{3^{3}}" ),
            Tex("{^{4}4}", "=", "4^{4^{4^{4}}}" ),
            Tex("{^{5}5}", "=", "5^{5^{5^{5^{5}}}}" ),
            Tex("{^{6}6}", "=", "6^{6^{6^{6^{6^{6}}}}}" ),
            Text("..." ),
            Tex("{^{a}a}", "=", "a^{a^{\\dotsm}}" ),
        )
        equacoes_7.arrange(DOWN, buff=0.3)
        equacoes_7.to_edge(UP, buff=1)
        self.play(Write(equacoes_7))
        self.wait(4)




