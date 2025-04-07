from manim import *

class UpdaterExample(Scene):
    def construct(self):
        # Create a square
        square = Square(color=RED)

        # Create a dot that follows the square
        dot = always_redraw(lambda: Dot().next_to(square, RIGHT))

        # Add the objects to the scene
        self.add(square, dot)

        # Animate the square moving
        self.play(square.animate.shift(UP))
        self.wait()