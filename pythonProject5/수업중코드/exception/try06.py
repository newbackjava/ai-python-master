try:
    test_file = open('member2.txt', mode='w');

    for _ in range(3):
        id = input("아이디 입력 >> ")
        age = input("나이 입력 >> ")
        tel = input("전화번호 입력 >> ")

        test_file.write(id + "," + age + "," + tel + "\n");

except FileNotFoundError:
    print("파일이 없었음.")
except IOError:
    # pass
    print('읽고 쓰는데 문제가 생겼음.')
except:
    # pass
    print('파일을 처리하는데 문제가 생겼음.')
finally:
    # 꼭 실행해야할 부분을 코드함.!!

    try:
        test_file.close();
    except:
        "스트림을 닫는데 문제가 생겼음."

    # 블록을 잡고
    # for, if, while, try등으로
    # 코드를 감싸주고 싶으면 ctrl+alt+t

# print("내 프로그램 끝남.")
# print("내 프로그램 끝남.")
# print("내 프로그램 끝남.")
# print("내 프로그램 끝남.")
# print("내 프로그램 끝남.")


