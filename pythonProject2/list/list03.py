print()
food = [] #감자, 고구마, 양파
for _ in range(3):
    data = input('입력>> ')
    food.append(data)

print(food[1])
print(food[0:2])
print(food[1:])
food[0] = '라면'
print(food)
