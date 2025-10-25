# 반복문은 2가지 경우에 사용
# 1)횟수를 세기위해서
# 2)반복하면서 어떤 처리를 하기 위해서

for _ in range(5):  # [0, 1, 2,  3, 4]
    print('환영합니다.')

sum = 0
for n in range(1, 6):
    sum = sum + n
print(sum)
