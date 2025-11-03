import threading

def run():
    for x in range(100):
        print(x)

run1 = threading.Thread(target=run)
run2 = threading.Thread(target=run)
run3 = threading.Thread(target=run)

run1.start(); #cpu가 동시에 처리할 대상으로 등록
run2.start();
run3.start();





