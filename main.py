from turtle import Turtle, Screen
from Paddle import Paddle
from Pongball import ball
from divider import Divider
from ScoreBoard import Scoreboard
import time 


myscreen = Screen()

myscreen.tracer(0)
myscreen.setup(800,400)
myscreen.bgcolor('black')
paddle1 = Paddle()
paddle2 = Paddle()
ball1 = ball()
score1 = Scoreboard()
score2 = Scoreboard()
score1.scorewrite(-100,0)
score2.scorewrite(100,0)
paddle1.goto(-380,0)
paddle2.goto(380,0)
divider = Divider()
divider.createdivider()

score1score = 0
score2score = 0

myscreen.onkeypress(paddle2.movedown,"Down")
myscreen.onkeypress(paddle2.moveup,"Up")   
myscreen.onkeypress(paddle1.movedown,"s")
myscreen.onkeypress(paddle1.moveup,"w")  
myscreen.listen()

is_game_on = True
ball1.decidestarting()
while is_game_on:
    myscreen.update()
    ball1.startmove()
    distance1 = ball1.distance(paddle1)
    distance2 = ball1.distance(paddle2)
    ball1.reflection(distance1,distance2,ball1.ycor())
    if ball1.xcor()>390 or ball1.xcor()<-390:
        if ball1.xcor()>390:
            score1.clear()
            score1score = score1score + 1
            score1.scorewrite(-100,score1score)
        if ball1.xcor()<-390:
            score2.clear()
            score2score = score2score + 1
            score2.scorewrite(100,score2score)
        ball1.reset()
        time.sleep(1)


myscreen.mainloop()


