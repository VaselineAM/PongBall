from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor('white')
        self.penup()
    
    def scorewrite(self,x,score):
        self.goto(x,160)
        self.pendown()
        self.clear()
        self.write(f"Score:  {score}",False,align="center",font=("Arial",18,"normal"))

        
        