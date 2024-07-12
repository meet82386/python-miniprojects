from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move

        self.goto(x_cor, y_cor)

    def bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        if self.speed >= 0.04:
            self.speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.x_bounce()