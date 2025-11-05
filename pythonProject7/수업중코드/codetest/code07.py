list = [3, 2]
find = 0
try :
    find = list.index(100)
    print(find)
except ValueError:
    print("해당 값이 없음.")
    find = -1
    print(find)
except:
    print("error")