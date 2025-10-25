# data access module
# crud기능
# def 4개 필요!
import pymysql


class DAO:
    # 인스턴스 변수
    conn = None #변수 생성 위치가 중요!
        # 클래스 바로 아래에 생긴 변수는 클래스 안 전체에서 사용 가능
        # 전역변수(글로벌 변수)
    cur = None


    def __init__(self):
        # 함수내에서 처음으로 만들어진 변수(지역변수, 로컬변수)는
        # 함수밖에서는 인식 불가
        # 변수가 위치가 중요!
        # 파이썬에서 변수는 언제 만들어지나??
        # 변수명 = 초기값
        try:
            self.conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='1234',
                db='big',
                charset='utf8'
            )

            print('연결 성공!!', self.conn.host_info)

            # 연결된 통로(stream)을 통해, SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
            self.cur = self.conn.cursor()
        except Exception as e:
            print('db연결 중 에러발생!!')
            print('에러정보>> ', e)

    def create(self,vo):
            # 3. sql문을 보내보자.
            sql = "insert into book values (%s, %s, %s, %s)"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>', result)

            self.conn.commit()  # insert한 것 반영해줘!
            self.conn.close()
            return result


    def read(self, id):

            # 3. sql문을 보내보자.
            sql = "select * from book where id = %s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, (id))
            print('sql문 전송 결과>', result)

            # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다.
            row = self.cur.fetchone()  # row하나만 꺼내!ss
            print(row)
            self.conn.close()
            return row  # 검색결과를 return!



    def all(self):
            # 3. sql문을 보내보자.
            sql = "select * from book"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql)
            print('sql문 전송 결과>', result)

            # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다.
            # row = cur.fetchone() #row하나만 꺼내!
            row = self.cur.fetchall()  # 모두 꺼내!
            # row = cur.fetchmany(5) #row 개수를 정해서 꺼내!
            print(row)
            self.conn.close()
            return row  # 검색결과를 return!


    def update(self, vo):

            # 3. sql문을 보내보자.
            sql = "update book set name = %s where id = %s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>', result)

            self.conn.commit()  # insert한 것 반영해줘!
            self.conn.close()



    def delete(self, vo):
            # 3. sql문을 보내보자.
            sql = "delete from book where id = %s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>', result)

            self.conn.commit()  # insert한 것 반영해줘!
            self.conn.close()

