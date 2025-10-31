print('1. 여기가 시작입니다.')

try:
    result = 3/0 #에러발생!
    #3번째 줄 아래부터는 실행이 되지 않고,
    #실행이 멈춰버림.!
    print(result)

except ZeroDivisionError:
    result1 = 3/3;
    print("result1 = ", result1)
except IndexError:
    print("인덱스 예외처리하였음.")

print('2. 여기가 중간입니다.')
print('3. 여기가 끝입니다.')

# C:\pythonProject\.venv\Scripts\python.exe C:\pythonProject\pythonProject5\exception\try02-1.py
# 1. 여기가 시작입니다.
# result1 =  1.0
# 2. 여기가 중간입니다.
# 3. 여기가 끝입니다.
#
# Process finished with exit code 0
