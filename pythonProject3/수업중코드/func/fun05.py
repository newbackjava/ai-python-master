# data = input('data >> ')
# print(data.isdigit())
# print(data.isalpha())
# ------------------
# data >> 한
# False
# True

# 함수 연습
# ** find('a'), find('1')이라고 호출시
#    문자인지 숫자인지 리턴하는 함수 정의
#    --> 호출해서 결과 출력

# age = 100;

def find(data):
    result8 = "문자도 숫자도 아님."
    data2 = str(data)
    if data2.isdigit():
        result8 = "숫자";
    elif data2.isalpha():
        result8 = "문자";

    return result8;

print(find('a'))
# print(find('1'))
print(find(1))














