from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
       Turtle.__init__(self)
       self.shape("circle")
       self.shapesize(radius)
       self.color(color)
       self.speed(speed)

ball1 = Ball(7,"red",5)
ball2 = Ball(8,"red",5)
def check_collision(ball1, ball2):
    ball1.xcor()
    ball1.ycor()
    ball2.xcor()
    ball1.ycor()
    ball1.pos()



