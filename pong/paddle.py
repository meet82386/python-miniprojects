from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__("square")
        self.penup()
        self.setpos(x, y)
        self.color("white")
        self.setheading(90)
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        y_cord = self.pos()[1]
        if y_cord < 240:
            self.forward(20)

    def move_down(self):
        y_cord = self.pos()[1]
        if y_cord > -240:
            self.back(20)
