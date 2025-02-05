from turtle import Turtle
import random

BALL_SPEED = 10

class Ball(Turtle):
    """Creates a ball object to be moved on the screen."""
    def __init__(self):
        super().__init__(shape="circle")
        self.create_ball()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.move_speed = 0.4

    def create_ball(self):
        self.color("white")
        #self.ball.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_ball_opposite(self):
       self.x_move *= -1
       self.y_move *= -1

    def bounce_y(self):
        self.y_move *= -1 # reverses the ball direction in y coordinate

    def bounce_x(self):
        self.x_move *= -1 # reverses the ball direction in x coordinate
        self.move_speed *= 0.9
    def ball_move_center(self):
        self.move_speed = 0.4
        self.goto(0,0)
