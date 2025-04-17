from manim import *

class similarity(Scene):
	def construct(self):
		# self.text()
		# self.triangle()
		self.rectangle()
		self.triangle()
		self.text()


	def text(self):
		txt1=Tex(r"Q. Prove that two triangles are similar when the two sides are parallel",font_size=20).to_corner(UL)
		txt2=MathTex(r"\textbf{Given: }",font_size=22).move_to(UP*3+LEFT*6.2)
		txt3=MathTex(r" PQ \parallel BC",font_size=20).move_to(UP*2.6+LEFT*5.5)
		txt4=MathTex(r"\textbf{To Prove:  }",font_size=22).move_to(UP*2.2+LEFT*6)
		txt5=MathTex(r"\triangle ABC \sim \triangle APQ",font_size=20).move_to(UP*1.8+LEFT*5.25)
		txt6=MathTex(r"\textbf{Proof:  }",font_size=22).move_to(UP*1.4+LEFT*6.15)
		txt7=MathTex(r"\text{Corresponding Angles are equal(by Parallel Lines Theorem)}\\ \text{Since } PQ \parallel BC \text{ ,we use the corresponding angle theorem: }",font_size=20).move_to(UP*1+LEFT*3.5)
		txt8=MathTex(r"\angle APQ = \angle ABC \text{(Corresponding angles)} \\ \angle AQP = \angle ACB \text{(Corresponding angles)}",font_size=20).move_to(UP*0.4+LEFT*4)
		txt9=MathTex(r"\text{Since two pairs of corresponding angles are equal, by AA similarity:}",font_size=20).move_to(UP*-0.2+LEFT*3)
		txt10=MathTex(r"\triangle ABC \sim \triangle APQ",font_size=20).move_to(UP*-0.6+LEFT*3.5)



		grp=VGroup(txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10)



		

		#animation stuff
		for i,j in enumerate(grp):
			self.play(Create(j))
			if i == 2:
				self.parallel()
			self.wait(1)
		self.wait(5)


	def triangle(self):
		C = LEFT + UP
		B = RIGHT + UP
		A = ORIGIN
		Q = 0.5 * LEFT + 0.5 * UP
		P = 0.5 * RIGHT + 0.5 * UP

		triangle1 = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
		triangle2 = Polygon(Q, P, A, color=GREEN, fill_opacity=0.1)


		all_shapes = VGroup(triangle1, triangle2).rotate(PI)

		label_C = Text("C", font_size=10).move_to(C + UP * 0.2).rotate(PI)
		label_B = Text("B", font_size=10).move_to(B + UP * 0.2).rotate(PI)
		label_A = Text("A", font_size=10).move_to(A + DOWN * 0.3).rotate(PI)
		label_Q = Text("Q", font_size=10).move_to(Q + LEFT * 0.2).rotate(PI)
		label_P = Text("P", font_size=10).move_to(P + RIGHT * 0.2).rotate(PI)

		labels = VGroup(label_A, label_B, label_C, label_Q, label_P).rotate(PI)

		all_shapes.move_to(RIGHT * 2 + UP)
		labels.move_to(RIGHT* 2 + UP)
		all_shapes.scale(2)
		labels.scale(2)
		self.play(Create(all_shapes))
		self.play(Write(labels))
			
	def parallel(self):
		C = LEFT + UP
		B = RIGHT + UP
		A = ORIGIN
		Q = 0.5 * LEFT + 0.5 * UP
		P = 0.5 * RIGHT + 0.5 * UP
		line_PQ = Line(P, Q, color=YELLOW, stroke_width=4)
		line_BC = Line(B, C, color=RED, stroke_width=4)
		
		line_PQ.move_to(RIGHT*2+UP)
		line_BC.move_to(RIGHT*2+UP*0.01)
		line_PQ.scale(2)
		line_BC.scale(2)

		self.play(Create(line_BC), Create(line_PQ))


	def rectangle(self):

		rec= Rectangle(height = config.frame_height, width= config.frame_width, color=WHITE)
		self.play(Create(rec))
		self.wait(2)