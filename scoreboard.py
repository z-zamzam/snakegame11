from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-30, 175)
        self.hideturtle()
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", move=False, align=ALIGNMENT, font=('Courier', 18, 'normal'))

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False, align='left', font=('Courier', 10, 'normal'))
