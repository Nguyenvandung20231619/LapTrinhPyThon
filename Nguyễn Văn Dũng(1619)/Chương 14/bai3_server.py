import socket
import re

def check_password(password):
    if not (6 <= len(password) <= 12): return False
    if not re.search("[a-z]", password): return False
    if not re.search("[0-9]", password): return False
    if not re.search("[A-Z]", password): return False
    if not re.search("[$#@]", password): return False
    return True

host = '127.0.0.1'
port = 8092

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server Bài 3 đang đợi kết nối tại port {port}...")

while True:
    conn, addr = server_socket.accept()
    print(f"\n Đã kết nối bởi: {addr}")
    
    data = conn.recv(1024).decode()
    if data:
        print(f" -> Dữ liệu nhận từ Client: {data}")
        
        passwords = data.split(',')
        valid_passwords = []
        
        for pwd in passwords:
            pwd = pwd.strip()
            if check_password(pwd):
                valid_passwords.append(pwd)
        
        response = ",".join(valid_passwords)
        print(f" -> Danh sách hợp lệ lọc được: {response}")
        
        conn.send(response.encode())
        print(f"Đã gửi phản hồi về cho Client.")
    
    conn.close()