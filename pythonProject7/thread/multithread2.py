import threading
import time

class RacingCar:
    #멤버변수
    name = ''
    #초기화함수
    def __init__(self, name):
        #self: 클래스로 생성한 객체!
        #c1 = RacingCar('appleCar')
        #self == c1
        #c1.name = 'appleCar'
        self.name = name
    #멤버함수
    def runCar(self):
        for _ in range(10):
            print(self.name + '~~달립니다.')

c1 = RacingCar('appleCar')
c2 = RacingCar('summerCar')
c3 = RacingCar('springCar')

t1 = threading.Thread(target=c1.runCar)
t2 = threading.Thread(target=c2.runCar)
t3 = threading.Thread(target=c3.runCar)

# c1.runCar()
# c2.runCar()
# c3.runCar()

t1.start()
t2.start()
t3.start()