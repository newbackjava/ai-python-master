today = '오늘은 목요일입니다. 코로나검사해야합니다.코로나'
print(today.find('독감')) #-1: 없음
print(today.find('코로나')) #14: 시작 인덱스
print(today.count('니다'))

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

print(today[-2]) #다

today2 = ','.join(today)
print(today2)

food = ['감자', '고구마', '양파']
food2 = ':'.join(food)
print(food2)

print(type(food2))
print(len(food2))

id = 'root'
id2 = 'Root'
#모두를 대문자, 소문자로 바꾸어서 처리
print(id.upper() == 'ROOT')
id3 = 'root '
print(len(id3.lstrip()))
print(len(id3.rstrip()))
print(len(id3.strip()))
#lower()

print(news.find("주꾸미",3))

## 함수를 쓸 때는
# 파괴함수(원본을 수정해버림)
# 비파괴함수(원본을 그대로 유지) : find, type, count

news2 = news.replace('주꾸미', '문어')
print(news2.find('주꾸미'))
print(news2.find('문어'))



news3 = news.split()
print(news3)
print(type(news3))

#<class 'list'>

# 누적용 변수
count = 0
ju_result = []

for i in range(0, len(news3)):
    # len(10)이면 0~9
    # pass
    # if news3[i] == '주꾸미':
    # if news3[i].startswith('먹방'):
    # if news3[i].endswith("니다'"):
    # if news3[i] in ['인턴', '기자', '채널']:
    if news3[i] not in ['인턴', '기자', '채널']:
        print(i) #위치값
        count += 1
        ju_result.append(news3[i])

print(count)
print(ju_result)

# in연산자 써서 풀어보세요.!
# 인턴 기자 채널만 리스트에 모아서 카운트/프린트
# 인턴 기자 채널만 빼고 리스트에 모아서 카운트/프린트


