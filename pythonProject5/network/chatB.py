import socket

# stream을 만들어야 하는데,
# 한쪽으로만 흐른다.
# 보내는 stream, 받는 stream
# socket은 2개를 따로 만든다.
# sock1은 보내는 용도, sock2는 받는 용도
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(('127.0.0.1', 3000))
print('127.0.0.1, 3000 port node start!')
print('------------B----------------')

while True:
    # pass
    #b가 a에게 받는 부분
    data, addr = sock2.recvfrom(1024)
    print('간단 채팅A>> ', data.decode('utf-8'))

    # a가 b에 보내는 부분
    data = input('간단 채팅B>> ')
    sock1.sendto(data.encode('utf-8'), ('127.0.0.1', 4000))