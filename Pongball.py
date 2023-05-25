from turtle import Turtle
import random
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_len=0.4,stretch_wid=0.4)
        self.speed(10)

    def decidestarting(self):
        angle = random.randint(0,30)
        leftorright = random.randint(1,2)
        if leftorright == 1:
            self.setheading(180-angle)
        elif leftorright == 2:
            self.setheading(angle)
    
    def startmove(self):
        self.forward(5)

    def reflection(self, d1, d2, ycoor):
        if d1<10 or d2<10:
            self.setheading(self.heading() -145)
        if ycoor<-180 or ycoor>180:
            self.setheading(self.heading() + 45 - 180)
    
    def reset(self):
        self.goto(0,0)
        self.decidestarting()
        self.startmove()



    
