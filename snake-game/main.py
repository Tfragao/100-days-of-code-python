from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600, startx=-800, starty=-200)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15: # we gave a bit of buffer has the food is 10 x 10
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    #Detect collision with wall
    x_collision = snake.head.xcor() > 280 or snake.head.xcor() < -280
    y_collision = snake.head.ycor() > 280 or snake.head.ycor() < -280
    if x_collision or y_collision:
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()