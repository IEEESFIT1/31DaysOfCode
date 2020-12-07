from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()
divider = Turtle()

screen. bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

divider.hideturtle()
divider.color('white')
divider.penup()
divider.goto(0,400)
divider.pendown()
divider.goto(0,-400)
divider.speed('fastest')

game_on = True

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
        # Detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()


    #detect when right paddle misses
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    #detect when left paddle misses
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()