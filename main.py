import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard


game_running = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game!")
screen.tracer(0)

paddle_rigth = Paddle(350,0)
paddle_left = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle_rigth.go_up, "Up")
screen.onkey(paddle_rigth.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

screen.listen()

while game_running:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detection colision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detection colision with the paddle
    if paddle_rigth.distance(ball) < 50 and ball.xcor() > 340 or paddle_left.distance(ball) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when the rigth missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when the left missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()