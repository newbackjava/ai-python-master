import turtle


def click(x, y):
    print(x, y) #100
    w = 50
    h = 50
    sx1 = x - w  #50
    sy1 = y - h  #50
    # sx2 = x + w / 2 #150 / 2 = 75
    # sy2 = y + h / 2

    global myTurtle
    myTurtle.goto(sx1, sy1)


myTurtle = turtle.Turtle('turtle')
turtle.title('거북이 go!')
myTurtle.pensize(20)
turtle.onscreenclick(click, 1)
turtle.done()
