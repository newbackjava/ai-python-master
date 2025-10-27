# 비교연산자
# ==, !=, >=, >, <=, <
# 스트링도 비교연산자로 비교 가능

import tkinter.messagebox as box

save_id = 'root' #회원가입할 때의 id
data_id = input("당신의 가입한 id는>> ");

result = save_id == data_id;
print(result);

if result:
    print("로그인 성공.");
    box.showinfo('result결과 ', '로그인 성공')

    # title, message는 파라메터(매개변수임)
    # function showinfo(title, message):
    #     print(title, message);




