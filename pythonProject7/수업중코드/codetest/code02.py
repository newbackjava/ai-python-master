def solution(numbers):
    # print(numbers) # numbers안에는 힙영역에 저장된 저장주소이름
    # n = 10
    # print(n)
    # print(type(numbers))
    answer = sum(numbers) / len(numbers)
    return answer

if __name__ == '__main__':
    result = solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
    print(result)