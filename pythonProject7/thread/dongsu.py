import turtle
import random


# 클릭을 했을 때, 두 가지 그림을 그리는 함수를 만들어보세요.
# 아무거나 둘 선택
# color, size가 변하게
def click(x, y):
    color_list = ['green', 'blue', 'yellow', 'red', 'purple', 'pink']

    print(x, y)

    while True:
        x2 = random.randint(-350, 350)
        y2 = random.randint(-350, 350)
        global my_turtle
        my_turtle.pensize(random.randint(1, 15))
        color_choice = random.choice(color_list)
        my_turtle.pencolor(color_choice)
        print('---', random.randint(1, 2))
        # randint(1,2) : 1~2
        if random.randint(1, 2) == 1:
            size = random.randint(10, 200)

            my_turtle.penup()
            my_turtle.goto(x2, y2)
            my_turtle.pendown()
            y2 += size
            my_turtle.goto(x2, y2)
            x2 += size
            my_turtle.goto(x2, y2)
            y2 -= size
            my_turtle.goto(x2, y2)
            x2 -= size
            my_turtle.goto(x2, y2)
        else:
            size = random.randint(10, 200)
            my_turtle.penup()
            my_turtle.goto(x2, y2)
            my_turtle.pendown()
            for _ in range(5):
                my_turtle.right(145)
                my_turtle.forward(size)

my_turtle = turtle.Turtle('turtle')
turtle.title('거북이로 객체지향 사각형 그리기')
turtle.onscreenclick(click, 1)
# my_turtle.pensize(20)
# my_turtle.pencolor('red')
turtle.done()
