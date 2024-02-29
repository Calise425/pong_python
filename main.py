from turtle import Screen
from scoreboard import Scoreboard
from center_line import CenterLine
from paddles import Paddle
from ball import Ball
import time

RIGHT_X = 400
LEFT_X = -410

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

center_line = CenterLine()
scoreboard = Scoreboard()
paddle_left = Paddle(LEFT_X)
paddle_right = Paddle(RIGHT_X)
ball = Ball()

screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")
screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")


game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(0.02)


screen.exitonclick()
