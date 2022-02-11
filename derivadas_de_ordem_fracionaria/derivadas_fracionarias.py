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
        self.scene13()
    
    def scene1(self):
        intro_words = Text("""
            Eu voltei... 
        """)


        self.play(Write(intro_words))
        self.wait(2)
        
        frase = VGroup(Tex("f"), Text("é repetido n vezes."))
        frase.arrange(RIGHT)
        lines_1 = VGroup(
            Text("Funções iteradas:"),
            Tex("f^n", "=", "f(f(f(...f()...)))"),
            frase,
        )
        lines_1.arrange(DOWN, buff=LARGE_BUFF)
        
        self.play(FadeTransform(intro_words, lines_1))
        self.wait(2)
        
        frase = VGroup(Tex("f^{-1}(x)", "=", "\sqrt{x}"), Text("se"), Tex("x\geq0"))
        frase.arrange(RIGHT)
        lines_2 = VGroup(
            Text("Pode definição temos funções inversas"),
            Text("Por exemplos se:"),
            Tex("f(x)", "=", "x^2"),
            Text("Sabemos que inversa do potencia quadrada é a raiz:"),
            frase,
        )
        lines_2.arrange(DOWN, buff=LARGE_BUFF)
        
        self.play(FadeTransform(lines_1, lines_2))
        self.wait(2)
           
        frase = VGroup(Text("Podemos aplicar"), Tex("f(x)"), Text("e"), Tex("f(f(x))"), Text("continuamente..."))
        frase.arrange(RIGHT)
        lines_3 = VGroup(
            Text("Em uma função iterativa é possivel descobrir formula por meio de indução!"),
            frase,
            Text("Da mesma forma podemos fazer isso com derivadas!")
        )
        lines_3.arrange(DOWN, buff=LARGE_BUFF)
        
        self.play(FadeTransform(lines_2, lines_3))
        
        eq_1 = Tex("f(x)", "=", "x^k")
        eq_2 = Tex("f'(x)", "=", "kx^{k-1}")
        eq_3 = Tex("f''(x)", "=", "k(k-1)x^{k-2}")
        eq_4 = Tex("f^n(x)", "=", "\\frac{k!}{(k-n)!}x^{k-n}")
        
        lines_4 = VGroup(
            eq_1,
        )
        lines_4.arrange(DOWN, buff=LARGE_BUFF)
        lines_4.to_edge(UP)
        
        self.wait(2)
        self.play(FadeTransform(lines_3, lines_4))
        
        lines_5 = eq_2
        lines_5.next_to(lines_4, DOWN, buff=0.2)
        
        self.wait(2)
        self.play(TransformFromCopy(lines_4, lines_5))
        
        lines_6 = eq_3
        lines_6.next_to(lines_5, DOWN, buff=0.2)
        
        self.wait(2)
        self.play(TransformFromCopy(lines_5, lines_6))
        
        lines_7 = Text("...")
        lines_7.next_to(lines_6, DOWN, buff=0.5)
        
        self.wait(2)
        self.play(TransformFromCopy(lines_6, lines_7))
        
        lines_8 = eq_4
        lines_8.next_to(lines_7, DOWN, buff=0.5)
        
        self.wait(2)
        self.play(TransformFromCopy(lines_7, lines_8))
        
        self.wait(2)
        self.remove(*self.mobjects)
        
    def scene2(self):
        l_1 = Text("Revisando propriedades dos fatoriais:")
        l_1.to_edge(UP)
        l_2 = Tex("k!", "=", "k(k-1)(k-2)(k-3)...")
        l_2.next_to(l_1, DOWN, buff=0.5)
        l_3 = Tex("(k-n)!", "=", "(k-n)(k-n-1)(k-n-2)(k-n-3)...")
        l_3.next_to(l_2, DOWN, buff=0.5)
        l_4 = Text("Até 1.")
        l_4.next_to(l_3, DOWN, buff=0.5)
            
        self.wait(2)
        self.play(Write(l_1))
        self.play(Write(l_2))
        self.play(Write(l_3))
        self.play(Write(l_4))
        
        self.wait(2)
        l_5 = Tex("(k-3)!", "=", "(k-3)(k-4)(k-5)(k-6)...")
        l_5.next_to(l_2, DOWN, buff=0.5)
        self.play(ReplacementTransform(l_3, l_5))

        l_6 = VGroup(Tex("(k-3)!", "="), Cancel(Tex("(k-3)")), Cancel(Tex("(k-4)")), Cancel(Tex("(k-5)")), Cancel(Tex("(k-6)")), Tex("..."))
        l_6.arrange(RIGHT)
        l_6.next_to(l_2, DOWN, buff=0.5)
        l_7 = VGroup(Tex("k!", "=", "k(k-1)(k-2)"),Cancel(Tex("(k-3)")), Tex("..."))
        l_7.arrange(RIGHT)
        l_7.next_to(l_1, DOWN, buff=0.5)
        l_8 = VGroup(Tex("\\frac{k!}{(k-3)!}", "=", "k(k-1)(k-2)"))
        l_8.next_to(l_4, DOWN, buff=0.5)
        self.wait(2)
        self.play(Write(l_8))
        self.play(FadeTransform(l_5, l_6))
        self.play(FadeTransform(l_2, l_7))
        
        l_9 = VGroup(Tex("\\frac{k!}{(k-n)!}", "=", "k(k-1)(k-2)...(k-n)"))
        l_9.next_to(l_4, DOWN, buff=0.5)
        self.wait(2)
        
        l_3 = Tex("(k-n)!", "=", "(k-n)(k-n-1)(k-n-2)(k-n-3)...")
        l_3.next_to(l_2, DOWN, buff=0.5)
        self.play(FadeTransform(l_6, l_3))
        self.play(FadeTransform(l_7, l_2))
        self.play(FadeTransform(l_8, l_9))
        
        l_10 = Text("Até (k-n).")
        l_10.next_to(l_9, DOWN, buff=0.5)
        self.play(Write(l_10))
        self.remove(*self.mobjects)
        
    def scene3(self):
        eq_4 = Tex("f^n(x)", "=", "\\frac{k!}{(k-n)!}x^{k-n}")
        self.play(Write(eq_4))
        
        frase = VGroup(Text("Definido apenas para "), Tex("n \in \mathbb{N}"))
        frase.arrange(RIGHT)
        frase.next_to(eq_4, DOWN, buff=0.5)
        
        self.play(Write(frase))
        
        frase_2 = VGroup(Text("Podemos expandir a derivada iterada para  "), Tex("n \in \mathbb{R}"))
        frase_2.arrange(RIGHT)
        frase_2.next_to(frase, DOWN, buff=0.5)
        
        self.play(Write(frase_2))
        eq_4_gamma = Tex("f^n(x)", "=", "\\frac{\Gamma(k+1)}{\Gamma(k-n+1)}x^{k-n}")
        self.play(ReplacementTransform(eq_4, eq_4_gamma))
        self.wait(2)
        self.remove(*self.mobjects)
        
    def scene4(self):
        eq_4_n = Tex("\Gamma \left( x ) = \int\limits_0^\infty {s^{x - 1} e^{ - s} ds}}")
        self.play(Write(eq_4_n))
        
        eq_5 = Tex("\Gamma \left( x ) = (x + 1)! \hspace{0.3cm} | \hspace{0.3cm} x \in \mathbb{N}")
        eq_5.next_to(eq_4_n, DOWN, buff=0.5)
        self.play(Write(eq_5))
        self.wait(2)
        self.remove(*self.mobjects)
        
    def scene5(self):
        frase_1 = Text("Algum exemplos de induções de formulas de derivadas iteradas.")
        self.play(Write(frase_1))
        self.wait(2)
        self.remove(*self.mobjects)
        
        l_1 = Tex("f(x)", "=", "a^x")
        l_1.to_edge(UP)
        l_2 = Tex("f(x)'", "=", "In(a)a^x")
        l_2.next_to(l_1, DOWN, buff=0.3)
        l_3 = Tex("f(x)''", "=", "In(a)^2a^x")
        l_3.next_to(l_2, DOWN, buff=0.3)
        l_4 = Text("...")
        l_4.next_to(l_3, DOWN, buff=0.5)
        l_5 = Tex("f^n(x)", "=", "In(a)^na^x")
        l_5.next_to(l_4, DOWN, buff=0.5)
  
        
        self.play(Write(l_1))
        self.play(Write(l_2))
        self.play(Write(l_3))
        self.play(Write(l_4))
        self.play(Write(l_5))
        self.wait(2)
        self.remove(*self.mobjects)
        
    def scene6(self):
        l_1 = Tex("e^{ix}", "=", "cos(x) + isin(x)")
        l_1.to_edge(UP)
        l_2 = Tex("f(x)", "=", "e^{ix}")
        l_2.next_to(l_1, DOWN, buff=0.3)
        l_3 = Tex("f^n(x)", "=", "(ix)^ne^{ix}")
        l_3.next_to(l_2, DOWN, buff=0.7)
        l_4 = Tex("f^n(x)", "=", "(xe^{i\\frac{\\pi}{2}})^ne^{ix}")
        l_4.next_to(l_3, DOWN, buff=0.3)
        l_5 = Tex("f^n(x)", "=", "x^ne^{i(n\\frac{\\pi}{2} + x)}")
        l_5.next_to(l_4, DOWN, buff=0.3)
        l_6 = Tex("f^n(x)", "=", "x^n(cos(n\\frac{\\pi}{2} + x) + isin(n\\frac{\\pi}{2} + x))")
        l_6.next_to(l_5, DOWN, buff=0.3)
  
        
        self.play(Write(l_1))
        self.play(Write(l_2))
        self.play(Write(l_3))
        self.play(Write(l_4))
        self.play(Write(l_5))
        self.play(Write(l_6))
        self.wait(2)
        
    def scene6(self):
        l_1 = Tex("e^{ix}", "=", "cos(x) + isin(x)")
        l_1.to_edge(UP, buff=0.5)
        l_2 = Tex("f(x)", "=", "e^{ix}")
        l_2.next_to(l_1, DOWN, buff=0.3)
        l_3 = Tex("f^n(x)", "=", "(ix)^ne^{ix}")
        l_3.next_to(l_2, DOWN, buff=0.7)
        l_4 = Tex("f^n(x)", "=", "(xe^{i\\frac{\\pi}{2}})^ne^{ix}")
        l_4.next_to(l_3, DOWN, buff=0.3)
        l_5 = Tex("f^n(x)", "=", "x^ne^{i(n\\frac{\\pi}{2} + x)}")
        l_5.next_to(l_4, DOWN, buff=0.3)
        l_6 = Tex("f^n(x)", "=", "x^n(cos(n\\frac{\\pi}{2} + x) + isin(n\\frac{\\pi}{2} + x))")
        l_6.next_to(l_5, DOWN, buff=0.3)
  
        
        self.play(Write(l_1))
        self.play(Write(l_2))
        self.play(Write(l_3))
        self.play(Write(l_4))
        self.play(Write(l_5))
        self.play(Write(l_6))
        self.wait(4)
        self.remove(*self.mobjects)
        
        l_6 = Tex("\\frac{d^n}{dx^n}e^{ix}", "=", "x^n(cos(n\\frac{\\pi}{2} + x) + isin(n\\frac{\\pi}{2} + x))")
        self.play(Write(l_6))
        l_6.to_edge(UP, buff=2)
        l_7 = Tex("\\frac{d^n}{dx^n}cos(x)", "=", "cos(n\\frac{\\pi}{2} + x)")
        l_7.next_to(l_6, DOWN, buff=0.3)
        l_8 = Tex("\\frac{d^n}{dx^n}sin(x)", "=", "sin(n\\frac{\\pi}{2} + x)")
        l_8.next_to(l_7, DOWN, buff=0.3)
        
        self.play(Write(l_7))
        self.play(Write(l_8))
        self.wait(4)
        self.remove(*self.mobjects)
    def scene7(self):
        frase_1 = Text("Fórmula de Cauchy para integrações repetidas.")
        frase_1.to_edge(UP, buff=2)
        self.play(Write(frase_1))
        self.wait(2)
        l_1 = Tex("f^{(-n)}(x) = \\frac{1}{(n-1)!} \\int_a^x\\left(x-t)^{n-1} f(t)\\,\\mathrm{d}t")
        l_1.next_to(frase_1, DOWN, buff=0.6)
        self.play(Write(l_1))
        self.wait(2)
        self.remove(*self.mobjects)
        
        l_1 = Tex("f^{(-n)}(x) = \\frac{1}{(n-1)!} \\int_a^x\\left(x-t)^{n-1} f(t)\\,\\mathrm{d}t")
        l_1.to_edge(UP, buff=1)
        self.play(Write(l_1))
        l_2 = Tex("g(x) = \\frac{1}{(2-1)!} \\int_a^x\\left(x-t)^{2-1} f(t)\\,\\mathrm{d}t")
        l_2.next_to(l_1, DOWN, buff=0.8)
        self.play(Write(l_2))
        l_3 = Tex("g(x) = \\frac{1}{(1)!} \\int_a^x\\left(x-t) f(t)\\,\\mathrm{d}t")
        l_3.next_to(l_1, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_2, l_3))
        l_4 = Tex("g(x) = \\int_0^x\\left(x-t) f(t)\\,\\mathrm{d}t")
        l_4.next_to(l_1, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_3, l_4))
        self.wait(2)
        l_5 = Tex("g(x) = \\int_0^x xf(t) - tf(t)\\,\\mathrm{d}t")
        l_5.next_to(l_1, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_4, l_5))
        self.wait(2)
        l_6 = Tex("g(x) = x\\int_0^x f(t)\\,\\mathrm{d}t - \\int_a^x tf(t)\\,\\mathrm{d}t")
        l_6.next_to(l_1, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_5, l_6))
        self.wait(2)
        l_7 = Tex("g'(x) = (\\int_0^x f(t)\\,\\mathrm{d}t + xf(x)) - xf(x)")
        l_7.next_to(l_1, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_6, l_7))
        self.wait(2)
        l_8 = Tex("g'(x) = \\int_0^x f(t)\\,\\mathrm{d}t")
        l_8.next_to(l_1, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_7, l_8))
        self.wait(2)
        l_9 = Tex("g'(x) = f^{-1}(t)")
        l_9.next_to(l_1, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_8, l_9))
        self.wait(2)
        l_10 = Tex("g(x) = f^{-2}(t)")
        l_10.next_to(l_1, DOWN, buff=0.8)
        l_11 = Text("Como podemos provar.")
        l_11.next_to(l_10, DOWN, buff=0.8)
        self.play(ReplacementTransform(l_9, l_10))
        self.play(Write(l_11))
        self.wait(4)
        self.remove(*self.mobjects)
        
    def scene8(self):
        frase_1 = Text("Integrais Fracionarias de Riemann-Liouville.")
        frase_1.to_edge(UP, buff=2)
        self.play(Write(frase_1))
        self.wait(2)
        l_1 = Tex("I^{n}f(x) = \\frac{1}{\Gamma(n)} \\int_a^x\\left(x-t)^{n-1} f(t)\\,\\mathrm{d}t")
        l_1.next_to(frase_1, DOWN, buff=0.6)
        frase = VGroup(Text("Para "), Tex("n \in \mathbb{C}, Re(n) > 0"))
        frase.arrange(RIGHT)
        frase.next_to(l_1, DOWN, buff=0.5)
        self.play(Write(l_1))
        self.play(Write(frase))
        self.wait(2)
        
    def scene9(self):
        frase_1 = Text("Derivativa Fracionaria.")
        frase_1.to_edge(UP, buff=2)
        self.play(Write(frase_1))
        self.wait(2)
        l_1 = Tex("D^{n}f(x) = \\frac{d^{\\lceil n \\rceil}}{dx^{\\lceil n \\rceil}} (I^{\\lceil n \\rceil-n}f)")
        l_1.next_to(frase_1, DOWN, buff=0.6)
        self.play(Write(l_1))
        self.wait(2)
        
        l_2 = Tex("D^{n}f(x) = \\frac{d^{\\lceil 2.5 \\rceil}}{dx^{\\lceil 2.5 \\rceil}} (I^{\\lceil 2.5 \\rceil-2.5}f)")
        l_2.next_to(frase_1, DOWN, buff=0.6)
        self.play(ReplacementTransform(l_1, l_2))
        
        l_3 = Tex("D^{n}f(x) = \\frac{d^{3}}{dx^{3}} (I^{0.5}f)")
        l_3.next_to(frase_1, DOWN, buff=0.6)
        self.play(ReplacementTransform(l_2, l_3))
        
    def scene10(self):
        frase_1 = Text("Derivativa Fracionaria.")
        frase_1.to_edge(UP, buff=2)
        self.play(Write(frase_1))
        self.wait(2)
        l_1 = Tex("D^{n}f(x) = \\frac{d^{\\lceil n \\rceil}}{dx^{\\lceil n \\rceil}} (I^{\\lceil n \\rceil-n}f)")
        l_1.next_to(frase_1, DOWN, buff=0.6)
        self.play(Write(l_1))
        self.wait(2)
        
        l_2 = Tex("D^{n}f(x) = \\frac{d^{\\lceil 2.5 \\rceil}}{dx^{\\lceil 2.5 \\rceil}} (I^{\\lceil 2.5 \\rceil-2.5}f)")
        l_2.next_to(frase_1, DOWN, buff=0.6)
        self.play(ReplacementTransform(l_1, l_2))
        
        l_3 = Tex("D^{n}f(x) = \\frac{d^{3}}{dx^{3}} (I^{0.5}f)")
        l_3.next_to(frase_1, DOWN, buff=0.6)
        self.play(ReplacementTransform(l_2, l_3))
        self.wait(4)
        self.remove(*self.mobjects)
        
    def scene11(self):
        frase_1 = Text("Propriedades da Integral de Riemann-Liouville.")
        frase_1.to_edge(UP, buff=2)
        self.play(Write(frase_1))
        self.wait(2)
        l_1 = Tex("\\frac{d}{dx}I^{a+1}f(x) = I^af(x)")
        l_1.next_to(frase_1, DOWN, buff=0.6)
        l_2 = Tex("I^a(I^bf) = I^{a+b}f")
        l_2.next_to(l_1, DOWN, buff=0.6)
        self.play(Write(l_1))
        self.play(Write(l_2))
        self.wait(4)
        self.remove(*self.mobjects)
        
        
    def scene13(self):
        frase_1 = Text("Riemann-Liouville Derivativa Fracional Direita")
        frase_1.to_edge(UP, buff=2)
        self.play(Write(frase_1))
        self.wait(2)
        l_1 = Tex("\\frac{d}{dx}I^{a+1}f(x) = I^af(x)")
        l_1.next_to(frase_1, DOWN, buff=0.6)
        l_2 = Tex("I^a(I^bf) = I^{a+b}f")
        l_2.next_to(l_1, DOWN, buff=0.6)
        self.play(Write(l_1))
        self.play(Write(l_2))
        
        
        
        
        
        
        
        