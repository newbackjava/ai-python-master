# 랜덤한 것을 만들어서 리스트에 집어 넣기

import random

# numbers = []
numbers = [0] * 1000
print(numbers)

others = [55, 77, 99]

random.seed(42)

for i in range(1000):
    # numbers[i] = random.random() # 0~0.999
    numbers[i] = random.randint(-5, 100) # 1~100
    # numbers[i] = random.randrange(1, 100) # 1~99
    # numbers[i] = random.choice(others)

print(numbers)
print(numbers.count(100))
print(numbers.count(-5))

new_list = []
for x in numbers:
    new_list.append(x * 10)

print(new_list)

print(new_list.index(890))
for i in range(1000):
    if new_list[i] == 890:
        print(i)

