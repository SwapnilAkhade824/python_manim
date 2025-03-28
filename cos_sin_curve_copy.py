from manim import *

class SineCurveUnitCircle(Scene):

    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width = 32.0
    
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-5,-3,0])
        x_end = np.array([6,-3,0])

        y_start = np.array([-4,-5,0])
        y_end = np.array([-4,6,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()
        self.add_y_labels()

        self.origin_point = np.array([-4,-3,0])
        self.curve_start_sin = np.array([-3,-3,0])
        self.curve_start_cos = np.array([-3,-2,0])

    def add_x_labels(self):
        x_labels = [
            MathTex(r"0"),
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi")
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-3 + 2*i, -3, 0]), DOWN)
            self.add(x_labels[i])

    def add_y_labels(self):
        y_labels = [
            MathTex(r"0"),
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi")
        ]

        for i in range(len(y_labels)):
            y_labels[i].next_to(np.array([-4, -2 + 2*i, 0]), LEFT)
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

        def get_line_to_curve_sin():
            x_sin = self.curve_start_sin[0] + self.t_offset * 4
            y_sin = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x_sin,y_sin,0]), color=YELLOW_A, stroke_width=2 )

        

        self.curve1 = VGroup()
        self.curve1.add(Line(self.curve_start_sin,self.curve_start_sin))
        def get_curve_sin():
            last_line = self.curve1[-1]
            x_sin = self.curve_start_sin[0] + self.t_offset * 4
            y_sin = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x_sin,y_sin,0]), color=YELLOW_D)
            self.curve1.add(new_line)

            return self.curve1

        def get_line_to_curve_cos():
            y_cos = self.curve_start_cos[1] + self.t_offset * 4
            x_cos = dot.get_center()[0]
            return Line(dot.get_center(), np.array([x_cos,y_cos,0]), color=YELLOW_A, stroke_width=2 )


        self.curve2 = VGroup()
        self.curve2.add(Line(self.curve_start_cos,self.curve_start_cos))
        def get_curve_cos():
            last_line = self.curve2[-1]
            y_cos = self.curve_start_cos[1] + self.t_offset * 4
            x_cos = dot.get_center()[0]
            new_line = Line(last_line.get_end(),np.array([x_cos,y_cos,0]), color=YELLOW_D)
            self.curve2.add(new_line)

            return self.curve2

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line_sin = always_redraw(get_line_to_curve_sin)
        sine_curve_line = always_redraw(get_curve_sin)
        dot_to_curve_line_cos = always_redraw(get_line_to_curve_cos)
        cosine_curve_line = always_redraw(get_curve_cos)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line_sin, sine_curve_line, dot_to_curve_line_cos, cosine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)