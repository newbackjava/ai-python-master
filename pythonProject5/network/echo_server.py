# echo_server.py
import socket

HOST = "0.0.0.0"   # 모든 인터페이스에서 들어오는 걸 받겠다
PORT = 6000        # 사용할 포트 (열려 있어야 함)

def main():
    # 1) 소켓 생성: IPv4 + TCP
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2) 포트 재사용 옵션 (개발할 때 편함)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 3) 주소와 포트에 바인딩
    server_sock.bind((HOST, PORT))

    # 4) 클라이언트 접속 대기 상태로
    server_sock.listen()  # listen(백로그) 기본값이면 5개 정도

    print(f"[SERVER] Listening on {HOST}:{PORT} ...")

    count = 0;
    while True:
        # 5) 클라이언트 접속 수락
        client_sock, client_addr = server_sock.accept()
        print(f"[SERVER] Connected by {client_addr}")
        count += 1;
        print("현재 연결된 클라이언트수 >> " + str(count))
        # 6) 1명의 클라이언트와 통신
        while True:
            data = client_sock.recv(1024)  # 최대 1024바이트 수신
            if not data:
                # 클라이언트가 연결 끊음
                print(f"[SERVER] Client {client_addr} disconnected.")
                break

            msg = data.decode("utf-8")
            print(f"[SERVER] Received: {msg}")

            # 받은 걸 그대로 돌려보내는 echo
            send_msg = f"[echo] {msg}"
            client_sock.sendall(send_msg.encode("utf-8"))

        # 이 클라이언트 소켓 닫기
        client_sock.close()

    # 일반적으로 여기 안 옴 (무한루프)
    server_sock.close()

if __name__ == "__main__":
    main()
