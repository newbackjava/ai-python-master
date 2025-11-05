from tkinter import *
import messagebox
import diary_db as db

def create_diary():
    day2 = d1_entry.get()
    title2 = title_entry.get()
    content2 = content_entry.get()
    etc2 = etc_entry.get()
    total = day2 + " " + title2 + " " + content2 + " " + etc2
    messagebox.showinfo("결과", total)
    db.create(day2, title2, content2, etc2)
+36
w = Tk()
w.geometry('500x800')
image = PhotoImage(file="diary.png")
top = Label(image=image)
d1 = Label(w, text="날짜:", font=('굴림', 25))
d1_entry = Entry(w, width=100, font=('굴림', 25), bg='yellow')
t1 = Label(w, text="제목:", font=('굴림', 25))
title_entry = Entry(w, width=100, bg='yellow', font=('굴림', 25))
content = Label(w, text="내용:", font=('굴림', 25))
etc = Label(w, text="기타:", font=('굴림', 25))
content_entry = Entry(w, width=100, bg="yellow", font=('굴림', 25))
etc_entry = Entry(w, width=100, bg="yellow", font=('굴림', 25))
btn_w = Button(w, text='db로 저장', command=create_diary, font=('굴림', 45), bg="lime")

top.pack()
d1.pack()
d1_entry.pack()
t1.pack()
title_entry.pack()
content.pack()
content_entry.pack()
etc.pack()
etc_entry.pack()
btn_w.pack()
w.mainloop()
