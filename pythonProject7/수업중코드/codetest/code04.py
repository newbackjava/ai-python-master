def solution(array, height):
    answer = 0 # 머쓱이보다 키큰 사람수
    for x in array:
        if x > height:
            answer += 1
    return answer


if __name__ == '__main__':
    result = solution([149, 180, 192, 170], 167)
    print(result)