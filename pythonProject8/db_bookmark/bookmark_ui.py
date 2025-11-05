import bookmark_db as db
from tkinter import *
from tkinter import messagebox

# id = input("ID를 입력해주세요.")
# name = input("이름을 입력해주세요.")
# url = input("웹주소를 입력해주세요.")
# img = input("이미지 이름을 입력해주세요.")
#
# data = [id, name, url, img]

# db.create(data)

# db.read(data)

def write():
    id_data = id_entry.get()
    name_data = name_entry.get()
    url_data = url_entry.get()
    img_data = img_entry.get()

    data = [id_data, name_data, url_data, img_data]
    result = db.create(data)
    if result >= 1:
        messagebox.showinfo("저장", "성공적으로 저장했습니다.")

def read():
    data = id_entry.get()
    result = db.select(data)
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    url_entry.delete(0, END)
    img_entry.delete(0, END)

    id_entry.insert(0, result[0])
    name_entry.insert(0, result[1])
    url_entry.insert(0, result[2])
    img_entry.insert(0, result[3])
    messagebox.showinfo("불러오기", "성공적으로 불러왔습니다.")

def read_all():
    data = db.select_all()
    result = '\n'.join(map(str, data))
    messagebox.showinfo("전체 조회", result)



window = Tk()
window.title("Bookmark")

img = PhotoImage(file="Cute_Cat_Bookmarks.png")
header = Label(window, image=img)
header.grid(row=0, column=0, columnspan=3)


id = Label(window, text="ID입력", font=('Pretendard', 20, 'bold'))
name = Label(window, text="이름 입력", font=('Pretendard', 20, 'bold'))
url = Label(window, text="URL입력", font=('Pretendard', 20, 'bold'))
img_name = Label(window, text="IMG입력", font=('Pretendard', 20, 'bold'))

id_entry = Entry(window, font=('Pretendard', 15, 'bold'))
name_entry = Entry(window, font=('Pretendard', 15, 'bold'))
url_entry = Entry(window, font=('Pretendard', 15, 'bold'))
img_entry = Entry(window, font=('Pretendard', 15, 'bold'))

save = Button(window, text="DB에 저장", font=('Pretendard', 15, 'bold'), command=write)
load = Button(window, text="DB에서 불러오기", font=('Pretendard', 15, 'bold'), command=read)
retrieve = Button(window, text="DB 전체 조회하기", font=('Pretendard', 15, 'bold'), command=read_all)


id.grid(row=1, column=0, padx=5, pady=5)
name.grid(row=2, column=0, padx=5, pady=5)
url.grid(row=3, column=0, padx=5, pady=5)
img_name.grid(row=4, column=0, padx=5, pady=5)

id_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
name_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
url_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
img_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

save.grid(row=5, column=0, padx=5, pady=5)
retrieve.grid(row=5, column=1, padx=5, pady=5)
load.grid(row=5, column=2, padx=5, pady=5)

window.mainloop()