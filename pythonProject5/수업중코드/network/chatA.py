import socket

# 연결통로를 만들고
# 데이터를 계속 받을 수도 있고
# 데이터를 계속 줄수도 있는 부품

# http는 무조건 요청해야 응답해줌.
# http는 한번 요청에 한번 응답함.

# 스트림은 보통 한방향 --> 소켓을 쓰기전용/읽기전용 따로 만들어야함.
# 1. 받을 수 있는 스트림 따로
# 2. 줄 수 있는 스트림 따로

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(('127.0.0.1', 4000))
print("4000포트 A 시작함. =========")

while True:
    # 값입력해서 소켓으로 보내는 코드
    data = input("간단 채팅A>> ")
    sock1.sendto(data.encode('utf-8'), ('127.0.0.1', 3000))

    # 소켓으로 도착했을 때 자동호출되는 함수 코드
    data, addr = sock2.recvfrom(1024); # return data, addr
    print('간단 채팅B>> ', data.decode('utf-8'))


