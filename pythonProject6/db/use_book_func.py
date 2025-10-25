# 북마크 테이블에 대한 crud기능 처리를 하고 싶음.
# from db import dao
# from 패키지 import 모듈명
# --> 모듈명.함수(), 모듈명.클래스명()

import sys
from tkinter import messagebox

from db.dao_func import *

# from 패키지명.모듈명 import 함수명, 클래스명, *
# --> 함수()

if __name__ == '__main__':
    choice = input('cud중 선택1)c, 2)u, 3)d, 4)r(one), 5)r(all)>> ')
    # 모든 입력은 string! "1"
    if choice == '1':
        vo = input('id,name,url,img>> ').split(',')
        # id = input('id입력>> ')
        # name = input('name입력>> ')
        # url = input('url입력>> ')
        # img = input('img입력>> ')
        # vo = (id, name, url, img)
        # create(id, name, url, img)
        print(vo)
        create(vo)
    elif choice == '2':
        #pass  # id가 1이면, name은 naver2로 변경
        id = input('id입력>> ')
        name = input('name입력>> ')
        vo = (name, id)
        print(vo)
        update(vo)
    elif choice == '3':
        vo = input('id>> ')
        print(vo)
        delete(vo)
    elif choice == '4':
        id = input('id>> ')
        print('id: ', id)
        row = read(id) #id를 주면서 검색해와라!
        messagebox.showinfo('결과', '검색결과는 ' + row[0] + ', ' +
                                        row[1] + ', ' +
                                        row[2] + ', ' +
                                        row[3]
                            )
    elif choice == '5':
        all = all() #((),(),(),....)
        ## 출력해주세요@@@
        print('id     name     url                  img')
        print('----------------------------------------')
        for one in all:
            print('%s     %s     %s   %s' % one)
    else:
        sys.exit(0)  # 프로그램 종료!
