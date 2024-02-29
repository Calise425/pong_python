from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.width(5)
        self.draw_line()

    def draw_line(self):
        self.penup()
        self.goto(0,320)
        self.color("white")
        self.setheading(270)
        self.width(5)
        for num in range(25):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
