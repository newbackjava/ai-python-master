class Shape:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def area(self):
        return self.x * self.y;

# s1 = Shape(1, 1)
# s1에는 x, y가 만들어진 힙영역의 저장된 이름을 가지고 있음.
# self라는 것은 s1을 의미!!

class Rectangle(Shape):

    def __init__(self, x, y, w, h):
        # 부모가 되는 Shape을 먼저 만들어야하므로
        # 부모 객체 초기화를 먼저 호출함.
        super().__init__(x, y);
        self.w = w;
        self.h = h;

    # 부모로 부터 상속받은 함수는 자식이 기능을 재정의할 수 있음
    # 함수이름을 똑같이 쓰면 됨.
    # 오버라이드(override) : 자식이 부모가 정의한 함수를 덮어씀(overwrite)
    # "재정의" 가능
    def area(self):
        return self.w * self.h;

    # 객체인 r을 프린트할 때 어떤 것을 프린트할지 string으로 만들어주는 함수
    # 저장공간이름(위치)이 들어있는 변수를 프린트할 때 자동 호출
    def __str__(self):
        return (str(self.x) + ", " +
                str(self.y) + ", " +
                str(self.w) +", " +
                str(self.h)) ;

r = Rectangle(10, 20, 30, 40);
print(r.area()) #1200
print(r)



