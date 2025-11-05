import member_db as db

choice = input("1.입력, 2.검색한개, 3. 검색여러개, 4. 수정, 5. 삭제>> ")
if choice == "1":
    data = input("아이디,패스워드,이름,전화번호 순서대로 입력>> ").split(',');
    print("입력받은 데이터 ", data) #['a','a','a','a']
    db.create(data)
elif choice == "2":
    data = input("검색할 id입력>> ")
    print("입력받은 데이터 ", data)
    db.read_one(data)
elif choice == "3":
    db.read_all()
elif choice == "4":
    data = input("바꿀 전화번호,아이디 순서대로 입력>> ").split(',');
    print("입력받은 데이터 ", data)  # ['888','ice']
    db.update(data)
elif choice == "5":
    data = input("삭제할 id입력>> ")
    print("입력받은 데이터 ", data)
    db.delete(data)
else:
    print("1-5 사이의 값을 입력해주세요.")