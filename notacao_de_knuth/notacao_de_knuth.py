from tkinter import CENTER, W
from manimlib import *
import numpy as np

class Cancel(VGroup):
    CONFIG = {
        "line_kwargs": {"color":RED},
        "buff_text": None,
        "buff_line": 0,
        "camera_qualities": "high"
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
        self.scene2()
        self.scene3()
        self.scene4()
        self.scene5()
        self.scene6()

    
    def scene1(self):
        eq_1 = Tex("a \\uparrow b", "=", "a^{b}")
        eq_2 = Tex("a[3]b", "=", "a^{b}")
        eq_3 = Tex("a \\rightarrow b \\rightarrow 3", "=", "a^{b}")
        
        lines_4 = VGroup(
            eq_1,
            eq_2,
            eq_3
        )
        lines_4.arrange(DOWN, buff=LARGE_BUFF)
        
        self.wait(4)
        self.play(Write(lines_4))

        self.wait(4)

        eq_1_2 = Tex("a \\uparrow 3", "=", "a^{3}")
        eq_2_2 = Tex("a \\uparrow\\uparrow  3", "=", "{^{3}a}")
        eq_3_2 = Tex("a \\uparrow\\uparrow\\uparrow 3", "=", "{^{^{a}a}a}")

        lines_5 = VGroup(
            eq_1_2,
            eq_2_2,
            eq_3_2
        )
        lines_5.arrange(DOWN, buff=0.6)
        self.play(FadeTransform(lines_4, lines_5))

        eq_1_3 = Tex("a \\uparrow 3", "=", "a^{3}")
        eq_2_3 = Tex("a \\uparrow^{2} 3", "=", "{^{3}a}")
        eq_3_3 = Tex("a \\uparrow^{3} 3", "=", "a \\uparrow^{2} a \\uparrow^{2} a")
        eq_4_3 = Tex("a \\uparrow^{4}  3", "=", "a \\uparrow^{3} a \\uparrow^{3}  a")
        eq_5_3 = Tex("a \\uparrow^{5}  3", "=", "a \\uparrow^{4} a \\uparrow^{4}  a")

        self.wait(1)
        lines_6_1 = VGroup(
            eq_1_3
        )
        lines_6_1.arrange(DOWN, buff=0.6)
        lines_6_1.to_edge(UP)
        self.play(FadeTransform(lines_5, lines_6_1))

        lines_6_1_1 = eq_2_3
        lines_6_1_1.next_to(lines_6_1, DOWN, buff=0.6)
        self.play(TransformFromCopy(lines_6_1, lines_6_1_1))
        self.wait(1)

        lines_6_2 = eq_3_3
        lines_6_2.next_to(lines_6_1_1, DOWN, buff=0.6)
        self.play(TransformFromCopy(lines_6_1_1, lines_6_2))
        self.wait(1)

        lines_6_3 = eq_4_3
        lines_6_3.next_to(lines_6_2, DOWN, buff=0.6)
        self.play(TransformFromCopy(lines_6_2, lines_6_3))
        self.wait(1)

        lines_6_4 = eq_5_3
        lines_6_4.next_to(lines_6_3, DOWN, buff=0.6)
        self.play(TransformFromCopy(lines_6_3, lines_6_4))
        self.wait(2)
        self.remove(*self.mobjects)


    def scene2(self):
        txt = Text("Caso de uso.:")
        eq_1_2 = Tex("2 \\uparrow^{3} 3", "=", "2 \\uparrow^{2} 2 \\uparrow^{2} 2") 
        eq_1_2_1 = Tex("2 \\uparrow^{3} 3", "=", "2 \\uparrow^{2} (2 \\uparrow^{2} 2)") 
        eq_1_3 = Tex("2 \\uparrow^{2} 2", "=", "2 \\uparrow 2")
        eq_1_3_1 = Tex("2 \\uparrow^{2} 2", "=", "4")
        eq_1_3_2 = Tex("2 \\uparrow^{2} 2", "=", "4")
        eq_1_2_2 = Tex("2 \\uparrow^{3} 3", "=", "2 \\uparrow^{2} 4") 
        eq_1_2_3 = Tex("2 \\uparrow^{3} 3", "=", "2 \\uparrow 2 \\uparrow 2 \\uparrow 2") 
        eq_1_4 = Tex("{{{2^{2}}^2}^2}", "=", "256") 

        lines_7 = VGroup(
            txt
        )
        lines_7.to_edge(UP)
        self.play(Write(lines_7))
        self.wait(2)

        lines_7_1 = eq_1_2
        lines_7_1.next_to(lines_7, DOWN, buff=0.6)
        self.play(TransformFromCopy(lines_7, lines_7_1))
        self.wait(1)

        lines_7_1_1 = eq_1_2_1
        lines_7_1_1.next_to(lines_7, DOWN, buff=0.6)
        self.play(ReplacementTransform(lines_7_1, lines_7_1_1))
        self.wait(1)
        
        lines_7_2 = eq_1_3
        lines_7_2.next_to(lines_7_1_1, DOWN, buff=0.6)
        self.play(TransformFromCopy(lines_7_1_1, lines_7_2))
        self.wait(1)

        lines_7_2_1 = eq_1_3_1
        lines_7_2_1.next_to(lines_7_1_1, DOWN, buff=0.6)
        self.play(ReplacementTransform(lines_7_2, lines_7_2_1))
        self.wait(1)

        lines_7_2_2 = eq_1_3_2
        lines_7_2_2.next_to(lines_7_1_1, DOWN, buff=0.6)
        self.play(ReplacementTransform(lines_7_2_1, lines_7_2_2))
        self.wait(1)

        self.remove(lines_7_2_2)
        
        lines_7_1_2 = eq_1_2_2
        lines_7_1_2.next_to(lines_7, DOWN, buff=0.6)
        self.play(ReplacementTransform(lines_7_1_1, lines_7_1_2))
        self.wait(1)

        lines_7_1_3 = eq_1_2_3
        lines_7_1_3.next_to(lines_7, DOWN, buff=0.6)
        self.play(ReplacementTransform(lines_7_1_2, lines_7_1_3))
        self.wait(1)
        
        lines_7_1_4 = eq_1_4
        lines_7_1_4.next_to(lines_7_1_3, DOWN, buff=1.5)
        self.play(ReplacementTransform(lines_7_1_3, lines_7_1_4))
        self.wait(1)
        self.remove(*self.mobjects)

    def scene3(self):
        txt = Text("Notação de colchetes.:")
        eq_1_2 = Tex("a [0] b", "=", "b + 1") 
        eq_1_3 = Tex("a [1] b", "=", "a + b")
        eq_1_4 = Tex("a [2] b", "=", "a \\times b")
        eq_1_5 = Tex("a [3] b", "=", "a^{b}")
        eq_1_6 = Tex("a [4] b", "=", "{^{b}a}")
        lines_1 = VGroup(
            txt,
            eq_1_2,
            eq_1_3,
            eq_1_4,
            eq_1_5,
            eq_1_6
        )
        lines_1.to_edge(UP)
        lines_1.arrange(DOWN, buff=0.5)
        self.play(Write(lines_1))
        self.wait(2)


    def scene4(self):
        txt = Text("Notação de colchetes.:")
        eq_1_2 = Tex("a [0] b", "=", "b + 1") 
        eq_1_3 = Tex("a [1] b", "=", "a + b")
        eq_1_4 = Tex("a [2] b", "=", "a \\times b")
        eq_1_5 = Tex("a [3] b", "=", "a^{b}")
        eq_1_6 = Tex("a [4] b", "=", "{^{b}a}")
        lines_1 = VGroup(
            txt,
            eq_1_2,
            eq_1_3,
            eq_1_4,
            eq_1_5,
            eq_1_6
        )
        lines_1.to_edge(UP)
        lines_1.arrange(DOWN, buff=0.5)
        self.play(Write(lines_1))
        self.wait(2)
        self.remove(*self.mobjects)

    def scene5(self):
        txt = Text("Definição comum de hiperoperadores.:")
        eq_1_2 = Tex("H_n(m, n, p) = \\begin{cases}  b + 1 & n = 0 \\\\ a & n = 1, b = 0 \\\\ 0 & n = 2, b = 0 \\\\ 1 & n \\ge 3 , b = 0 \\\\ H_{n-1}(a, H_n(a, b - 1)) & n \\ge 0, b \\neq 0  \\end{cases}") 
        lines_1 = VGroup(
            txt,
            eq_1_2
        )
        lines_1.to_edge(UP)
        lines_1.arrange(DOWN, buff=0.5)
        self.play(Write(lines_1))
        self.wait(2)
        self.remove(*self.mobjects)

    def scene6(self):
        txt = Text("Definição da função de Ackermann.:")
        eq_1_2 = Tex("\\phi(n, m, p)  = \\begin{cases}  m + n & p = 0 \\\\ 0 & p = 1, n = 0 \\\\ 1 & p = 2, n = 0 \\\\ m & n \\ge 3 , p = 0 \\\\ H_{n-1}(a, H_n(a, b - 1)) & n \\ge 0, b \\neq 0  \\end{cases}") 
        lines_1 = VGroup(
            txt,
            eq_1_2
        )
        lines_1.to_edge(UP)
        lines_1.arrange(DOWN, buff=0.5)
        self.play(Write(lines_1))
        self.wait(2)

        eq_1_2 = Tex("A(n, m)  = \\begin{cases}  n + 1 & m = 0 \\\\ (2\\uparrow^{m-2}(n+3))-3  & m > 0 \\end{cases}")
        lines_2 = VGroup(
            txt,
            eq_1_2
        )
        lines_2.to_edge(UP)
        lines_2.arrange(DOWN, buff=0.5)
        self.play(ReplacementTransform(lines_1, lines_2))
        self.wait(2)






