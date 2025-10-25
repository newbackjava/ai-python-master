from dao_class import *

if __name__ == '__main__':
    vo = input('id,name,url,img 입력>> ').split(',')  # 4개의 값을 리스트로 넣어줌
    dao = DAO()#__init__()호출함(객체 생성할때 항상 호출됨.)db연결->cursor객체 생성
# 실제벽돌1 = 벽돌틀()  #새롭게 만든 부품dao 클래스DAO()