import random

target = random.randint(1, 100)
# print(target)
cnt = 0
while True:
    number = int(input('숫자를 입력>>'))
    cnt += 1
    if number != target:
        if(number > target):
            print('too big')
        else:
            print('too small')
    else:
        print('correct!')
        print('try cnt>> ', cnt)
        break