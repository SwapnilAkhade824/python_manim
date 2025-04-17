from manim import *

class SurfaceGraph(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: np.array([u, v, u**2 + v**2]),
            u_range=[-2, 2], v_range=[-2, 2],
            color=BLUE
        )
        self.add(axes, surface)
        self.wait()
