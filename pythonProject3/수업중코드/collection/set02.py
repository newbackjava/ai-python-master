x = 100
y = x

print("x =", x)
print("y =", y)

print("수정후======")
y = 200

print("x =", x)
print("y =", y)

print()

x2 = [1, 2, 3]
y2 = x2 #얕은 복사
y2 = x2.copy() #깊은 복사
# 리스트는 깊은 복사를 해야
# 값의 리스트가 클론됨.!

print("x2 =", x2)
print("y2 =", y2)

print("수정후======")
y2[0] = 999
print("x2 =", x2)
print("y2 =", y2)









