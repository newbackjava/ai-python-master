# 외부에서 파일을 만들어서 파일에 저장하는 기능을 쓰고 싶으면
# 반드시 호출될 수 있는 형태로 변경해야함.
# 1) 함수로 만든다.
# 2) 클래스를 만들어 그 안에 함수를 넣는다.

def file_read(day):
    lines = []

    try:
        test_file = open(day + '.txt', mode='r', encoding="utf-8");
        lines = test_file.readlines();
        # ['','','']
        # ['2025-11-02\n', '일요일\n', '내일은 월요일이야!!\n']
        print(type(lines));
        print("읽어온 데이터 확인 " + str(lines));

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

    return lines;

def file_save(day, title, content):

    try:
        test_file = open(day + '.txt', mode='w', encoding="utf-8");
        test_file.write(day + "\n" + title + "\n" + content + "\n");
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
