# 1. mysql연결할 라이브러리 지정
import pymysql
#pip install pymysql
#npm install jsmysql
#apt install pymysql

def create(day, title, content, etc):
    # 2. db연결(url-ip+port, id/pw, db명)
    con = pymysql.connect(host='localhost', port=3307, user='root', passwd='1234', db='phone');
    print(con)

    # 2-1. sql문을 보내고, 받아와서 가공할 수 cursor부품을 만듦.
    cursor = con.cursor();

    # 3. sql문을 만들고 sql문을 전송한 후 결과를 받아야함.
    sql = f"insert into diary values ('{day}','{title}','{content}','{etc}')"
    result = cursor.execute(sql);
    print(result);

    # 4. sql문의 결과를 받아왔으면 그 결과를 처리

    # 5. 반영할지 말지 결정, 스트림 close!
    con.commit();
    con.close();

def delete():
    pass

def read():
    pass

def update():
    pass

