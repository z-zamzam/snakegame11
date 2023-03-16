import turtle as tt
MOVE_DISTANCE = 20


class Snake(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.new_x = None
        self.new_y = None
        self.turtles = []
        n = 0
        for i in range(3):
            turtle = tt.Turtle("square")
            turtle.penup()
            turtle.setx(n)
            turtle.color("white")
            turtle.speed(1)
            self.turtles.append(turtle)
            n -= 20
        self.head = self.turtles[0]

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            self.new_x = self.turtles[turtle - 1].xcor()
            self.new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(x=self.new_x, y=self.new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def add_turtle(self):
        turtle = tt.Turtle("square")
        turtle.penup()
        self.turtles[-1].goto(x=self.new_x, y=self.new_y)
        turtle.color("white")
        turtle.speed(1)
        self.turtles.append(turtle)
        self.move()
