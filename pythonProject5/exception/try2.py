print('1. 여기가 시작입니다.')

try:
    result = 3/0 #에러발생!
    #3번째 줄 아래부터는 실행이 되지 않고,
    #실행이 멈춰버림.!
    print(result)
# 에러의 종류에 따라 다르게 처리할 수 있음.
except ZeroDivisionError:
    result = 3/3
    print(result)
except IndexError:
    print('예외처리하였음.')
print('2. 여기가 중간입니다.')
print('3. 여기가 끝입니다.')
