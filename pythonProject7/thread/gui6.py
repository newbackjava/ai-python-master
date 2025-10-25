import turtle

player = turtle.Turtle()
y = 0
x = 0
wn = turtle.Screen()


def p_up():
    global y, up
    up = True
    while (up == True):
        y += 50
        player.sety(y)
def p_right():
    global x, right
    right = True
    while (right == True):
        x += 50
        player.setx(x)

def p_left():
    global x, left
    left = True
    while (left == True):
        x -= 50
        player.setx(x)


def p_down():
    global y, down
    down = True
    while (down == True):
        y -= 50
        player.sety(y)


def up_stop():
    global up
    up = False


def down_stop():
    global down
    down = False
def right_stop():
    global right
    right = False


def left_stop():
    global left
    left = False


wn.listen()
wn.onkeypress(p_up, "w")
wn.onkeypress(p_down, "space")
wn.onkeypress(p_right, "e")
wn.onkeypress(p_left, "q")
wn.onkeyrelease(up_stop, "w")
wn.onkeyrelease(down_stop, "space")
wn.onkeyrelease(right_stop, "e")
wn.onkeyrelease(left_stop, "q")
wn.mainloop()
