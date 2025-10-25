import datetime as dt
# - 현재 시각을 찍는 스레드 100번
import threading
import time

dt_object = dt.datetime

print(dt_object)
def dt():
    for _ in range(100):
        time.sleep(5)
        print('현재시각> ', dt_object.now())

# - 리스트에 있는 먹고 싶은 음식 목록 10개를 찍는 스레드
# def food():
#     food_list = ['사과','배','무','배추','된장','고추장',
#                  '커피','물','쥬스','오이']
#

def food():
    food_list = ['사과','배','무','배추','된장','고추장',
                 '커피','물','쥬스','오이']
    for one in food_list:
        time.sleep(10)
        print('과일> ', one)

# - 1부터 500까지 카운트하는 스레드
def plus():
    for x in range(500):
        time.sleep(1) #time.sleep(1000)
        print('카운트> ', x)

# 스레드 객체로 만들어주고
plus = threading.Thread(target=plus)
dt = threading.Thread(target=dt)
food = threading.Thread(target=food)

# cpu의 스케쥴러에 등록
plus.start()
dt.start()
food.start()