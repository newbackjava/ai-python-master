import random
import threading


def plus():
    for x in range(101):
        print('증가>> ', x)

# 1부터 100까지 증가
# 증가>> 1
# 증가>> 2

def minus():
    for x in range(100, 0, -1):
        print('감소>> ', x)

# 100부터 1까지 감소
# 감소>> 100
# 감소>> 99

def text():
    text = ['@', '#', '$', '₩']
    for _ in range(100):
        print('특수>> ' + random.choice(text))


# 특수문자를 100번 프린트(@, #, $, ₩)  #text = ['@', '#', '$', '₩']
# 특수>@                            random.choice(text)
# 특수>#

# 스레드 객체로 만들어주고
plus = threading.Thread(target=plus)
minus = threading.Thread(target=minus)
text = threading.Thread(target=text)

# cpu의 스케쥴러에 등록
plus.start()
minus.start()
text.start()
