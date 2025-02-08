from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_high_score())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 255)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    def read_high_score(self):
        with open("data.txt") as f:
            return  f.read()

    def write_high_score(self):
        with open("data.txt", mode="w") as f:
            f.write(str(self.high_score))