import device as cal

# 함수의 반환값이 있을 때만! print(함수호출!)
print(cal.add(100, 200))
print(cal.minus(100, 200))
print(cal.mul(100, 200))
print(cal.div(100, 200))

#반환값이 있는 경우 반환값을 변수에 넣어둘 수 있다.
result = cal.add(1000, 200)
print(result)

result2 = cal.add(x = 333, y = 222)
print(result2)

result3 = cal.add(200) #default y = 555
print(result3)