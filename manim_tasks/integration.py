from typing_extensions import runtime
from manim import *

class Integration(Scene):

	config.pixel_height = 1080
	config.pixel_width = 1920
	config.frame_height = 18.0
	config.frame_width = 32.0 

	def construct(self):

		self.coordinate_axis()
		self.curve()
		self.rectangles()

		self.wait(5)

	def coordinate_axis(self):

		axis = Axes(
			x_range = [-1.5,7.5,1],
			y_range = [-1.5,1.5,1],
			x_length = 15,
			y_length = 10
		)

		self.axis = axis
		axis.shift(LEFT*5)

		self.add(axis)

	def curve(self):

		curve = self.axis.plot(lambda x: np.sin(x),x_range=[-0.5,7,0.001])

		self.add(curve)

	def rectangles(self):

		rect = Rectangle(width=1,height=2,color=BLUE,fill_color=BLUE,fill_opacity=0.3)
		rect.move_to(self.axis.c2p())

		self.add(rect)