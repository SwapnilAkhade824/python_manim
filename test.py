from manim import *

class IntegrationAsReverseDifferentiation(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Original function f(x) = x^2 (parabola)
        func = axes.plot(lambda x: x**2, color=GREEN)
        func_label = MathTex("f(x) = x^2").next_to(func, UR, buff=0.2).set_color(GREEN)

        # Derivative f'(x) = 2x (straight line)
        derivative = axes.plot(lambda x: 2*x, color=RED)
        derivative_label = MathTex("f'(x) = 2x").next_to(derivative, UR, buff=0.2).set_color(RED)

        # Integration symbol and result (x^2 + C)
        integral_symbol = MathTex(r"\int 2x \,dx = x^2 + C").scale(1.2)
        integral_symbol.to_edge(UP)

        # Differentiation arrow
        diff_arrow = Arrow(
            start=func.get_end() + RIGHT,
            end=derivative.get_end() + RIGHT,
            color=YELLOW,
            buff=0.2,
            stroke_width=4
        )
        diff_text = Text("Differentiate", font_size=24).next_to(diff_arrow, RIGHT)

        # Integration arrow (reverse)
        int_arrow = Arrow(
            start=derivative.get_start() + LEFT,
            end=func.get_start() + LEFT,
            color=YELLOW,
            buff=0.2,
            stroke_width=4
        )
        int_text = Text("Integrate", font_size=24).next_to(int_arrow, LEFT)

        # Analogy text
        analogy = Text("Integration reverses differentiation!", font_size=28)
        analogy.to_edge(DOWN)

        # Animation sequence
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # Show original function
        self.play(Create(func), Write(func_label))
        self.wait(1)

        # Differentiate to get f'(x)
        self.play(
            TransformFromCopy(func, derivative),
            TransformFromCopy(func_label, derivative_label),
            GrowArrow(diff_arrow),
            Write(diff_text)
        )
        self.wait(1)

        # Integrate back to f(x) + C
        self.play(
            Write(integral_symbol),
            GrowArrow(int_arrow),
            Write(int_text),
            Write(analogy)
        )
        self.wait(2)