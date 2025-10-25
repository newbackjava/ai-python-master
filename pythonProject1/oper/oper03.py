# 논리연산자
# and, or, !

# if 조건1 and 조건2 and 조건3:
#   처리 내용
# 조건1이 False이면 조건2,3을 체크할 필요없음.
# 조건1에 False일 가능성이 제일 큰 것을 넣음.

import tkinter.messagebox as box

saved_id = 'root' #할당연산자
saved_pw = '1234'
data_id = input('당신의 id는>> ')
data_pw = input('당신의 pw는>> ')
if saved_id == data_id and saved_pw == data_pw :
    print('login 성공.')
    box.showinfo('result','로그인 성공.!')
else:
    #pass
    box.showerror('result', '로그인 실패.!')

# if 조건1 or 조건2 or 조건3:
#   처리 내용
# 조건1이 True이면, 조건2,3을 체크할 필요없음.
# 조건1에 True일 가능성이 제일 큰 것을 넣음.
