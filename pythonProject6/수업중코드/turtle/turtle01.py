import turtle

t = turtle.Pen()

while True:
    direction = input("왼쪽: left, 오른쪽: right >> ")
    angle = int(input("각도 >> "))
    if direction == "left":
        t.left(angle) # 왼쪽으로 angle만큼 틀어라.
        t.forward(150) # 앞으로 150만큼 가라.
    else:
        t.right(angle)
        t.forward(150)