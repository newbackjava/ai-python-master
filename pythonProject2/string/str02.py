# 주민번호 13자리 입력을 받아서
# 나이와 성별을 판별해보세요.
# 현재 날짜
import datetime

today = datetime.datetime.today()

print(today.year, today.month, today.day)
print(today.hour, today.minute, today.second)

sn = input('주민번호 13자리 입력>> ')
year = sn[:2]  # 0~1
gender = sn[6]  # 7

if gender == '1' or gender == '3':
    print('남자!')
else:
    print('여자!')

if gender in ('1', '3'):
    print('남자!')
else:
    print('여자!')

print('--------------')
print(year)

year2 = int(year) + 1900 #int(), float(), str(), '90'--> 90
print(year2)

age = today.year - year2 + 1
print('age>> ', age)
