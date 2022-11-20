from manim import *

class Vector1(Scene):
    def construct(self):
        #Slide 1
        text_1 = Tex("Concept of Quantity")
        self.play(Write(text_1))
        self.wait(1)
        #Slide 2
        self.play(text_1.animate.shift(UP * 3.2))
        duck = SVGMobject("duck.svg")
        duck.set_color(WHITE)
        self.play(Write(duck))
        self.wait(1)
        #Slide 3
        self.play(duck.animate.shift(LEFT * 3))
        sqr = Square(side_length = 4, color = BLUE)
        sqr.shift(RIGHT * 3)
        self.play(Create(sqr))
        self.wait(1)
        #slide 4
        
        pass