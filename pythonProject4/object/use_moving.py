import moving as m  # module까지 써주어야 함.

if __name__ == '__main__':
    b1 = m.Bike(100, 2, '강릉')
    # b1.speed = 100
    # b1.person = 2
    # b1.location = '강릉'
    print(b1)

    b1.start()
    result = b1.speed_up()  # 10
    print(result, '만큼 스피트업!')
    result2 = b1.speed_up()  # 10
    print(result2, '만큼 스피트업!')

    print('----------')

    # class의 instance인 object!
    c1 = m.Car('네모', 'red')
    # 객체생성시 자동으로 멤버변수값을 초기화해주는 함수를
    # 하나 만들자!(생성자 메서드, 초기화해주는것 ,
    # initializer(이니셜라이저)
    # c1.shape = '네모'
    # c1.color = 'red'
    c2 = m.Car('세모', 'green')
    # c2.shape = '세모'
    # c2.color = 'green'
    print(c1)
    print(c2)
    c1.speed_up()
    c2.speed_down()
