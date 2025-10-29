import datetime

## 함수정의해보자. ==> datetime이용해서 함수 만들어보세요.
#1. 현재 년월일/시분초를 알아오는 함수
#2. 현재 달과 현재 시각을 알아오는 함수

def get_day():
    return datetime.datetime.today();

def get_month_hour():
    result1 = datetime.datetime.today();
    return result1.month, result1.hour;

print(get_day());
print(get_month_hour());

# 파이썬은 리턴을 여러개 할 수 있다.
# 받는 곳에서는 하나로 묶어서 받는다.

result2 = get_month_hour();
print(type(result2));
# (10, 11)
# <class 'tuple'>
# result2 = 100; --> X
# 여러개의 리턴받은 데이터를 받을 때는
# 읽기전용인 tuple로 받아서 온다.!!!
print("결과는 " + str(result2));
# 튜플은 슬라이싱으로 할 수 있고, 인덱싱도 가능함.
# 리턴이 많은 경우 튜플로 하나로 묶어서 받아오는 것이 편함.
print(result2[0]);
print(result2[1]);

# 리턴이 몇개 안되는 경우 그냥 다 따로 따로 저장해두는 것이 편함.
print("===============")
result3, result4 = get_month_hour();
print(result3);
print(result4);

# 함수 리턴이 여러개인 경우 안쓰고 싶으면 그 자리에 _를 넣어두세요.
_, result44 = get_month_hour();
print(result44);

def get_list(food): #food = 'japan'
    if food == 'korean':
        data = ['냉면', '오미지차', '팥빙수']
    elif food == 'japan':
        data = ['우동', '생면']
    else:
        data = ['라면', '커피']
    return data #반환은 list형!

result5 = get_list("japan");
print(result5);
print(result5[0]);
print(type(result5));

## 함수는 소문자를 쓰자. 단어가 이어지면 _로 연결하자.!
## 대문자로 쓰면 it에서는 클래스로 인식!!
# def Call5():
#     print("---------")
# Call5();

# 파이썬은 여러개 리턴이 가능함.
# 다른 언어에서는 무조건 하나로 묶어서 리턴해야함.

# result1 = datetime.datetime.today()
# print(result1)
# print(type(result1))
# print(result1.year)
# print(result1.month)
# print(result1.hour)

## py파일에는
## 1. 함수만 정의되어있을 수 있고
## 2. 클래스가 정의되어있을 수 있고
## 3. 함수+클래스 함께 정의되어있을 수 있고


## class에는
## 그 부품의 특징(특성, 속성) : property, attribute
## --> 실제로 구현할 때는 변수를 쓴다.!
## 그 부품의 기능들(기능을 수행하기 위한 방법을 정의) : 메서드
## --> 실제로 구현할 때는 함수를 쓴다.!
