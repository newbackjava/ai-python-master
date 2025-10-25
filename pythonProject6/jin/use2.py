
from tkinter import *
from tkinter import messagebox
#버튼 개당 함수 1개
from PIL import ImageTk


def save():
    #입력값 가지고 오고, 일치하는지 확인
    id2 = id_entry.get()
    pw2 = pw_entry.get()
    print('입력한 id는 ', id2, '입력한 pw는 ', pw2)
    # 원래의 id/pw와 입력한 id/pw가 동일한지 판별하여 프린트
    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인 성공', '로그인 성공!')
        print('로그인 성공')
    else:
        messagebox.showinfo('로그인 실패', '로그인 실패!')
        print('로그인 실패')

def read():
    pass

w = Tk()
w.geometry("500x600")
# 라벨을 하나 만들어보자.
icon = PhotoImage(file='r7.png')
top = Label(w, image=icon)
top.pack()

# img = w.PhotoImage(file = "ask_img.jpg")
# img.pack()
id = Label(w,
           text = '아이디 입력',
           font = ('comic sans', 20)
           )
id.pack() #id라는 라벨을 w에 넣어줌
id_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
id_entry.pack()
pw = Label(w,
           text = '암호 입력',
           font = ('comic sans', 20))
pw.pack()
pw_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
pw_entry.pack()
name = Label(w,
           text = '이름 입력',
           font = ('comic sans', 20))
name.pack()
name_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
name_entry.pack()
tel = Label(w,
           text = '연락처 입력',
           font = ('comic sans', 20))
tel.pack()
tel_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
tel_entry.pack()
button = Button(w,
           text='DB에 저장',
           font=('comic sans', 20),
           bg='white',
           command=save
           ) #클릭버튼
button.pack()
read = Button(w,
           text='DB에서 읽어오기',
           font=('comic sans', 20),
           bg='white',
           command=read
           ) #클릭버튼
read.pack()
w.mainloop()