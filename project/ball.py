#https://github.com/meet-projects/yl1201718
from turtle import Turtle
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
        self.penup()#2
        self.goto(x,y) #3
        self.shape('circle')#5
        self.shapesize(self.r/10)#6
        self.color(color)#7
    def move(self,screen_width,screen_height):
        current_x = self.xcor()#1
        current_y = self.ycor()
                
        new_x = current_x + self.dx#2,1 Get the x coordinates of the ball and save it inside a variable called current_x

        new_y = current_y + self.dy#,3Get the y coordinates of the ball and save it inside a variable called current_y


        right_side_ball = new_x + self.r#4 Get the right side of the ball (hint new x coordination + the radius) and save it inside a variable called right_side_ball

        up_side_ball = new_y+ self.r#
        left_side_ball = new_x - self.r#
        down_side_ball = new_y-self.r#
        self.goto(new_x,new_y)#Let the ball go to the new x and y coordinates
        if new_x > screen_width/2:#  right side if new_x is bigger than the screen_width/2, than bounce it up
            self.dx = -self.dx
        if  new_x < (-1)*screen_width/2:# left side, need explenation!!!!!!!
            
            self.dx = -self.dx
        if new_y > screen_height/2:#up
            self.dy = -self.dy#### need explenation
        if new_y < (-1)*screen_height/2:# down
            self.dy = -self.dy




            
            
            
        
        
            
        
            
            
            
        
        
        
        
        
    
    
    
    
    
    
    
    
