from os import access
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
		self.rectangles(0.5)
		self.rectangles(0.25)

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

		self.play(FadeIn(rectangles))
		self.wait(2)
		self.play(FadeOut(rectangles))
		self.wait(1)