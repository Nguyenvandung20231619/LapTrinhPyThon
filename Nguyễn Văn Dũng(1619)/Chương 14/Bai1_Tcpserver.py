import socket

# Thiết lập thông tin server
host = '127.0.0.1'
port = 8090

# Tạo socket và lắng nghe kết nối
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server đang đợi kết nối tại port {port}...")

conn, addr = server_socket.accept()
print(f"Đã kết nối bởi: {addr}")

# Nhận thông điệp từ client
data = conn.recv(1024).decode()
print(f"Nhận từ client: {data}")

# Trả lời lại cho client
message = "From SERVER TCP"
conn.send(message.encode())

conn.close()
server_socket.close()