# import tkinter
# tkinter.mainloop()

from tkinter import *
from tkinter import messagebox


def login():
    print("login success")
    id2 = id_entry.get() #입력값가지고 온다.
    pw2 = pw_entry.get() #입력값가지고 온다.
    messagebox.showinfo("가지고 온 값", "id2 =" + id2 + ", pw2 =" + pw2)
    # print("id2 =", id2)
    # print("pw2 =", pw2)


w = Tk() #window화면 하나 만들었으,ㅁ.
w.title("Hello World")
w.geometry("500x250")

id = Label(w, text="아이디입력", font=('궁서', 30))
pw = Label(w, text="패스워드입력", font=('궁서', 30))
id_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white')
pw_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white')
b = Button(w,
           text='로그인처리',
           font=('궁서', 30),
           bg='yellow',
           command=login
           )

id.pack();
id_entry.pack();
pw.pack();
pw_entry.pack();
b.pack();
# 맨끝에 오게 해야함.
# 위에서 설정한거 계속 떠있어라! 개념!
w.mainloop()



