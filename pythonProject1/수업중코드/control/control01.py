# 제어문
# 순차문: 입력--> 처리--> 출력
# 조건문: if 조건, if~else, if~elif~..else 조건x
# 반복문: while, for

# 숫자입력>> 32
# 숫자입력>> 20
# 연산자 입력(+,-)>> +
# 두 수를 더한 결과는 52입니다.
# (두 수를 뺀 결과는 12입니다.)

# 1. 입력
n1 = int(input("숫자입력>> "));
n2 = int(input("숫자입력>> "));
oper = input("연산자 입력(+,-)>> ")

# n11 = int(n1)
# 2. 처리
# 연산자에 따라서 달라질 수 있음.
result = 0; # 처리 결과를 넣기 위한 변수를 선언!
if oper == '+':
    # pass
    result = n1 + n2;
elif oper == '-':
    # pass
    result = n1 - n2;
else:
    # pass
    result = "연산자 다시 입력하세요."

# 3. 출력
print(result);

# 숫자입력>> 333
# 숫자입력>> 111
# 연산자 입력(+,-)>> +
# 444