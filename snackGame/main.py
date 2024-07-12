import time
import turtle as t
from food import Food
from snake import Snake
from score_board import ScoreBoard

screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snack Game")
screen.tracer(0)


snake = Snake()


screen.listen()
screen.onkeypress(snake.move_fwd, "Right")
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_back, "Left")
screen.onkeypress(snake.eat, "e")

game_is_on = True
food_eaten = False

food = Food()
score_board = ScoreBoard()

while game_is_on:

    current_position = snake.head.pos()
    food_position = food.pos()

    x_diff = abs(current_position[0] - food_position[0])
    y_diff = abs(current_position[1] - food_position[1])

    if x_diff < 20 and y_diff < 20:
        snake.eat()
        food.eat_food()
        score_board.increment_score()

    if current_position[0] >= 300 or current_position[0] <= -300 or current_position[1] >= 300 or current_position[1] <= -300:
        score_board.reset()
        snake.reset()

    if snake.is_colliding():
        score_board.reset()
        snake.reset()

    snake.move(snake.head.pos())
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
