from typing_extensions import runtime
from manim import *

class ImageExample(Scene):

    def construct(self):
        self.rocket1()

    def rocket1(self):
        # Load image (make sure it's in the same folder or provide full path)
        image = ImageMobject("rocket.jpg")

        # Optional: scale or move the image
        image.rotate(PI/4)
        image.scale(2)
        #self.play(FadeIn(image), run_time=2)
        #self.add(image)
        self.play(image.animate.scale(scale_factor=0.5).shift(LEFT*4 + DOWN*4),run_time=2)
        self.play(Rotate(image,angle=-PI/4),run_time=1)
        #self.play(image.animate.move_to([4,4,0]))
        # Wait to display
        self.wait(2)