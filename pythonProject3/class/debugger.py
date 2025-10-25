from function.inernet.crawl import connect, find
import function.fun02 as f02

connect()
find()

b = 10
a = b + 1
print(a)

a = 200
b = 30
print(a + 100)

for x in range(3):
    a = 333 + x
    b = 333 + x
    print(a, b)

f02.call1()
