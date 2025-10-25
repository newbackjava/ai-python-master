from db.dao_class2 import *

if __name__ == '__main__':
    vo = input('id,name,url,img>> ').split(',')
    dao = DAO()  #실제벽돌1 = 벽돌틀()
    dao.create(vo)


