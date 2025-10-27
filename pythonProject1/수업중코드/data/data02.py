# name변수에는 str이 들어감.
# 변수에 값이 들어갈 때 변수에 들어가는 타입이 결정됨.
# 파이썬에서는 어떤 값이 들어가는지에 따라 변수에 다양한 타입이 들어갈 수 있음.
# 동적할당언어 : 변수에 들어가는 값의 유형(타입)에 따라 변수에 들어가는 타입이 결정됨.
#              변수에 들어가는 타입이 어떤 값의 유형을 넣는지에 따라 변함.
#              파이썬, js
# <---> 정적할당언어 : 자바, c++
# String name = "홍길동";

name = "홍길동"
age = 100
tel = '011'

print('이름은 ' + name + '이다.');
print('나이는 ' + str(age) + '이다.');
print('나이는 ' ,age,  '이다.', end=':');
# 파이썬에서 +연산자를 쓸 때는 타입이 동일해야한다.
print('전화번호는',tel , '이다.');
# 파이썬에서는 프린트하고 나서 무조건 엔터가 들어간다.

# 꼭 알아두세요.!!!
# 내가 생각했던 타입이 아닐 수 있어요!
# ai할 때는 빈번함.
print(type(name));
print(type(age));
print(type(tel));


name2 = input("이름입력>> ");
print("당신이 입력한 이름은 " + name2);

age2 = input("나이입력>> "); #100, 외부에서 입력한 타입은 무조건 str, "100"
print("당신의 내년 나이는 " , (int(age2) + 1)); #float()실수로 변환
print("당신의 내년 나이는 " + str((int(age2) + 1))); #float()실수로 변환
# 자바스크립트에서는 parseInt(), parseFloat()

# 한줄복사 : 컨트롤 + D

# C:\pythonProject\.venv\Scripts\python.exe C:\pythonProject\pythonProject1\data\data02.py
# 이름은 홍길동이다.
# 나이는 100이다.
# 나이는  100 이다.:전화번호는 011 이다.
# <class 'str'>
# <class 'int'>
# <class 'str'>
# 이름입력>> 트럼프
# 당신이 입력한 이름은 트럼프
# 나이입력>> 100
# 당신의 내년 나이는  101
# 당신의 내년 나이는 101
#
# Process finished with exit code 0


