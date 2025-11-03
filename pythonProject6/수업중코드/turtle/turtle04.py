import turtle
import random

colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

def leftClick(x, y):
    print(x, " ", y)

    #네모 전체 크기의 가로
    #네모 전체 크기의 세로
    width = 200
    height = 200

    # 클릭한 위치값으로 계산함.


    # 4개의 좌표를 구해서 그려라.
    sx1 = x - width/2
    sy1 = y - height/2
    sx2 = x + width / 2
    sy2 = y + height / 2

    myTurtle.penup()  # 이동만!
    myTurtle.goto(sx1, sy1)

    myTurtle.pencolor(random.choice(colors))
    myTurtle.pendown()  # 그림 그리기 위해서  펜을 내려

    myTurtle.goto(sx1, sy2)
    myTurtle.goto(sx2, sy2)
    myTurtle.goto(sx2, sy1)
    myTurtle.goto(sx1, sy1)


myTurtle = turtle.Turtle('turtle')
myTurtle.pensize(20)
myTurtle.pencolor('red')
turtle.onscreenclick(leftClick, 1)
turtle.done()
