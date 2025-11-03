import turtle

t = turtle.Pen()

while True:
    choice = input("네모: 1, 별: 2 >> ")
    if choice == "1":
        for _ in range(4):
            t.right(90)
            t.forward(300)
    else:
        for _ in range(10):
            t.right(110)
            t.forward(200)
