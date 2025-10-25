from me import Day

if __name__ == '__main__':
    #객체가 생성될 때 이니셜라이저 함수가 자동호출
    #멤버변수가 복사된다!
    day1 = Day('자바공부', 10, '강남')
    print(Day.count, '', Day.time )
    day2 = Day('여행', 15, '강원도')
    print(Day.count, '', Day.time )
    day3 = Day('운동', 11, '피트니스')
    print(Day.count, '', Day.time )

    print(day1)
    print(day2)
    print(day3)
    # print(day1.time + day2.time + day3.time)