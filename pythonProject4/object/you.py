# Car클래스 만들어보세요.
# 속성 2개 이상
# 동작 2개 이상
# __str__재정의
class Car:
    color = None
    speed = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def __str__(self):
        return self.color + " " + str(self.speed)

    def start(self):
        print("출발하다.")
    def stop(self):
        print("멈추다.")

# car1, car2 인스턴스(객체)만들어서
car1 = Car("red", 150)
# car1.color = "red"
# car1.speed = 150

print(car1)

print("-------------")
car2 = Car("blue", 200)
car2.color = "blue"
car2.speed = 200

print(car2)

# 필드값 각각 넣어보고
# 필드값 프린트
# 함수도 호출해서 결과 확인