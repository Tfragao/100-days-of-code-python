from turtle import Turtle

Y_OFFSET = 20

class Paddle(Turtle):
    """A blueprint to create paddle objects."""
    def __init__(self, x_pos, y_pos):
        super().__init__(shape="square")
        #self.paddle = Turtle(shape="square")
        self.create_paddle()
        self.paddle_position(x_pos, y_pos)

    def create_paddle(self):
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def up(self):
        """Moves the paddle up on the screen."""
        new_y = self.ycor() + Y_OFFSET
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the paddle down on the screen."""
        new_y = self.ycor() - Y_OFFSET
        self.goto(self.xcor(), new_y)

    def paddle_position(self, x_pos, y_pos):
        """Set a position of the paddle"""
        self.setposition(x_pos, y_pos)
