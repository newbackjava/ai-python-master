import datetime
print(datetime.datetime.today())
today = datetime.datetime.today()
print(type(today)) # <class 'datetime.datetime'>

print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.hour)
print(today.minute)
print(today.second)

print("------------------")

sn = input("주민번호 입력>> ")
# 040721-4055113
year = sn[:2] #04
gender = sn[7] #4

if gender == '1' or gender == '3':
    print("남자")
else:
    print("여자")


if gender in ('1', '3'):
    print("남자")
else:
    print("여자")

age = today.year - (2000 + int(year))
print("나이는 " + str(age))

