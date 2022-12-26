from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.ball_speed = 0.01
        self.x_move = 10
        self.y_move = 10
        self.move()

    def move(self):
        x_value = self.xcor() + self.x_move
        y_value = self.ycor() + self.y_move
        self.goto(x_value, y_value)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.ball_speed *= 0.9
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.01
        self.bounce_x()
