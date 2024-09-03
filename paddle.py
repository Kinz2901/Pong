from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):
  def __init__(self, position, direction="up"):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(position)
    self.direction = direction

  def up(self):
    if(int(self.ycor()) < 260):
      new_y = self.ycor() + 20
      self.goto(self.xcor(), new_y)

  def down(self):
    if(int(self.ycor()) > -260):
      new_y = self.ycor() - 20
      self.goto(self.xcor(), new_y)

