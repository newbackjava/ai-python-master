from tkinter import *
import messagebox
from PIL import Image, ImageTk

# 컨트롤 + 쉬프트 + f : 코드 정리

def login():
    print('회원가입 성공')
    id2 = id_entry.get()
    pw2 = pw_entry.get()
    name2 = name_entry.get()
    tel2 = tel_entry.get()
    messagebox.showinfo("회원가입 성공", "id2=" + id2 + "pw2=" + pw2 + "name2=" + name2 + "tel2=" + tel2)


def reset():
    id_entry.delete(0, END)
    pw_entry.delete(0, END)
    name_entry.delete(0, END)
    tel_entry.delete(0, END)


w = Tk()

w.title = "hello world"
w.geometry('500x700')

img = PhotoImage(file='1.png')
top = Label(w, image=img)
top.pack()

id = Label(w, text="id 입력", font=('굴림', 30))
id_entry = Entry(w, font=("굴림", 30), bg='gray', fg='black')
pw = Label(w, text="pw 입력", font=('굴림', 30))
pw_entry = Entry(w, font=("굴림", 30), bg='gray', fg='black')
name = Label(w, text="name 입력", font=('굴림', 30))
name_entry = Entry(w, font=("굴림", 30), bg='gray', fg='black')
tel = Label(w, text="tel 입력", font=('굴림', 30))
tel_entry = Entry(w, font=("굴림", 30), bg='gray', fg='black')

sb = Button(w,
            text='회원가입 버튼',
            font=("굴림", 30),
            fg="gray",
            command=login)
rb = Button(w,
            text='리셋 버튼',
            font=("굴림", 30),
            fg="gray",
            command=reset)

id.pack()
id_entry.pack()

pw.pack()
pw_entry.pack()

name.pack()
name_entry.pack()

tel.pack()
tel_entry.pack()

sb.pack()
rb.pack()
# 위에서 설정한거 계속 떠 있어라
w.mainloop()
