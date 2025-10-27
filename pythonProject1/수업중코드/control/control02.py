# 유한루프
for i in range(0, 5, 1): #0, 1, 2, 3, 4
    print(i)

for i in [0, 1, 2, 3, 4]: #0, 1, 2, 3, 4
    print(i, '내가 돌아.')

#범위를 100부터 시작해서 100씩 점프, 999까지 생성
for i in range(100, 1000, 100):
    print(i)

count = 0
while True: #무한루프
    if count == 5:
        print('반복문 중지.')
        break #반복문이 중지
    print('내가 돌아.@@@')
    count = count + 1