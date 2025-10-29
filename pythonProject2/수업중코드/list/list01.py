food = []

# print(food[0])
# IndexError: list index out of range

# 넣고
food.append('커피')
food.append('라면')
food.append('짜장면')
print(food)

# 수정
food[0] = '아이스커피'
print(food)

# 삭제
del food[0]
print(food)
food.remove('라면') #파괴함수
food.append('레몬주스')
print(food)
food.pop() #맨끝에 있는 것을 삭제
food.append('사과주스')
food.append('수박주스')
print(food)
food.reverse() #파괴함수
print(food)

# 검색
food.sort() #오름차순 정렬
food.reverse() #내림차순 효과
print(food)

# 장점 : 쉽다.! 간단히 꺼내서 출력/간단 연산
# 단점 : 리스트에 값을 넣을 수 없음. 위치를 찾을 수 없음.
for one in food:
    print(one)

# 단점 : 조금 복잡!
# 장점 : 리스트에 값을 넣을 수 있음. 위치를 찾을 수 있음.
for i in range(0, len(food)):
    print(food[i]);
    
# for문 심화!!
# 3번만 프린트해라.!
for _ in range(0, 3): #변수쓰지 않을 때
    print("프린트")


food2 = [
    ['커피', '물'],
    ['국수', '홍차'],
    ['짬뽕', '아이스홍차', '라면']
]

food2[0][0] = '라떼'
print(food2)

# 1차원 리스트는 for문 한개!!! 필요함.
# 2차원 리스트는 for문 2개!!
# 2차원 리스트는 1차원리스트 모아놓은 것
# 1차원리스트는 개수가 달라도 된다.!!
# 1차원리스트는 개수가 달라도 되기때문에 for문 돌릴때 매번 구해준다.
print(len(food2))
print(len(food2[0]))
for i in range(0, len(food2)): #2차원 리스트에서 len() 행개수
    #밖의 for문은 행을 반복해주는 것
    #안의 for문은 한 행의 열값을 프린트하기 위함.
    for j in range(0, len(food2[i])):
        print(food2[i][j], end=' ');
    print()