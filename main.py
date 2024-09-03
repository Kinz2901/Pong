from turtle import Screen
from paddle import Paddle
from ball import Ball 
from score import Score
import time

direction = "up"

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

ball = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
score = Score()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(l_paddle.up, "W")
screen.onkeypress(l_paddle.down, "S")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

while game_is_on:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()
  # if(int(r_paddle.ycor()) < 260 and direction == "up"):
  #   r_paddle.up()
  # else: 
  #   direction ="down"

  # if(int(r_paddle.ycor()) > -260 and direction == "down"):
  #   r_paddle.down()
  # else:
  #   direction ="up"

  if int(ball.distance(l_paddle)) < 50 and int(ball.xcor()) < -320 or int(ball.distance(r_paddle)) < 50 and int(ball.xcor()) > 320:
    ball.bounce_x()

  if ball.xcor() == 400:
    score.l_point()

  if ball.xcor() == -400:
    score.r_point()
    
  
screen.exitonclick()
