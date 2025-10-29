hobby3 = [
    {10: {'아침':'game', '저녁' :'picture'}},
    {20: {'아침':'coffee', '저녁' :'tour'}}
    ]
print(hobby3[0][10]) #[10] dic의 키다.!
# {'아침': 'game', '저녁': 'picture'}
print(hobby3[0][10]['아침']) #game
print(type(hobby3[0])) #<class 'dict'>
print(hobby3[1]) #{20: {'아침': 'coffee', '저녁': 'tour'}}

d1 = hobby3[0] # {10: {'아침':'game', '저녁' :'picture'}}
d2 = d1[10] #  {'아침':'game', '저녁' :'picture'}
d3 = d2['아침'] #game
print(d3)

foods = [
    {"mon" : {"아침" : "커피", "저녁" : "샌드위치"}},
    {"sun" : [{"근무일" : "라떼"}, {"휴일" : "탄산수"}]}
]

print(foods)
# 샌드위치 추출
# 인덱스 --> mon --> 저녁
print(foods[0]["mon"]["저녁"])
# 탄산수 추출
# 인덱스 --> sun --> 인덱스 --> 휴일
print(foods[1]["sun"][1]["휴일"])



food = {'아침': '토스트', '점심': '한정식', '저녁': '스프'}
# 삽입
food['간식'] = '귤'
print(food)

# 검색
print(food['간식'])

# dic가지고 for문을 돌려주면 key만 추출된다.
for k in food:
    print(k, food[k])

# 수정
food['간식'] = "치토스"
print(food)

# 삭제
del food['간식']
print(food)

keyss = food.keys()
print(keyss)
print(type(keyss))
# <class 'dict_keys'>
# 속성(변수) + 메서드(함수)
keys_list = list(keyss)
print(keys_list)

values = food.values()
print(values)
# dict_values(['토스트', '한정식', '스프'])
values_list = list(values)
#타입변환(형변환) : casting(캐스팅)
#모르는 클래스(부품)타입으로 리턴이되면
#아는 타입으로 캐스팅해 사용함.!
#예) dict_values --> list()

# keys_list로 반복문을 이용하여 
# food 딕셔너리의 키와 값을 출력
for k in keys_list:
    print(k, food[k])