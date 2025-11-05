import pymysql as mysql
from pymysql import IntegrityError


def create(data):
    con = mysql.connect(host="localhost",port=3307,user="root",passwd="1234",db="cloth")

    cursor = con.cursor()
    sql = f"INSERT INTO book VALUES('{data[0]}','{data[1]}','{data[2]}','{data[3]}')"
    try:
        result = cursor.execute(sql)
        print(result)

        con.commit()
    except IntegrityError:
        pass
    finally:
        con.close()

    return result

def select(data):
    con = mysql.connect(host="localhost", port=3307, user="root", passwd="1234", db="cloth")

    cursor = con.cursor()
    sql =f"SELECT id, name, url, img FROM book WHERE id = '{data}'"
    try:
        result = cursor.execute(sql)
        print(result)
        row = cursor.fetchone()
        print(type(row))
        print("검색 결과 :")
        print(row)

    except IntegrityError:
        pass
    finally:
        con.close()
    return row

def select_all():
    con = mysql.connect(host="localhost", port=3307, user="root", passwd="1234", db="cloth")

    cursor = con.cursor()
    sql = "SELECT * FROM book"
    try:
        result = cursor.execute(sql)
        print(result)
        rows = cursor.fetchall()
        print("검색 결과 :")
        print(rows)

    except IntegrityError:
        pass
    finally:
        con.close()
    return rows