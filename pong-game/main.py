from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong Game")
screen.tracer(0)  # This turns animation on/off and set delay for update drawings. Python Turtle documentation.

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
#Right Paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

#Left Paddle
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
score = ScoreBoard()

#TODO: adjust ball speed when hit the paddle
#TODO: there is a bug when using "w" and "s" key to move the left paddle (it behaves differently compared to the up
# and down arrow keys)

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    y_collision = ball.ycor() > 280 or ball.ycor() < -280
    if y_collision:
        ball.bounce_y()

    #Detect collision with right paddle
    """The ball and the paddle have width of 20 pixels each.normally we would check if the distance 
       Between the ball and the paddle is less than 20 pixel, but this work when the ball hits the 
       the paddle center (we are using distance() method). The if statement addresses the issue when the
       ball hits the edge of the paddle."""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect when right paddle misses
    if ball.xcor() > 390:
        ball.ball_move_center()
        ball.move_ball_opposite()
        score.l_points()
    #Detect when left paddle misses
    if ball.xcor() < -390:
        ball.ball_move_center()
        ball.move_ball_opposite()
        score.r_points()



screen.exitonclick()