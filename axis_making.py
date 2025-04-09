from manim import *

class axis_making(Scene):
    def construct(self):
        

        # Axes
        axes = Axes(
            x_range=[-4, 7, 1],
            y_range=[-1, 7, 1],
            x_length=11,
            y_length=8,
            axis_config={"include_tip": True},

            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True}
        ).to_edge(DOWN)

        self.add(axes)
        self.wait()
       