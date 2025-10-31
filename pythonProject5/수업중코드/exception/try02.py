print('1. 여기가 시작입니다.')

try:
    result = 3/0 #에러발생!
    #3번째 줄 아래부터는 실행이 되지 않고,
    #실행이 멈춰버림.!
    print(result)

except:
    # try블럭을 실행하다가
    # 프로그램을 멈출만한 에러가 생기면
    # 실행에서 제외시키고
    # 대응책을 써놓으면 실행되고
    # 프로그램이 멈추지않고,
    # 아래 코드가 계속이 됨.
    # except(제외, 예외)안에는
    # 대응책을 써놓음.
    print("2번이 실행이 안됨")


print('2. 여기가 중간입니다.')
print('3. 여기가 끝입니다.')

# C:\pythonProject\.venv\Scripts\python.exe C:\pythonProject\pythonProject5\exception\try02.py
# 1. 여기가 시작입니다.
# 2번이 실행이 안됨
# 2. 여기가 중간입니다.
# 3. 여기가 끝입니다.
#
# Process finished with exit code 0