from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=2,stretch_wid=0.5)
        self.rt(90)
    
    def movedown(self):
        self.forward(20)

    def moveup(self):
        self.backward(20)
