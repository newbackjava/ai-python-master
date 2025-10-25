from db.dao_class import *

if __name__ == '__main__':
    dao = DAO() #__init__ ()호출함. db연결->cursor객체 생성
    vo = input('id,name,url,img>> ').split(',')
    print(vo)
    dao.create(vo) #sql만들어 전송, 결과받아오면 됨.
