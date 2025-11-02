# echo_client.py
import socket

SERVER_HOST = "127.0.0.1"  # 같은 PC에서 테스트
SERVER_PORT = 6000

def main():
    for x in range(100):
        # 1) 소켓 생성
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        # 2) 서버에 연결
        sock.connect((SERVER_HOST, SERVER_PORT))
        print(f"[CLIENT] Connected to {SERVER_HOST}:{SERVER_PORT}")

        try:
            while True:
                msg = input("보낼 메시지(q: 종료): ").strip()
                if msg.lower() == "q":
                    break

                # 3) 서버로 전송
                sock.sendall(msg.encode("utf-8"))

                # 4) 서버가 돌려보낸 데이터 받기
                data = sock.recv(1024)
                if not data:
                    print("[CLIENT] 서버가 연결을 끊었습니다.")
                    break

                print("[CLIENT] From server:", data.decode("utf-8"))
        finally:
            sock.close()
            print("[CLIENT] Closed.")

if __name__ == "__main__":
    main()
