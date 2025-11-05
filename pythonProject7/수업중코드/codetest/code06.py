# 리스트에 값을 넣어보세요.
# 1. 리스트를 만들 때 이미 알고 있는 경우
# numbers = [0, 0, 0]
# 2. 리스트를 만들 때 값을 몰라서 못넣는 경우
numbers = []

datas = input("데이터를 입력하시오. ").split(", ")
# 11.1, 22.2, 33.3, 44.4, 55.5, 33.3, 11.1
print(datas)

for x in datas:
    numbers.append(float(x))

print(numbers)
print(numbers.index(22.2)) # 1
# print(numbers.index(33.3)) # 2
for i in range(len(numbers)):
    if numbers[i] == 33.3:
        print(i)

numbers.sort(reverse=True) #오름차순, 내림차순
# 데이터를 입력하시오. 11.1, 22.2, 33.3, 44.4, 55.5, 33.3, 11.1
# ['11.1', '22.2', '33.3', '44.4', '55.5', '33.3', '11.1']
# [11.1, 22.2, 33.3, 44.4, 55.5, 33.3, 11.1]
# 1
# 2
# 5
print(numbers)
# [55.5, 44.4, 33.3, 33.3, 22.2, 11.1, 11.1]
print(numbers[0])
print(numbers[-1])



