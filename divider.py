from turtle import Turtle
class Divider(Turtle):
    def __init__(self):
        super().__init__()
        #self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=0.2,stretch_wid=0.1)
    
    def createdivider(self):
        for x in range(-200,+200,20):
            self.goto(0,x)
        self.ht()