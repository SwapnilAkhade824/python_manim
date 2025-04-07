from manim import *

class sin_cos_waves(Scene):

	config.pixel_height = 1080
	config.pixel_width = 1920
	config.frame_height = 18.0
	config.frame_width = 32.0

	unit = 1.1

	def construct(self):

		self.show_axis()
		self.add_circle()
		self.draw_line()
		self.wait()
		self.dot_moving_with_curve()
		self.wait(2)


	def show_axis(self):

		global ax

		ax = Axes(
			x_range=[-2,7,1],
			y_range=[-2,7,1],
			x_length=10,
			y_length=10,
			axis_config={
				"include_numbers":False,
			}
		)

		labels_x = [
			MathTex(r"0"),MathTex(r"\frac {\pi}{2}"),MathTex(r"\pi"),MathTex(r"\frac {3 \pi}{2}"),MathTex(r"2 \pi")
		]
		labels_y = [
			MathTex(r"0"),MathTex(r"\frac {\pi}{2}"),MathTex(r"\pi"),MathTex(r"\frac {3 \pi}{2}"),MathTex(r"2 \pi")
		]

		for i in range(len(labels_x)):

			labels_x[i].next_to(np.array([ax.get_origin()[0] + self.unit * (i+1), ax.get_origin()[1], 0]), DOWN*3)
			labels_y[i].next_to(np.array([ax.get_origin()[0], ax.get_origin()[1] + self.unit * (i+1), 0]), LEFT*3)
			self.add(labels_x[i])
			self.add(labels_y[i])

		self.add(ax)
		origin = ax.get_origin()
		ad = self.unit
		self.cur_st_sin = np.array(origin + [ad,0,0])
		self.cur_st_cos = np.array(origin + [ad,ad,0])

	def add_circle(self):

		circle = Circle(radius = self.unit)
		circle.move_to(ax.coords_to_point(0,0))
		self.add(circle)
		self.circle = circle
		
	def draw_line(self):

		origin = ax.get_origin()
		edge = VGroup()
		ad = self.unit
		edge.add(Line(origin + [ad,0,0], origin + [ad,ad,0],color=WHITE))
		edge.add(Line(origin + [0,ad,0], origin + [ad,ad,0],color=WHITE))
		self.add(edge)

	def dot_moving_with_curve(self):  

		dot = Dot(radius=0.08,color=YELLOW)
		dot.move_to(self.circle.point_from_proportion(0))
		self.t_offset = 0
		rate = 0.25

		def move_around_circle(mob,dt):

			self.t_offset += (dt*rate)
			dot.move_to(self.circle.point_from_proportion(self.t_offset % 1))

		self.sin_cur = VGroup()
		self.sin_cur.add(Line(self.cur_st_sin, self.cur_st_sin))

		def draw_curve_sin():
			last_line = self.sin_cur[-1]
			x = self.cur_st_sin[0] + self.t_offset * self.unit * 4
			y = dot.get_center()[1]
			self.sin_cur.add(Line(last_line.get_end(),np.array([x,y,0]),color=GREEN,stroke_width=3))

			return self.sin_cur

		def trace_sin():

			return Line(dot.get_center(),self.sin_cur[-1].get_end(),color=RED)

		self.cos_cur = VGroup()
		self.cos_cur.add(Line(self.cur_st_cos, self.cur_st_cos))

		def draw_curve_cos():
			last_line = self.cos_cur[-1]
			y = self.cur_st_cos[0] + self.t_offset * self.unit * 4
			x = dot.get_center()[0]
			self.cos_cur.add(Line(last_line.get_end(),np.array([x,y,0]),color=GREEN,stroke_width=3))

			return self.cos_cur

		def trace_cos():

			return Line(dot.get_center(),self.cos_cur[-1].get_end(),color=RED)

		dot.add_updater(move_around_circle)

		cur_sin = always_redraw(draw_curve_sin)
		cur_cos = always_redraw(draw_curve_cos)
		trac_sin = always_redraw(trace_sin)
		trac_cos = always_redraw(trace_cos)

		self.add(dot)
		self.add(cur_sin,trac_sin,cur_cos,trac_cos)

		self.wait(4.05)

		dot.remove_updater(move_around_circle)

