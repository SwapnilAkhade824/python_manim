from manim import *

class Example(Scene):
    def construct(self):
        vt = ValueTracker(5)

        # Showing the Example
        text1 = Tex(r"Example: Evaluate the integral", font_size=25)
        eqn1 = MathTex(r"\iint\limits_{R} xy (x+y) \, dx\,dy", font_size=20)
        text2 = Tex(r"over the area between the curves\\", font_size=20)
        eqn2 = MathTex(r"y=x^2", font_size=20)
        text3 = Tex(r"and", font_size=20)
        eqn3 = MathTex(r"y=x", font_size=20)
        grp = VGroup(text1, eqn1, text2, eqn2, text3, eqn3).arrange(RIGHT)

        text4 = MathTex(r"\text{We have } y=x^2 \text{ and } y=x, x^2 - x=0 \text{ i.e. either } x=0 \text{ or } x=1", font_size=25)
        text5 = MathTex(r"\text{Further, if } x=0 \text{ then } y=0, \text{ if } x=1 \text{ then } y=1. \\ \text{This means the two curves intersect at points } (0,0) \text{ and } (1,1).", font_size=25)

        # Graph
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE}
        ).shift(DOWN * 2)

        curve1 = axes.plot(lambda x: x**2, x_range=[-2, 2], color=BLUE)
        curve2 = axes.plot(lambda x: x, x_range=[-2, 2], color=BLUE)

        # Shading areas properly
        area1 = axes.get_area(curve1, x_range=[-2, 0], color=YELLOW)  # left side region
        area_between = axes.get_area(curve2, bounded_graph=curve1, x_range=[0,1], color=RED)  # region strictly between y=x and y=x^2
        area2 = axes.get_area(curve1, x_range=[0, 2], color=RED)  # left side region

        # Grouping graph elements
        self.play(Write(grp), run_time=5)
        self.play(grp.animate.move_to(UP * 3 + LEFT * 1), run_time=2)
        self.play(Write(text4), run_time=5)
        self.play(text4.animate.move_to(UP * 2.5 + LEFT * 2.5))
        self.play(Write(text5), run_time=5)
        self.play(text5.animate.move_to(UP * 2 + LEFT * 0.5))
        self.play(Create(axes), run_time=3)
        self.play(Create(curve1), Create(curve2), run_time=3)
        self.play(Create(area1), Create(area_between),Create(area2), run_time=3)

        self.wait(5)
