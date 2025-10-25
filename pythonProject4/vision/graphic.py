import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
#버튼을 눌렀을 때 로그인 기능을 처리해야함.
#특정한 기능은 하나의 함수로 만들어 주면 됨.
#버튼 눌렀을 때 처리하고자 하는 기능하나는 함수하나가 됨.
#함수를 만드는 것을 함수를 정의한다라고 함.
#기능을 프로그래머가 정의하기 때문에 함수를 정의한다라고 표현함.
def login():
    #id입력한 값, pw입력한 값 가지고 와야함.
    #원래 회원가입할 때의 id/pw와 입력한 값을 비교해야함.
    id2 = id_entry.get() #root
    print('입력한 id는 ', id2)
    pw2 = pw_entry.get() #root
    print('입력한 pw는 ', pw2)
    #pw 입력한 값 가지고와서 프린트
    #원래의  id:root/pw:1234
    #원래의 id/pw와 입력한 id/pw가 동일한지 판별하여 프린트
    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인 성공', '축하합니다.')
        result.config(text='로그인 성공@@')
        print('로그인 성공')
        img2 = tkinter.PhotoImage(file='a2.png')
        result2.configure(image=img2)
        result2.image=img2
    else:
        messagebox.showinfo('로그인 실패', '다시해보세요..')
        result.config(text='로그인 실패@@')
        print('로그인 실패')
        img3 = tkinter.PhotoImage(file='a.png')
        result2.configure(image=img3)
        result2.image = img3

def reset():
    id_entry.delete(0,END) #entry값 지움.
    pw_entry.delete(0,END)
    pw_entry.insert(0,'다시 입력') #entry에 값 넣음.
    result.config(text='') #값 텍스트 지움.


w = Tk()
w.geometry("500x900")

id = Label(w, text='ID입력', font=('궁서', 30))
id.pack()

id_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white') #id입력
id_entry.pack()

pw = Label(w, text='PW입력' , font=('궁서', 30)) #pw글자
pw.pack()


pw_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white') #pw입력
pw_entry.pack()

b = Button(w,
           text='로그인 처리',
           font=('궁서', 30),
           bg='yellow',
           command=login
           ) #클릭버튼
b.pack()
b2 = Button(w,
           text='리셋',
           font=('궁서', 30),
           bg='yellow',
           command=reset
           ) #클릭버튼
b2.pack()

result = Label(w, text='결과는 여기에', font=('궁서', 30))
result.pack()

img = tkinter.PhotoImage(file='r5.png')
result2 = Label(w, image=img)
result2.pack()

w.mainloop()