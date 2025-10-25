import datetime

def get_list(food): #food = 'japan'
    if food == 'korean':
        data = ['냉면', '오미지차', '팥빙수']
    elif food == 'japan':
        data = ['우동', '생면']
    else:
        data = ['라면', '커피']
    return data #반환은 list형!

def get_day():
    return datetime.datetime.today()

def get_day2():
    today = datetime.datetime.today()
    return today.month, today.hour

if __name__ == '__main__':
    #return은 여러 개일 수 있다.
    #하나의 변수에 리턴값을
    #   넣어주면 tuple로 묶어준다.
    result3 = get_day2()
    print(result3)
    print(result3[0])
    print(result3[1])
    print('---------')
    a, b = get_day2()
    print(a)
    print(b)
    print('---------')

    a2, _ = get_day2()
    print(a2)

    #return은 datatime객체
    #멤버변수, 멤버함수
    result2 = get_day()
    print(type(result2))
    print(result2.month)

    #return은 list형
    result = get_list('japan')
    print(result)

