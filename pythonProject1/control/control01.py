# 제어문
# 순차문: 입력--> 처리--> 출력
# 조건문: if 조건, if~else, if~elif~..else 조건x
# 반복문: while, for
# 정리문제
# ----------
# 숫자입력>> 32
# 숫자입력>> 20
# 연산자 입력(+,-)>> +
# 두 수를 더한 결과는 52입니다.
# (두 수를 뺀 결과는 12입니다.)
n1 = int(input('숫자입력>> '))
n2 = int(input('숫자입력>> '))
oper = input('연산자 입력(+,-)>> ') #+, -
if oper == '+':
    # pass
    print(n1 + n2)
elif oper == '-':
    print(n1 - n2)
else:
    print('연산자를 다시 입력해주세요.!')
