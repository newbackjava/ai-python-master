import threading
#실(실처럼 작게 프로그램을 나누어서 처리)
#동시프로그램

def a1(x, y):
    for i in range(x, y+1):
        print('a1번>> ', i)

def a2(x, y):
    for i in range(x, y+1):
        print('a2번>> ', i)

def a3(x, y):
    for i in range(x, y+1):
        print('a3번>> ', i)

thread1 = threading.Thread(target=a1, args=(1, 100))
thread2 = threading.Thread(target=a2, args=(0, 50))
thread3 = threading.Thread(target=a3, args=(5, 133))

thread1.start() #cpu 스케쥴링에 thread1대기줄에 세워줘!
thread2.start() #cpu 스케쥴링에 thread2대기줄에 세워줘!
thread3.start() #cpu 스케쥴링에 thread3대기줄에 세워줘!