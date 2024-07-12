from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color("green")
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_tim(self):
        self.goto(STARTING_POSITION)

    def is_lvl_completed(self):
        y_cord = self.ycor()

        if y_cord >= FINISH_LINE_Y:
            return True
        return False
