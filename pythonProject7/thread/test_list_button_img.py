import base64
import io
import os
import random
import ssl
import threading
import time
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class RacingCar:
    # 멤버변수
    name = ''
    counter = 0  # 클래스 변수

    def __init__(self, name):
        # self: 클래스로 생성한 객체!
        # c1 = RacingCar('appleCar')
        # c1.name = 'appleCar'
        self.name = name

    # 멤버함수
    def runCar(self, label, x1, y1):

        while True:
            jump = random.randint(1, 10)
            print(jump)
            x1 = x1 + jump
            if x1 >= 500:
                RacingCar.counter += 1
                #messagebox.showinfo('결과>> ',
                                    # str(RacingCar.counter) + ': ' +
                                    # self.name)
                break
            label.place(x=x1 + jump, y=y1)
            time.sleep(0.05)


def run_start():
    # 라벨 객체 만들어서 window에 끼워넣어야 함.
    print('call ok!!')
    ## 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.

    car_list = []
    for i in range(9):
        car_list.append(RacingCar('car' + str(i)))

    thread_list = []
    y_value = 100
    for i in range(0, len(car_list)):
        y_value = y_value + 50
        thread_list.append(threading.Thread(target=car_list[i].runCar,
                                            args=(car_label_list[i],
                                                  10, y_value + 50)))

    for thread_one in thread_list:
        thread_one.start()


if __name__ == '__main__':
    window = Tk()
    window.geometry("500x600")
    window.title('멀티 gui test')
    b = Button(window, text='멀티 스레드 시작',
               command=run_start)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
    car_label_list = []
    y_value = 100
    for i in range(9):
        y_value = y_value + 50

        # car_label = Button(window, text='button' + str(i))
        image_url = "https://item.kakaocdn.net/do/a55eb47ef16882d3ee4ff9cd9bb873579f17e489affba0627eb1eb39695f93dd"

        from PIL import Image

        name = 'test7.png'
        # curl 요청
        os.system("curl " + image_url + " > " + name)

        # img = PhotoImage(file='car1.gif')
        path_dir = '/Users/administrator/Documents/python_project/pythonProject7/thread'

        file_list = os.listdir(path_dir)
        for x in file_list:
            if x == name:
                print(x)
        print('--------' , name)

        img = PhotoImage(file=name)
        car_label = Button(window, image=img, width=200, height=200)
        # car_label = Label(window, image=img)
        # 이미지가 너무 크면 tkinter에는 안들어가요!(jpg < png)
        car_label.image = img
        print(len(car_label_list))
        car_label_list.append(car_label)
        car_label.place(x=10, y=y_value)

    window.mainloop()
