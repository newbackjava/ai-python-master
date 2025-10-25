food = [] # list()
# food[0] = '커피' --> index가 아직 없음.
food.append('커피')
food[0] = '라떼'
food.append('라면')
food.append('짜장면')
print(len(food))
food[2] = '짬뽕'
print(food)
# del food[1]
# print(food)
# food.remove('라떼')
# print(food)

food.reverse()

print(food)

# food.pop() #del food[len(food) - 1]
# print(food)
# food.pop()
# print(food)

for x in food:
    print(x, end=' ')
print()
for i in range(len(food)):
    print(food[i], end=' ')


