#data access module(dao처럼)
#crud기능
#def 4개 필요!
#버튼하나당! 함수하나!
#함수로 모듈화시키는 작업!
import pymysql
class DAO:#클래스 안으로 넣어보자.
    conn = None#전역변수를 지정할때 self를 써주는데 init밖에 None으로 지정해주었기
    cur = None#때문에self.conn,self.cur로 쓰면 다른 함수에서 끌어다가 쓸 수 있다.
    #init안에 있는 함수는 이 안에서만 쓸 수 있으므로 conn이랑cur을 밖으로 빼서 써줘야 전체적으로
    #필요할때마다 self를 붙여서 갖다가 쓸 수 있다.
    def __init__(self):#init으로 넣어버리면 init안에 써준 코드는 반복해서 안써줘도 된다.
        #함수내에서 처음으로 만들어진 변수는(지역변수,로컬변수)
        #함수밖에서는 인식 불가
        #그래서 변수 위치가 중요!
        #파이썬에서는 변수는 언제 만들어지나?
        #변수명 = 초기값
        #conn = None처럼 클래스 바로 아래에 생긴 변수는 클래스 안 전체에서 사용 가능.
        try:
            self.conn = pymysql.connect(
                # 파라메터 #리턴이 있기 때문에 연결통로역할을 하는 conn을 써준다.
                # conn을 프린트하면 주소가 나옴!
                host='localhost',
                port=3306,
                user='root',
                password='1234',
                db='big',
                charset='utf8'
            )
            print('1. 연결성공~!~!', self.conn.host_info)#socket localhost:3366이주소가 프린트.
            # 연결된 통로(stream)을 통해, SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
            cur = self.conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

        except Exception as e:
            print('에러정보는 e')
            print('db연결 중 에러발생')

    def create(self, vo):  # readOne
            # 3. sql문을 보내보자
            sql = "insert into book values (%s, %s, %s, %s)"#자바에서(?,?,?,?)랑 같음.

            # 커서로 sql문을 보냄
            print(vo)
            result = self.cur.execute(sql,vo)#튜플()로 묶은 vo를 넣어주면
            #알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
            print('sql문 전송 결과> ', result)

            self.conn.commit()  # 내가 실행한 insert한 거 반영해줘! 꼭 써야함
            self.conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.


    def read(self, id):#readOne
            print('1. 연결성공~!~!', self.conn.host_info)
            # 연결된 통로(stream)을 통해, SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
            cur = self.conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

            # 3. sql문을 보내보자
            sql = "select * from book where id = %s"

            # 커서로 sql문을 보냄
            result = cur.execute(sql, (id))  # 튜플()로 묶은 vo를 넣어주면
            # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
            print('sql문 전송 결과> ', result)#1개 가져왔다고 결과값 나옴. 우리가 원하는 row내용을 주지 않는다.
            #select는 commit할 필요가 없다. read만 하니까!
            #!!!read 인 경우, 커서에 있는 연결통로(stream)검색 결과를 꺼내야 우리가 불러오는 내용을 받아볼 수 있다.
            row = cur.fetchone()#fetchone꺼낼 때 쓰는 함수.row 하나만 꺼내와라!
            print(row)
            self.conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.
            return row #검색결과를 return!



    def all(self):#readAll

            print('1. 연결성공~!~!', self.conn.host_info)
            # 연결된 통로(stream)을 통해, SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
            cur = self.conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

            # 3. sql문을 보내보자
            sql = "select * from book"

            # 커서로 sql문을 보냄
            result = cur.execute(sql)  # 튜플()로 묶은 vo를 넣어주면
            # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
            print('sql문 전송 결과> ', result)#1개 가져왔다고 결과값 나옴. 우리가 원하는 row내용을 주지 않는다.
            #select는 commit할 필요가 없다. read만 하니까!
            #!!!read 인 경우, 커서에 있는 연결통로(stream)검색 결과를 꺼내야 우리가 불러오는 내용을 받아볼 수 있다.
            #row = cur.fetchone()#fetchone꺼낼 때 쓰는 함수.row 하나만 꺼내와라!
            row = cur.fetchall()#많이꺼내!
            #row = cur.fetchmany(5)#row 개수를 정해서 꺼내
            print(row)
            self.conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.
            return row #검색결과를 return!



    def update(self,vo):

            print('1. 연결성공~!~!', self.conn.host_info)
            # 연결된 통로(stream)을 통해, SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
            cur = self.conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

            # 3. sql문을 보내보자
            sql = "update book set name = %s where id = %s"

            # 커서로 sql문을 보냄
            result = cur.execute(sql, vo)  # 튜플()로 묶은 vo를 넣어주면
            # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
            print('sql문 전송 결과> ', result)

            self.conn.commit()  # 내가 실행한 insert한 거 반영해줘! 꼭 써야함
            self.conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.


    def delete(self, vo):

            print('1. 연결성공~!~!', self.conn.host_info)
            # 연결된 통로(stream)을 통해, SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
            cur = self.conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

            # 3. sql문을 보내보자
            sql = "delete from book where id = %s"

            # 커서로 sql문을 보냄
            result = cur.execute(sql,vo)  # 튜플()로 묶은 vo를 넣어주면
            # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
            print('sql문 전송 결과> ', result)

            self.conn.commit()  # 내가 실행한 insert한 거 반영해줘! 꼭 써야함
            self.conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.
