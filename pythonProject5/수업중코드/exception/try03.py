# import builtins

# test_file = open('test0.txt');
# print("=======================")
# test_file.close();

# C:\pythonProject\.venv\Scripts\python.exe C:\pythonProject\pythonProject5\exception\try03.py
# Traceback (most recent call last):
#   File "C:\pythonProject\pythonProject5\exception\try03.py", line 3, in <module>
#     test_file = open('test0.txt');
# FileNotFoundError: [Errno 2] No such file or directory: 'test0.txt'
#
# Process finished with exit code 1

try:
    test_file = open('test.txt', mode='r');
    # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp949'>
    # result = print("test")
    data = test_file.readlines();
    print(data);
    for line in data:
        print(line)
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

print("내 프로그램 끝남.")
print("내 프로그램 끝남.")
print("내 프로그램 끝남.")
print("내 프로그램 끝남.")
print("내 프로그램 끝남.")


