from tkinter import *
import messagebox
# from PIL import Image, ImageTk
# 컨트롤 + 쉬프트 + f : 코드 정리

# import cal
# cal1 = cal.Cal()

# import cal as c
# cal1 = c.Cal()

from cal import *

cal1 = Cal()

from sub.cal2 import *

cal2 = Cal2()


# from cal import Cal, Cal2

# Cal.plus()

def plus():
    s1 = int(l1_entry.get())
    s2 = int(l2_entry.get())
    result1 = cal1.plus(s1, s2)
    print(result1)
    messagebox.showinfo("더하기 결과", str(result1))


def minus():
    s1 = int(l1_entry.get())
    s2 = int(l2_entry.get())
    result1 = cal1.minus(s1, s2)
    print(result1)
    messagebox.showinfo("빼기 결과", str(result1))


def mul():
    s1 = int(l1_entry.get())
    s2 = int(l2_entry.get())
    result1 = cal1.mul(s1, s2)
    print(result1)
    messagebox.showinfo("곱하기 결과", str(result1))


def div():
    s1 = int(l1_entry.get())
    s2 = int(l2_entry.get())
    result1 = cal1.div(s1, s2)
    print(result1)
    messagebox.showinfo("나누기 결과", str(result1))


def reset():
    l1_entry.delete(0, END)
    l2_entry.delete(0, END)
    # 라벨에 글자넣기
    # l1.config(text="리셋됨.")
    # l2.config(text="리셋됨.")
    # entry에 글자넣기
    # l1_entry.insert(0, "리셋되었음.")
    # l2_entry.insert(0, "리셋되었음.")

    # 버튼에 글자 넣기
    # plus_b.config(text="리셋되었음.")

    # 버튼에 이미지 넣기
    img2 = PhotoImage(file="1.png")
    plus_b.config(image=img2)
    plus_b.image = img2

w = Tk()

w.title = "나의 계산기"
w.geometry('500x800')
w.config(bg='green')

img = PhotoImage(file='2.png')
top = Label(w, image=img)
top.pack()

l1 = Label(w, text="첫번째 숫자", font=('굴림', 30))
l1_entry = Entry(w, font=("굴림", 30), bg='red', fg='black')
l2 = Label(w, text="두번째 숫자", font=('굴림', 30))
l2_entry = Entry(w, font=("굴림", 30), bg='red', fg='black')

plus_b = Button(w,
                text='plus 버튼',
                font=("굴림", 30),
                bg='yellow',
                fg="gray",
                command=plus
                )
minus_b = Button(w,
                 text='minus 버튼',
                 font=("굴림", 30),
                 bg='yellow',
                 fg="gray",
                 command=minus)
mul_b = Button(w,
               text='mul 버튼',
               font=("굴림", 30),
               bg='yellow',
               fg="gray",
               command=mul)
div_b = Button(w,
               text='div 버튼',
               font=("굴림", 30),
               bg='yellow',
               fg="gray",
               command=div)

reset_b = Button(w,
                 text='내용지우기',
                 font=("굴림", 30),
                 bg='yellow',
                 fg="gray",
                 command=reset)

l1.pack()
l1_entry.pack()

l2.pack()
l2_entry.pack()

plus_b.pack()
minus_b.pack()
mul_b.pack()
div_b.pack()
reset_b.pack()

# 위에서 설정한거 계속 떠 있어라
w.mainloop()
