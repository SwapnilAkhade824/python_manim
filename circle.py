from manim import * 
import math

class curcul(Scene):
	fku = math.pi 
	dku = -math.pi
	def construct(self):
		axex = Axes()
		p1=NumberPlane(x_range=[0,7,1],y_range=[-1,1,1], axis_config={"color":RED} ,background_line_style = {"stroke_opacity":0})
		p2=NumberPlane(x_range=[0,7,1],y_range=[-1,1,1], axis_config={"color":GREEN},background_line_style = {"stroke_opacity":0})
		p3=NumberPlane(x_range=[-3,3,1],y_range=[-3,3,1], axis_config={"color":BLUE},background_line_style = {"stroke_opacity":0})
	
		p1.shift(LEFT * 3 + UP * 2) 	
		p2.shift(RIGHT * 3 + UP * 2)  	
		p3.shift(DOWN * 2)  	

		p1.scale(0.5)
		p2.scale(0.5)
		p3.scale(0.5)
		
		sin = p1.plot(lambda x: math.sin(x), x_range=[0,self.fku*2,1])
		cos = p2.plot(lambda x: math.cos(x), x_range=[0,self.fku*2,1])
		cir = p3.plot_implicit_curve(lambda x,y: x**2+y**2-4)
		
		dot1 = Dot(color=YELLOW).move_to(p1.c2p(0, 0))  # start at (0,0)
		dot2 = Dot(color=YELLOW).move_to(p2.c2p(0, 0))  # start at (0,0)
		dot3 = Dot(color=YELLOW).move_to(p3.c2p(0, 0))  # start at (0,0)

		def dotI(mob,alpha):
			x = interpolate(0,self.fku*2,alpha)
			y = math.sin(x)
			mob.move_to(p1.c2p(x,y))
		def dotII(mob,alpha):
			x = interpolate(0,self.fku*2,alpha)
			y = math.cos(x)
			mob.move_to(p2.c2p(x,y))
		def dotIII(mob,alpha):
			angle = interpolate(0,2*math.pi,alpha)
			y = 2 * math.sin(angle)
			x = 2 * math.cos(angle)
			mob.move_to(p3.c2p(x,y))


		self.play(Create(p1),Create(p2),Create(p3),Create(sin),Create(cos),Create(cir))
		self.add(dot1,dot2,dot3)
		self.play(UpdateFromAlphaFunc(dot1, dotI, run_time=5), UpdateFromAlphaFunc(dot2, dotII, run_time=5),UpdateFromAlphaFunc(dot3, dotIII, run_time=5)) 
		#self.wait(100)  #cause why not :-)
		self.wait(2)