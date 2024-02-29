from turtle import Screen
from scoreboard import Scoreboard
from center_line import CenterLine
from paddles import Paddle
from ball import Ball
import time

# Locations for the right and left paddles
RIGHT_LOCATION = (400, 0)
LEFT_LOCATION = (-410, 0)

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

center_line = CenterLine()
scoreboard = Scoreboard()
paddle_left = Paddle(LEFT_LOCATION)
paddle_right = Paddle(RIGHT_LOCATION)
ball = Ball()

screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")
screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")

# The game loop to provide continuous motion of the ball
game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.refresh_time)

    # Detect collision with the top or bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect Scoring for either side
    if ball.xcor() < -440:
        scoreboard.increase_score("r")
        ball.refresh()
        ball.bounce_x()

    if ball.xcor() > 440:
        scoreboard.increase_score("l")
        ball.refresh()
        ball.bounce_x()

    # Detect collision with right or left paddles
    if -410 < ball.xcor() < -390 or 400 > ball.xcor() > 380:
        if paddle_right.distance(ball) < 60 or paddle_left.distance(ball) < 60:
            ball.bounce_x()

screen.exitonclick()
