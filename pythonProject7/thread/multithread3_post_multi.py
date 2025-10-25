import random
import threading
import time
from tkinter import *
from tkinter import messagebox


class RacingCar:
    #멤버변수
    name = ''
    counter = 0 #클래스 변수

    #초기화함수
    def __init__(self, name):
        #self: 클래스로 생성한 객체!
        #c1 = RacingCar('appleCar')
        #self == c1
        #c1.name = 'appleCar'
        self.name = name
    #멤버함수
    def runCar(self, label, x1, y1):

        while True:
            jump = random.randint(1,10)
            print(jump)
            x1 = x1 + jump
            if x1 >= 500:
                RacingCar.counter += 1
                messagebox.showinfo('결과>> ',
                                    str(RacingCar.counter) + ': ' +
                                    self.name)
                break
            label.place(x = x1 + jump, y = y1)
            time.sleep(0.05)

def run_start():
    # 라벨 객체 만들어서 window에 끼워넣어야 함.
    print('call ok!!')
    ## 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.
    c1 = RacingCar('appleCar')
    c2 = RacingCar('summerCar')
    c3 = RacingCar('springCar')
    c4 = RacingCar('appleCar2')
    c5 = RacingCar('summerCar2')
    c6 = RacingCar('springCar2')
    c7 = RacingCar('appleCar3')
    c8 = RacingCar('summerCar3')
    c9 = RacingCar('springCar3')


    t1 = threading.Thread(target=c1.runCar, args=(car_label1, 10, 100))
    t2 = threading.Thread(target=c2.runCar, args=(car_label2, 10, 150))
    t3 = threading.Thread(target=c3.runCar, args=(car_label3, 10, 200))
    t4 = threading.Thread(target=c1.runCar, args=(car_label4, 10, 250))
    t5 = threading.Thread(target=c2.runCar, args=(car_label5, 10, 300))
    t6 = threading.Thread(target=c3.runCar, args=(car_label6, 10, 350))
    t7 = threading.Thread(target=c1.runCar, args=(car_label7, 10, 400))
    t8 = threading.Thread(target=c2.runCar, args=(car_label8, 10, 450))
    t9 = threading.Thread(target=c3.runCar, args=(car_label9, 10, 500))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()

if __name__ == '__main__':
    window = Tk()
    window.geometry("500x550")
    window.title('멀티 스레드 자동차 경주')
    b = Button(window, text='멀티 스레드 시작',
               command=run_start)
    b.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)
    car1_img = PhotoImage(file='car1.gif')
    car2_img = PhotoImage(file='car2.gif')
    car3_img = PhotoImage(file='car3.gif')
    car_label1 = Label(window, image=car1_img)
    car_label1.place(x = 10, y = 100)
    car_label2 = Label(window, image=car2_img)
    car_label2.place(x = 10, y = 150)
    car_label3 = Label(window, image=car3_img)
    car_label3.place(x = 10, y = 200)
    car_label4 = Label(window, image=car1_img)
    car_label4.place(x = 10, y = 250)
    car_label5 = Label(window, image=car2_img)
    car_label5.place(x = 10, y = 300)
    car_label6 = Label(window, image=car3_img)
    car_label6.place(x = 10, y = 350)
    car_label7 = Label(window, image=car1_img)
    car_label7.place(x = 10, y = 400)
    car_label8 = Label(window, image=car2_img)
    car_label8.place(x = 10, y = 450)
    car_label9 = Label(window, image=car3_img)
    car_label9.place(x = 10, y = 500)
    window.mainloop()
