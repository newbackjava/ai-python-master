print('1. 여기가 시작입니다.')

result = 3/0 #에러발생!
#3번째 줄 아래부터는 실행이 되지 않고,
#실행이 멈춰버림.!
print(result)

print('2. 여기가 중간입니다.')
print('3. 여기가 끝입니다.')

# C:\pythonProject\.venv\Scripts\python.exe C:\pythonProject\pythonProject5\exception\try01.py
# 1. 여기가 시작입니다.
# Traceback (most recent call last):
#   File "C:\pythonProject\pythonProject5\exception\try01.py", line 3, in <module>
#     result = 3/0 #에러발생!
#              ~^~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1