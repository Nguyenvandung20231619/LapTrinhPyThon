import socket

host = '127.0.0.1'
port = 8091

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5) 

print(f"Server đang chạy tại port {port}...")

while True: 
    conn, addr = server_socket.accept()
    try:
        data = conn.recv(1024).decode()
        if data:
            a, b = map(int, data.split(','))
            tong = a + b
            print(f"Kết nối từ: {addr} | Tính: {a} + {b} = {tong}")
            conn.send(str(tong).encode())
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        conn.close()