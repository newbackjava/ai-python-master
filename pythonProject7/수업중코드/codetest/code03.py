def solution(numbers):

    # 오름차순으로 정렬후
    # 맨 끝의 값과 그 앞에 있는 값을 곱하면 최대값임!
    numbers.sort()
    # print(numbers)
    last = numbers[len(numbers) - 1]
    last_pre = numbers[len(numbers) - 2]
    answer = last * last_pre
    return answer

if __name__ == '__main__':
    result = solution([0, 31, 24, 10, 1, 9])
    print(result)