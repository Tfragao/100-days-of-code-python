from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Using a tuple here guarantees that the snake size does not change
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
GO_OFF_SCREEN = 1000 # This is just to make the snake disappears from the playing screen.
segments = []

class Snake:
    """Blueprint to handle snakes objects."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """creates a snake object."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(GO_OFF_SCREEN, GO_OFF_SCREEN)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves up the snake on the screen."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves down the snake on the screen."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves left the snake on the screen."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves right the snake on the screen."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)







