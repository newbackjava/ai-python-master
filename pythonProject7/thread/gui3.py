import turtle

t = turtle.Pen()

while True:
    choice = input('선택1)네모,2)별>> ')
    if choice == '1':
        for _ in range(4):
            t.right(90)
            t.forward(300)
    else:
        for _ in range(10):
            t.right(110)
            t.forward(200)