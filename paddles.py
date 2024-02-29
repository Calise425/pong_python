from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.shapesize(1.0, 5.0, 1)
        self.goto(location)

    def move_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -250:
            self.backward(20)
