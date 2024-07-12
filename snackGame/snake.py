import turtle as t

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        """Initialize snake object."""
        self.snake = []
        self.place_snake()
        self.head = self.snake[0]

    def place_snake(self):
        for position in STARTING_POSITION:
            tim = t.Turtle("square")
            tim.penup()
            tim.setpos(x=position[0], y=position[1])
            tim.color("white")
            self.snake.append(tim)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.place_snake()
        self.head = self.snake[0]

    def move(self, prev_pos):
        self.head.forward(MOVE_DISTANCE)
        for _ in self.snake[1:]:
            current_pos = _.pos()
            _.setpos(x=prev_pos[0], y=prev_pos[1])
            prev_pos = current_pos

    def move_fwd(self):
        prev_pos = self.head.pos()
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move(prev_pos)

    def move_back(self):
        prev_pos = self.head.pos()
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move(prev_pos)

    def move_up(self):
        prev_pos = self.head.pos()
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move(prev_pos)

    def move_down(self):
        prev_pos = self.head.pos()
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move(prev_pos)

    def is_colliding(self):
        for _ in self.snake[1:]:
            if self.head.distance(_) <= 0:
                return True
        return False

    def eat(self):
        new_tim = t.Turtle("square")
        new_tim.penup()
        last_tim_pos = self.snake[-1].pos()
        new_tim.setpos(x=last_tim_pos[0], y=last_tim_pos[1])
        new_tim.color("white")
        self.snake.append(new_tim)
