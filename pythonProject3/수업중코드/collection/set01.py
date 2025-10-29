jumsu = [100, 99, 100, 99, 100, 88]

target = set()
for x in jumsu:
    target.add(x)

print(target)

print("-----------")

import random

random.seed(42)

c1 = []
for i in range(1000):
    c1.append(random.randint(1, 1000))

print(len(c1))
print(c1)

c2 = set()
for x in c1:
    c2.add(x)

print(len(c2))
print(c2)

c3 = set(c1) #set은 중복을 제거해 주는 부품
print(len(c3))
print(c3)



