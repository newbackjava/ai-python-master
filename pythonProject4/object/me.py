class Day:
    #클래스의 인스턴스인 객체가 생성될 때마다
    #메모리에 따로 만들어진다라고 해서 인스턴스 변수
    doing = '' #인스턴스 변수
    time = 0 #인스턴스 변수
    location = '' #인스턴스 변수
    count = 0 #누적용, #클래스 변수
    time = 0 #클래스 변수

    def __init__(self, doing, time, location):
        self.doing = doing
        self.time = time
        self.location = location
        # 이니셜라이저가 호출될 때마다
        # 몇 개의 객체가 생성되었는지 누적!
        # self.count = self.count + 1
        Day.count += 1 #클래스 변수
        Day.time += time


    def study(self):
        print(self.doing + '을 열심히 하다.')

    def __str__(self):
        return self.doing + " " + \
                str(self.time) + " " + \
                self.location




