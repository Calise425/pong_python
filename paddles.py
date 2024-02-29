from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_value):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.shapesize(1.0, 4.0, 1)
        self.goto(x_value, 0)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
