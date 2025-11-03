import threading

def run(args):
    for x in range(100):
        print(args, ": ", x)

run1 = threading.Thread(target=run, args=("★",))
run2 = threading.Thread(target=run, args=("☆",))
run3 = threading.Thread(target=run, args=("☎",))

run1.start(); #cpu가 동시에 처리할 대상으로 등록
run2.start();
run3.start();





