from manim import *

class SineCurveUnitCircle(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,-2,0])
        x_end = np.array([6,-2,0])

        y_start = np.array([-4,-6,0])
        y_end = np.array([-4,6,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()
        self.add_y_labels()

        self.origin_point = np.array([-4,-2,0])
        self.sin_curve_start = np.array([-3,-2,0])
        self.cos_curve_start = np.array([-4,-1,0])

    def add_x_labels(self):
        x_labels = [MathTex("0"),
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-3 + 2*i, -2, 0]), DOWN)
            self.add(x_labels[i])

    def add_y_labels(self):
        y_labels = [MathTex("0"),
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
        ]
        for i in range(len(y_labels)): 
            y_labels[i].next_to(np.array([-4,-1+2*i,0]),LEFT)
            self.add(y_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_sin_curve():
            x = self.sin_curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=BLUE, stroke_width=2 )

        def get_line_to_cos_curve():
            y = self.cos_curve_start[1] + self.t_offset *  4 
            x = dot.get_center()[0]
            return Line(dot.get_center(), np.array([x, y, 0]), color=RED_A, stroke_width=2)

        self.sin_curve = VGroup()
        self.sin_curve.add(Line(self.sin_curve_start, self.sin_curve_start))
        
        self.cos_curve = VGroup()
        self.cos_curve.add(Line(self.cos_curve_start, self.cos_curve_start))

        def get_sin_curve():
            last_line = self.sin_curve[-1]
            x = self.sin_curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=GREEN)
            self.sin_curve.add(new_line)
            return self.sin_curve

        def get_cos_curve():
            last_line = self.cos_curve[-1]
            x = dot.get_center()[0]
            y = self.cos_curve_start[1] + self.t_offset*4
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color = YELLOW)
            self.cos_curve.add(new_line)

            return self.cos_curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_sin_curve)
        dot_to_curve_line2=always_redraw(get_line_to_cos_curve)
        sine_curve_line = always_redraw(get_sin_curve)
        cos_curve_line = always_redraw(get_cos_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line,dot_to_curve_line2, sine_curve_line, cos_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)


