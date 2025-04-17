from manim import * 

class Graphspeed(Scene):
	def construct(self):
		axes = Axes( x_range=[-3,3,1],y_range=[-5,10,1],axis_config={"color":WHITE})

		graph = axes.plot(lambda x: x**2, color=BLUE, x_range=[-3,3])
		diff_grph= axes.plot(lambda x: 2*x, color=RED, x_range=[-3,3])
		dot=Dot().move_to(axes.c2p(-2,4))

		def asdasdasfsd(mob, alpha):
			x = interpolate(-2, 0,alpha*10)
			y = x**2 
			mob.move_to(axes.c2p(x, y))
		def update_slow_dot(mob, alpha):
			x = interpolate(0, 2,alpha)
			y = x**2 
			mob.move_to(axes.c2p(x, y))

		self.add(axes,graph, diff_grph)
		self.add(dot)
		self.play(UpdateFromAlphaFunc(dot, asdasdasfsd), run_time=15, rate_func=linear)
		self.play(UpdateFromAlphaFunc(dot, update_slow_dot), run_time=2, rate_func=linear)
		self.wait()
