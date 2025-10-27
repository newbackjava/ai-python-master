# 비교연산자
# ==, !=, >=, >, <=, <
# 스트링도 비교연산자로 비교 가능

import tkinter.messagebox as box

save_id = 'root' #회원가입할 때의 id
save_pw = '1234'
data_id = input("당신의 가입한 id는>> ");
data_pw = input("당신의 가입한 pw는>> ");

result1 = save_id == data_id;
result2 = save_pw == data_pw;

print(result1, result2);

if result1 and result2: #or
    print("로그인 성공.");
    box.showinfo('result결과 ', '로그인 성공')
else:
    # pass #else안에 아무것도 안넣으면 안된다.
    # 무엇을 넣어할지 모르겠으면 일단 pass라고 써놓아야한다.

    box.showerror('result', '로그인 실패.!')
    # title, message는 파라메터(매개변수임)
    # function showinfo(title, message):
    #     print(title, message);




