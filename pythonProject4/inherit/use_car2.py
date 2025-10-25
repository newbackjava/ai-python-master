# 새로운 클래스를 만들 때
# 기존의 있던 클래스를 "재사용!"해서
# 만드는 것을 상속이라고 함.
import object.moving as Car

class Sedan(Car):
    person = 0

    def tour(self):
        print('편안하게 여행을 가다.')

class Truck(Car):
    #멤버변수2개, 멤버함수2개
    weight = 0 #멤버변수 3개

    def move(self): #멤버함수3개
        print('짐을 싣고 가다.')


