from turtle import Turtle
WIDTH = 5
HEIGTH = 1


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid= WIDTH,stretch_len=HEIGTH)
        self.move(x_pos, y_pos)

    def move(self, x_pos, y_pos):
        self.goto(x_pos, y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.move(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.move(self.xcor(), new_y)

