from manim import *

class mini_project(Scene):
	def construct(self):
		#Text
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
		for i in grp:
			self.play(Create(i))
			self.wait(1)
		self.wait(5)



