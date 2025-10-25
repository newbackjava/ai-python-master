today = '오늘은 목요일입니다. 코로나검사해야합니다.'
print(today.find('독감')) #-1: 없음
print(today.find('코로나')) #14: 시작 인덱스
print(today.count('코로나'))

news = '''[서울=뉴시스]황지향 인턴 기자 = '돈쭐내러 왔습니다' 먹요원들의 먹방에 MC 이영자도 감탄한다.

3일 오후 10시 30분에 방송되는 채널 IHQ 예능 프로그램 '돈쭐내러 왔습니다' 28회에서는 경기도 안양시 중앙시장에 위치한 한 막창 집에서 미션을 수행하는 먹피아 조직의 모습이 펼쳐진다.

이날 제이쓴은 "1세대 치킨 프렌차이즈가 모두 대구에서 시작됐다. 바로 이 대구에서 재료를 공수하는 음식점이 오늘의 주인공"이라고 포문을 연다.

이어서 등장한 의뢰인은 "아들과 아내가 운영 중인 막창 집을 '돈쭐(돈으로 혼쭐)' 내달라"고 요청한다.

제작진을 다큐멘터리 촬영팀으로 알고 있는 아들은 인터뷰에서 "2019년 말에 오픈했다. 5시간만 일했는데도 하루 200만~250만원의 매출이 나왔는데 코로나19 이후 10배 가까이 떨어졌다. 어머니가 히터를 끄고 일하신다"고 말해 안타까움을 자아낸다.

먹피아 조직은 의뢰인의 희망 금액대로 '120분 동안 100만원 매출'을 목표로 세운다. 먼저 동은, 쏘영, 나름이 투입돼 막창 10개를 먹는가 하면 고추냉이와 불닭 소스 등을 활용한 먹방을 선보인다.

이어서 아미, 먹갱, 만리는 먹방 시작 5분 만에 주꾸미 10인분을 해치워 "'돈쭐'에만 있는 명장면이다"라는 이영자의 감탄을 이끌어 낸다.

이들은 미리 주문한 주꾸미 20인분을 모두 해치운 것은 물론 추가 주문을 하려다 '솔드아웃'에 직면해 놀라움을 자아낸다．
'''

print(len(news))
print(news.find('주꾸미'))
print(news.count('주꾸미'))
print(news.count('의뢰인'))


print(today[-2])

today2 = ','.join(today)
print(today2)

food = ['감자', '고구마', '양파']
food2 = ' '.join(food)
print(food2)
print(type(food2))
print(len(food2))

id = 'root'
id2 = 'Root'
#모두를 대문자, 소문자로 바꾸어서 처리
print(id.upper() == 'ROOT') #lower()

id3 = 'root '
print(len(id3.lstrip()))
print(len(id3.rstrip()))
print(len(id3.strip()))

count = []
i = 0
while i > -1:
    i = news.find('주꾸미', i)
    if i > -1:
        count.append(i)
        i += len('주꾸미')
print('주꾸미 위치>>', count)







news2 = news.replace('주꾸미', '문어')
print(news2)

news2 = news.split()
print(len(news2))
print(type(news2))
print(news2)

for x in news2: #for-each
    print(x)

count = 0
ju_list = []
for i in range(0, len(news2), 1):
    #print(news2[i])
    #if(news2[i] == '주꾸미'):
    #if(news2[i].startswith('주꾸미')):
    if(news2[i].endswith('주꾸미')):
        print('찾음.>> ', i)
        ju_list.append(i)
        count += 1 #count = count + 1
print('최종 주꾸미 개수는 ', count)
print('최종 주꾸미 위치는 ', ju_list)




