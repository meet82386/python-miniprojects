# PONG: The Famous Arcade Game

# STAPES:

# Create the screen.
# Create and move the paddle
# Create another paddle
# Create a ball and make it move
# Detect collision with ball and bounce
# Detect collision with paddle
# Detect when paddle missed
# Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

paddle = Paddle(360, 0)
cross_paddle = Paddle(-360, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(paddle.move_up, key="Up")
screen.onkeypress(paddle.move_down, "Down")
screen.onkeypress(cross_paddle.move_up, key="w")
screen.onkeypress(cross_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    ball_cords = ball.pos()

    # Detect collisions with wall
    if ball_cords[0] >= 380:
        scoreboard.l_point()
        ball.reset_ball()

    if ball_cords[0] <= -380:
        scoreboard.r_point()
        ball.reset_ball()

    if ball_cords[1] >= 280 or ball_cords[1] <= -280:
        ball.bounce()

    # Detect collision with paddles
    if (ball.distance(paddle) < 50 and ball.xcor() > 320) or (ball.distance(cross_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

print(paddle.score)
print(cross_paddle.score)
screen.exitonclick()
