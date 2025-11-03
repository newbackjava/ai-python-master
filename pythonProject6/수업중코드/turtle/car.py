import random
import threading
import time
from tkinter import *

from navigator_updater.widgets import LabelBase


class RacingCar:
    name = ""
    counter = 0

    def __init__(self, name):
        print("차 한대 만들어짐.  이름은 >> ", name)

    def runCar(self, label, x1, y2):
        print("와~~~ 달려 달려.!!")
        while True:
            # x축 랜덤한 값 얻어서 x축에다가 더해줘야함.
            jump = random.randint(1, 10)
            x1 = x1 + jump

            if x1 >= 500:
                print("게임종료")
                break
            label.place(x = x1, y = y2)
            time.sleep(1)


def run_start():
    print("자동차 객체 3대 만들고, 스레드도 만들고!!!")

    c1 = RacingCar("car1")
    c2 = RacingCar("car2")
    c3 = RacingCar("car3")

    t1 = threading.Thread(target=c1.runCar, args=(car_label1, 10, 100))
    t2 = threading.Thread(target=c2.runCar, args=(car_label2, 10, 150))
    t3 = threading.Thread(target=c3.runCar, args=(car_label3, 10, 200))

    # cpu스케쥴러에게 스레드만든 것 등록
    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    # tkinter로 이미지 만들기
    window = Tk()
    window.geometry("500x250")
    window.title("자동차 경주 게임")

    b = Button(window, text="멀티 스레드 시작", command=run_start)
    b.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)
    # 자동차 3대 이미지 --> 라벨을 사용할 예정.

    car_label1 = Label(window, text="car1")
    car_label2 = Label(window, text="car2")
    car_label3 = Label(window, text="car3")

    car_label1.place(x = 10, y = 100)
    car_label2.place(x = 10, y = 150)
    car_label3.place(x = 10, y = 200)

    # 맨끝!!
    window.mainloop()
    # 스레드만드는 것은 함수를 따로 만들자.
    # ==> run_start()
