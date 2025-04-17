from typing_extensions import runtime
from manim import *
# from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.recorder import RecorderService
import numpy as np

class IntegrationFull(Scene):
    def construct(self):
        self.frame1_intro()
        self.frame2_definition()
        self.frame3()
        self.frame4_limit_notation()
        self.frame5_types_of_integrals()
        self.frame6_constant_velocity()
        self.frame7_varying_velocity()
        self.frame8_closing_quote()

    def frame1_intro(self):
        title = Tex(r"\textbf{Understanding the Concept of Integration}", font_size=60)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

    def frame2_definition(self):
        definition = Tex(
            r"\text{Integration is the reverse of differentiation,}",
            r"\\\text{often referred to as the antiderivative.}",
            font_size=48
        )
        self.play(Write(definition))
        self.wait(2)

        func_example = MathTex(r"F(x) = \int f(x)\, dx", font_size=60)
        self.play(Transform(definition, func_example))
        self.wait(2)
        self.play(FadeOut(definition))

    def frame3(self):
        self.areas = VGroup()
        size = 0.5
        self.coordinate_axis()
        self.curve()
        while size > 0.01:
            self.rectangles(size)
            size /= 2       
        self.add(self.areas[0])
        for i in range(len(self.areas)-1):
            self.play(Transform(self.areas[0],self.areas[i+1]),run_time=2)
        # self.data()
        self.wait(3)
        self.play(FadeOut(self.axis), FadeOut(self.areas[0]), FadeOut(self.curve_graph))
    def coordinate_axis(self):
        axis = Axes(
            x_range = [-1.5, 7.5, 1],
            y_range = [-1.5, 1.5, 1],
            x_length = 10,  # scaled down from 15
            y_length = 5,   # scaled down from 10
        )
        self.axis = axis
        axis.move_to(ORIGIN)  # centers it on screen
        self.add(axis)

    def curve(self):
        self.curve_graph = self.axis.plot(lambda x: np.sin(x), x_range=[-0.5, 7, 0.001])
        self.add(self.curve_graph)
    def rectangles(self,size):
        count = 0
        x_c = [0,size]
        y_c = [0,np.sin(sum(x_c)/2)]
        rectangles = VGroup()
        while count < np.ceil(2*np.pi/size):
            rect = Polygon(
                self.axis.coords_to_point(x_c[0],y_c[0]),
                self.axis.coords_to_point(x_c[1],y_c[0]),
                self.axis.coords_to_point(x_c[1],y_c[1]),
                self.axis.coords_to_point(x_c[0],y_c[1]),
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=0.3
            )
            rectangles.add(rect)
            x_c = x_c[::-1]
            x_c[1] = x_c[0] + size
            y_c[1] = np.sin(sum(x_c)/2)
            count += 1
        self.areas.add(rectangles)

    def frame4_limit_notation(self):
        eq = MathTex(
            r"\int_a^b f(x)\, dx = \lim_{\Delta x \to 0} \sum_{i=1}^n f(x_i) \Delta x",
            font_size=48
        )
        self.play(Write(eq))
        self.wait(3)
        self.play(FadeOut(eq))

    def frame5_types_of_integrals(self):
        title = Tex("Types of Integrals", font_size=60)
        indef = MathTex(r"\text{Indefinite:} \quad \int f(x)\, dx = F(x) + C", font_size=48)
        defin = MathTex(r"\text{Definite:} \quad \int_a^b f(x)\, dx = F(b) - F(a)", font_size=48)
        group = VGroup(indef, defin).arrange(DOWN, aligned_edge=LEFT, buff=0.8)

        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(group))

    def frame6_constant_velocity(self):
        ax = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": GREY}
        ).to_edge(DOWN)

        v_graph = ax.plot(lambda x: 3, x_range=[0, 5], color=GREEN)
        label = ax.get_graph_label(v_graph, label="v(t) = 3", x_val=4)

        self.play(Create(ax), Create(v_graph), Write(label))
        area = ax.get_area(v_graph, x_range=(0, 5), color=BLUE, opacity=0.5)
        self.play(FadeIn(area))
        text = Tex("Displacement = Area under the curve", font_size=48).to_edge(UP)
        self.play(Write(text))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [ax, v_graph, label, area, text]])

    def frame7_varying_velocity(self):
        ax = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": GREY}
        )
        ax.move_to(ORIGIN)

        v_graph = ax.plot(lambda x: -(x-2.5)**2+6.25, x_range=[0, 5], color=ORANGE)
        self.play(Create(ax), Create(v_graph))

        area = ax.get_area(v_graph, x_range=(0, 5), color=RED, opacity=0.5)
        self.play(FadeIn(area))
        text = Tex("Displacement with varying velocity", font_size=48).to_edge(UP)
        self.play(Write(text))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [ax, v_graph, area, text]])

    def frame8_closing_quote(self): #ABSOLUTELY UNNECESSARY PART OF THE VIDEO LMFAO
        quote = Tex(
            r"``The integral sign $\int$ was introduced in 1675.''",
            r"\\\text{It's a stretched-out S for \textit{summa}, the Latin word for sum.}",
            font_size=48
        ) 
        self.play(Write(quote))
        self.wait(3)
        self.play(FadeOut(quote))
        # thanks = Tex(r"\textbf{woooooooo hoooo,ba bam ba bam \\ chal gand mara}", font_size=60, color=BLUE)
        # self.add((thanks))
        # self.wait(0.2)
        
