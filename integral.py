from manim import *
# from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.recorder import RecorderService

class antiderivative(Scene):
	def playlist(self):
		self.frame1()
		self.frame2()

	def frame1(self):
		intro= tex(
			"Understanding the Concept of Integration" #lets see how basic integral works
			)
		self.play(Write(intro))

	def frame2(self):
		defin= tex(
			"F(x)=\int_{}^{} f(x) dx \\" #This is how a basic integral looks like
			)
		self.play(Write(defin))

class frame3(Scene):
	def construct(self):
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
		self.areas.add(rectangles)