# 유한반복 : for --> 무한반복 (조건X)
# 무한반복 : while --> 유한반복 (시작값,조건식, 증감식)

target = 62;
count = 0;  # 누적용, 시도횟수 ==> 반복문안에 넣지 않음.

while True:
    # count = count + 1;
    count += 1;
    data = int(input("숫자 입력>> "));
    if data == target: #62
        print("정답입니다.")
        print("시도한 횟수는 >> ", count)
        break; # while을 stop(if안에 있다고 해서, if문을 중단X!)
    elif data > target: #63
        print("큼")
        print("다시 입력하세요.")
    elif data < target:
        print("작음")
        print("다시 입력하세요.")

print("프로그램을 종료합니다.!!!");