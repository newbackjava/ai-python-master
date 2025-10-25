import random
import threading
import time
from tkinter import *
from tkinter import messagebox


class RacingCar:
    # 멤버변수
    name = '' #인스턴스 변수
    counter = 0 #클래스 변수

    # 초기화함수
    def __init__(self, name):
        # self: 클래스로 생성한 객체!
        # c1 = RacingCar('appleCar') , c2, c3
        # self == c1
        # c1.name = 'appleCar'
        self.name = name

    # 멤버함수
    def runCar(self, label, x1, y1):
        while True:
            # 랜덤하게 움직일 값을 생성해서
            # 랜덤생성한 jump값을 기존의 x에 더해준다.
            # y축 값은 변하지 않음.
            jump = random.randint(1, 20)
            print(jump)
            x1 = x1 + jump
            if x1 >= 500:
                RacingCar.counter += 1
                messagebox.showinfo('결과>> ',
                                    str(RacingCar.counter) + ': ' +
                                    self.name)
                break
            label.place(x=x1, y=y1)
            time.sleep(0.5)


def run_start():
    # 라벨 객체를 만들어서 window에 끼워넣어야 함.
    print('call ok!!')

    # 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.
    c1 = RacingCar('appleCar')
    c2 = RacingCar('summerCar')
    c3 = RacingCar('springCar')

    t1 = threading.Thread(target=c1.runCar, args=(car_label1, 10, 100))
    t2 = threading.Thread(target=c2.runCar, args=(car_label2, 10, 150))
    t3 = threading.Thread(target=c3.runCar, args=(car_label3, 10, 200))

    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    window = Tk()
    window.geometry("500x250")
    window.title('멀티 스레드 자동차 경주')
    b = Button(window, text='멀티 스레드 시작', command=run_start)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)  # fill x,y축 가득 채우는 것. ipadx 여백
    car_label1 = Label(window, text='appleCar')
    car_label1.place(x=10, y=100)

    car_label2 = Label(window, text='summerCar')
    car_label2.place(x=10, y=150)

    car_label3 = Label(window, text='springCar')
    car_label3.place(x=10, y=200)

    window.mainloop()

c1 = RacingCar('appleCar')
c2 = RacingCar('summerCar')
c3 = RacingCar('springCar')

t1 = threading.Thread(target=c1.runCar)
t2 = threading.Thread(target=c2.runCar)
t3 = threading.Thread(target=c3.runCar)

t1.start()
t2.start()




