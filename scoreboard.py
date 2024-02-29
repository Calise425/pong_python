from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 40, 'normal')
LEFT_POSITION = (-50, 230)
RIGHT_POSITION = (50, 230)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(LEFT_POSITION)
        self.write(self.score_left, False, align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_POSITION)
        self.write(self.score_right, False, align=ALIGNMENT, font=FONT)

    def increase_score(self, side):
        if side.lower() == "l":
            self.score_left += 1
            self.update_score()
        else:
            self.score_right += 1
            self.update_score()

