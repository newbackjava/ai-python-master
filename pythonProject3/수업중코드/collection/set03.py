title = ['영어','수학','국어','컴퓨터']
term1 = [100, 99, 88, 77]
# 2학기 점수는 1학기와 거의 동일하다.
#      국어점수만 66점으로 됨.
term2 = term1.copy()
print(term1)
print(term2)
print("----------")
term2[2] = 66
print(term1)
print(term2)

equal_count = 0
big_count = 0
# 0부터 시작, 1씩 증가
for i in range(len(term1)):
    if term1[i] == term2[i] :
        equal_count += 1
    elif term1[i] > term2[i]:
        big_count += 1
print(equal_count)
print(big_count)

