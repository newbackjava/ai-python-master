import random
import turtle

# 클릭을 했을 때, 두 가지 그림을 그리는 함수를 만들어보세요.
# 아무거나 둘 선택
# color, size가 변하게!
def click(x, y):
    print(x, y)
    x2 = random.randint(-400,400)
    y2 = random.randint(-400,400)
    pen_size = random.randint(1, 30)
    color_list = ['green','blue','yellow','red', 'purple','pink']
    # color_choice = color_list[random.randint(0, 7)]
    color_choice = random.choice(color_list)
    my_turtle.pensize(pen_size)
    my_turtle.pencolor(color_choice)

    # my_turtle.penup() #이동만!
    # my_turtle.goto(x, y)
    # my_turtle.pendown()
    # my_turtle.goto(x2,y2)
    my_turtle.goto(x,y)

my_turtle = turtle.Turtle('turtle')
#class Turtle:
#   def __init__(self):
#       거북이 화면 가운데에 보이게 해주는 처리
turtle.title('거북이로 객체지향 사각형 그리기')
turtle.onscreenclick(click, 1)
# my_turtle.pensize(20)
# my_turtle.pencolor('red')
turtle.done()

# w = Tk()
# --
# ---
# ---
#
# w.mainloop()