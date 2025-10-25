from tkinter import *
from tkinter import messagebox

from pythonProject6.db.dao_class2 import DAO

def save():
    # 1) 입력한 값 가지고 와야함.
    id = id_entry.get()
    name = name_entry.get()
    url = url_entry.get()
    img = img_entry.get()

    # 2) vo에 넣어줌.(tuple)
    vo = (id, name, url, img)

    # 3) dao객체 생성후, 해당 함수 호출!
    dao = DAO()
    result = dao.create(vo)

    # 4) return값이 1이면, 성공!, 아니면 실패!
    if result == 1:
        messagebox.showinfo('결과', 'db에 저장 성공@@')
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        url_entry.delete(0, END)
        img_entry.delete(0, END)
    else:
        messagebox.showinfo('결과', 'db에 저장 실패@@')

def read():
    # id에 입력을 먼저 한 후,
    # 버튼을 누르면 해당 id의 정보를 db에서 검색해온다.
    id = id_entry.get()
    dao = DAO()
    row = dao.read(id)
    print('검색결과>> ', row)
    name_entry.insert(0, row[1])
    url_entry.insert(0, row[2])
    img_entry.insert(0, row[3])

window = Tk()
window.geometry('500x600')
icon = PhotoImage(file='r7.png')
top = Label(window, image=icon)
top.pack()

id_label = Label(window, text='ID입력')
id_label.pack()
id_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
id_entry.pack()
name_label = Label(window, text='NAME입력')
name_label.pack()
name_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
name_entry.pack()
url_label = Label(window, text='URL입력')
url_label.pack()
url_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
url_entry.pack()
img_label = Label(window, text='IMG입력')
img_label.pack()
img_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
img_entry.pack()
save = Button(window, width=30, height=3,
              bg='green',
              font=('애플 고딕', 20),
              text='DB에 저장',
              command=save
              )
save.pack()
read = Button(window, width=30, height=3,
              bg='green',
              font=('애플 고딕', 20),
              text='DB에서 읽기',
              command=read
              )
read.pack()
window.mainloop()
