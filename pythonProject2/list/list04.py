import datetime

today = datetime.datetime.today()
month = today.month #3
if month == 12 or 1 <= month <= 2: # 1 <= month && month <= 2
    print('겨울')
elif 3 <= month <= 5:
    print('봄')
elif 6 <= month <= 8:
    print('여름')
elif 9 <= month <= 11:
    print('가을')
else:
    print('해당 계절이 없습니다.')