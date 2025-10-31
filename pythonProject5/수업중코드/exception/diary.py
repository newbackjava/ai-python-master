from tkinter import *

import messagebox

import try07 as file

# 컨트롤 + 쉬프트 + f : 코드 정리

def save():
    print("저장하기 처리")
    
    # 수도코드(가짜코드, 스크립트)
    # 1. 입력한 데이터 가지고 오기
    day_value = day_entry.get()
    title_value = title_entry.get()
    content_value = content_entry.get()
    print(day_value,'',title_value,'',content_value)
    # 2. 파일 저장하는 모듈의 함수 호출
    #    입력한 데이터 함수에 전달
    file.file_save(day_value, title_value, content_value)
    messagebox.showinfo("일기장 저장", "일기장 저장 처리 시작함.")
    # 입력한 값 지워라 처리 추가하면 더 좋겠음.
    day_entry.delete(0, END)
    title_entry.delete(0, END)
    content_entry.delete(0, END)

def read():
    print("읽어오기 처리")
    # 1. 날짜입력값 가지고 오기
    day_value = day_entry.get();
    print(day_value)

    # 2. 파일읽어오는 함수에 날짜값 주면서 
    #    파일 읽은 내용 받아와서 변수에 저장
    result = file.file_read(day_value)
    print(result)

    #  # ['2025-11-02\n', '일요일\n', '내일은 월요일이야!!\n']
    # 3. UI에 넣기
    # 만약에 입력한 날짜에 일기가 없으면 []를 리턴받음.
    if len(result) > 0 :
        title_entry.insert(0, result[1]);
        content_entry.insert(0, result[2]);
    else:
        messagebox.showinfo("일기없음", "해당 날짜의 일기가 없음.")


w = Tk()
w.title = "나의 일기장"
w.geometry('700x900')
w.config(bg='green')

img = PhotoImage(file='a2.png', height=500)
top = Label(w, image=img)
top.pack()

day = Label(w, text="날짜: ", font=('굴림', 30))
day_entry = Entry(w, font=("굴림", 30), bg='red', fg='black')

title = Label(w, text="제목: ", font=('굴림', 30))
title_entry = Entry(w, font=("굴림", 30), bg='red', fg='black')

content = Label(w, text="내용: ", font=('굴림', 30))
content_entry = Entry(w, font=("굴림", 30), bg='red', fg='black')

file_save = Button(w,
                   text='파일로 쓰기',
                   font=("굴림", 30),
                   bg='yellow',
                   fg="gray",
                   command=save)

file_read = Button(w,
                   text='파일로 읽기',
                   font=("굴림", 30),
                   bg='yellow',
                   fg="gray",
                   command=read)

day.pack()
day_entry.pack()

title.pack()
title_entry.pack()

content.pack()
content_entry.pack()

file_save.pack()
file_read.pack()
# 위에서 설정한거 계속 떠 있어라
w.mainloop()
