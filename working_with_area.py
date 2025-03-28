from typing_extensions import runtime
from manim import *

class working_with_area(Scene):

	config.pixel_height = 1080
	config.pixel_width = 1920
	config.frame_height = 18.0
	config.frame_width = 32.0

	def construct(self):

		self.show_axis()
		self.wait()
		self.make_curve()
		self.wait()
		self.make_area()
		self.wait(2)

	def show_axis(self):

		axes = Axes(
			x_range=[-5,5.5,1],
			y_range=[-5,5.5,1],
			x_length=10,
			y_length=10,
			axis_config={
				"include_numbers":True
			}
		)

		self.axes = axes
		self.add(axes)

	def make_curve(self):

		circleup = self.axes.plot(lambda x: (4-x**2)**(0.5),x_range=[-2,2,0.001],color=BLUE,stroke_width=3)
		circledn = self.axes.plot(lambda x: -(4-x**2)**(0.5),x_range=[-2,2,0.001],color=BLUE,stroke_width=3)

		self.curve1,self.curve2 = circleup,circledn
		self.add(circleup,circledn)

	def make_area(self):

		area1 = self.axes.get_area(self.curve1,x_range=(-2,2),color=BLUE)
		area2 = self.axes.get_area(self.curve2,x_range=(-2,2),color=BLUE)

		# area = VGroup(area1,area2)
		self.play(FadeIn(area1),FadeIn(area2),run_time=2)
		self.wait(2)
		self.play(FadeOut(area1),FadeOut(area2),run_time=2)

