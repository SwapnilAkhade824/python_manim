from manim import *

class SmoothShapeTransition(Scene):
    def construct(self):
        square = Square() 
        square.set_fill(PINK, opacity=0.5)
        square.rotate(PI / 4)  

        rect = Rectangle(width=2.5, height=1.5)
        rect.set_fill(RED, opacity=0.5) 
        rect.rotate(PI / 2) 

        circle = Circle() 
        circle.set_fill(BLUE, opacity=0.5)

        triangle = Triangle()
        triangle


        self.play(Create(square))
        self.play(Transform(square, rect, run_time=1.5))
        self.play(Transform(square, circle, run_time=1.5))
        self.play(FadeOut(square))  
