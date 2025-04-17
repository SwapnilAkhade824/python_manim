from manim import *

class SimilarTrianglesWithCommonVertex(Scene):
    def construct(self):

        C = LEFT + UP
        B = RIGHT + UP
        A = ORIGIN
        Q = 0.5 * LEFT + 0.5 * UP
        P = 0.5 * RIGHT + 0.5 * UP

        triangle1 = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        triangle2 = Polygon(Q, P, A, color=GREEN, fill_opacity=0.1)


        all_shapes = VGroup(triangle1, triangle2).rotate(PI)

        label_C = Text("C", font_size=10).move_to(C + UP * 0.2).rotate(PI)
        label_B = Text("B", font_size=10).move_to(B + UP * 0.2).rotate(PI)
        label_A = Text("A", font_size=10).move_to(A + DOWN * 0.3).rotate(PI)
        label_Q = Text("Q", font_size=10).move_to(Q + LEFT * 0.2).rotate(PI)
        label_P = Text("P", font_size=10).move_to(P + RIGHT * 0.2).rotate(PI)

        labels = VGroup(label_A, label_B, label_C, label_Q, label_P).rotate(PI)

        self.play(Create(all_shapes))
        self.play(Write(labels))
        # self.wait(5)
        triangle1.set_fill(GRAY, opacity=0.05).set_stroke(GRAY, opacity=0.2)
        triangle2.set_fill(GRAY, opacity=0.05).set_stroke(GRAY, opacity=0.2)
        line_PQ = Line(P, Q, color=YELLOW, stroke_width=4)
        line_BC = Line(B, C, color=RED, stroke_width=4)
        line_BC.move_to(DOWN * 0.01)
        self.play(Create(line_BC), Create(line_PQ))
        # self.wait(8)

