## 틀역할!!!
class Car:
    # Car들의 공통된 특징(특성, 속성, 항목, 필드)
    # 색, 스피드 --> 변수(속성)
    color = None
    speed = 0

    # Car를 가지고 할 수 있는 기능(동작)
    # 시동걸다. 멈추다 --> 함수(메서드)
    def start(self):
        print("차가 출발하다.")
    def stop(self):
        print("차가 멈추다.")

c1 = Car() #틀인 class로 차한대 만들었음.
c1.color = "red"
c1.speed = 160
print(c1.color, c1.speed)
c1.start()
c1.stop()

c2 = Car() #틀인 class로 차한대 만들었음.


c3 = Car() #틀인 class로 차한대 만들었음.
c4 = Car() #틀인 class로 차한대 만들었음.
c5 = Car() #틀인 class로 차한대 만들었음.