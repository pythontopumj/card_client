import socket
import json
import time

def test_connection(server_ip, server_port):
        try:
            socket_test=socket.create_connection((server_ip, server_port), timeout=5)
            request = json.dumps({'action': 'register', 'nickname': 'admin'})
            socket_test.send(request.encode('utf-8'))
            response = socket_test.recv(1024).decode('utf-8')
            print(response)
            while True:
                time.sleep(30)
                request = json.dumps({'action': 'register', 'nickname': 'dddmin'})
                socket_test.send(request.encode('utf-8'))
                response = socket_test.recv(1024).decode('utf-8')
                print(response)


        except Exception as e:
            print(f"Failed to connect to {server_ip}:{server_port}. Error: {e}")

# 서버 IP와 포트 번호를 입력하세요
test_connection('pythontopumj.xyz', 9999)