import math
import turtle
import time
import random
from ball import Ball

turtle.tracer(0) #2
turtle.hideturtle()#3

RUNNING = True#4
SLEEP = 0.05#4
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2#4
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2#4
turtle.bgpic("large.gif")

################part 0 : Creating the Balls###################
MY_BALL = Ball(0,0,0,0,30,"red")#1

NUMBER_OF_BALLS = 5#2(1)
MINIMUM_BALL_RADIUS = 10#2(2).
MAXIMUM_BALL_RADIUS = 30#2(3)
MINIMUM_BALL_DX = -5#2(4)
MAXIMUM_BALL_DX = 5#2(5)
MINIMUM_BALL_DY = -5#2(6)
MAXIMUM_BALL_DY = 5#2(7)

Balls = []#3

for i in range (NUMBER_OF_BALLS):##########?????
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
 	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
 	dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
 	r =  random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
 	color = (random.random(), random.random(), random.random()) # geerate random color
	ball = Ball(x, y, dx, dy, r, color)# Creates new ball
	Balls.append(ball)

#############Part 1: Move All Balls
def  move_all_ball():
	for ball in Balls:#1-2
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)#1-2

##########Part 2: Check for ball collisions

def collide(ball_a , ball_b):#Create a function collide that takes two Ball objects as arguments: ball_a and ball_b

	if ( ball_a == ball_b):#Check if ball_a and ball_b are the same. If yes, return False
		return False
	distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))#Calculate the distance between the centers of the balls
	if (distance + 10 <= ball_a.r + ball_b.r):
		return True
	else:
		return False

	#######Part 3: Check collisions for all balls
def check_all_balls_collision():
	for ball_a in Balls:
		for ball_b in Balls:## Create a nested for-loop in which both loops iterate through BALLS. Use ball_a as the variable name for the first loop and ball_b for the second loop
			if collide (ball_a , ball_b):
				radius_a = ball_a.r
				radius_b = ball_b.r

				X_coordinate = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				Y_coordinate = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
 				X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
 				Y_axis_speed  = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
 				Radius =  random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
 				color = (random.random(), random.random(), random.random()) # geerate random color
	 
 				while X_axis_speed == 0:
 					X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
 				while Y_axis_speed == 0:
 					Y_axis_speed  = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
 				if (ball_a.r > ball_b.r): #ball b is smaller
 					ball_b.goto(X_coordinate , Y_coordinate)
 					ball_b.dx = X_axis_speed
 					ball_b.dy = Y_axis_speed
 					ball_b.r = Radius
 					ball_b.shapesize(ball_b.r/10)

 					ball_a.r+=5
 					ball_a.shapesize(ball_a.r/10)
 				else:
 					ball_a.goto(X_coordinate , Y_coordinate)
 					ball_a.dx = X_axis_speed
 					ball_a.dy = Y_axis_speed
 					ball_a.r = Radius
 					ball_a.shapesize(ball_a.r/10)
					ball_b.r+=5
 					ball_b.shapesize(ball_b.r/10)
 #########part 4: Check collision with my ball

def check_myball_collision():
	for ball in Balls:
		if collide (MY_BALL , ball):#Write a for-loop to iterate through all the balls
			X_coordinate = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			Y_coordinate = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			Y_axis_speed  = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			Radius =  random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			color = (random.random(), random.random(), random.random()) # geerate random color

			while X_axis_speed == 0:
				X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			while Y_axis_speed == 0:
				Y_axis_speed  = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			if (MY_BALL.r > ball.r): #ball is smaller
				ball.goto(X_coordinate , Y_coordinate)
				ball.dx = X_axis_speed
				ball.dy = Y_axis_speed
				ball.r = Radius
				ball.shapesize(ball.r/10)
				ball.color(color)

				MY_BALL.r+=1
				MY_BALL.shapesize(MY_BALL.r/10)
			else:
				return False
	return True

####Part 5: Movearound#####################3
def movearound(event): #Create a function called movearound that takes an argument event
	X_coordinate = event.x - SCREEN_WIDTH
	Y_coordinate = SCREEN_HEIGHT - event.y
	MY_BALL.goto(X_coordinate , Y_coordinate)

######Part 5.1: Move it!
turtle.getcanvas().bind("<Motion>", movearound)#call the function movearound everytime the mouse moves by adding this line to my code
turtle.getscreen().listen()



####Part 6: The While Loop
while (RUNNING):
	move_all_ball()#. Move all the balls in the game and then check for any collisions between all balls
	check_all_balls_collision()#. Move all the balls in the game and then check for any collisions between all balls
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)

turtle.mainloop()













