from turtle import Turtle
class Ball:
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
        self.shapesize(shape.r/10)#6
        self.color(color)#7
    def move(self,screen_width,screen_height):
        current_x = self.xcor()#1
        new_x = current_x + dx#2
        current_y = self.ycor()
        new_y = current_y +dy#,3
        
        new_x = current_x + self.dx
        new_y = current_y + self.dy#,3

                
    
        
        
        
        
        
    
    
    
    
    
    
    
    
