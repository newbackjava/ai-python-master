try:
    # test_file3 = open('test2.txt', 'w')
    test_file3 = open('test2.txt', 'a')
    # result = test_file3.write('hello hi lunch')
    # print(result)
    test_file3.write('hello hi lunch\n')
    test_file3.write('hello2 hi2 lunch2\n')
except FileNotFoundError:
    print('해당 파일을 찾을 수 없음.')
except IOError:
    print('읽고 쓰는데 문제가 생겼음.')
except:
    print('파일을 처리하는데 문제가 생겼음.')
finally:
    try :
        test_file3.close()
    except:
        print('file을 closing하는데 문제가 생김.')
