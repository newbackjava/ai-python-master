import turtle
import random

colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

def leftClick(x, y):
    print(x, " ", y)
    myTurtle.penup() # 이동만!
    myTurtle.goto(x, y)
    myTurtle.pencolor(random.choice(colors))
    myTurtle.pendown() # 그림 그리기 위해서  펜을 내려
    myTurtle.goto(x, -y)

myTurtle = turtle.Turtle('turtle')
myTurtle.pensize(20)
myTurtle.pencolor('red')
turtle.onscreenclick(leftClick, 1)
turtle.done()
