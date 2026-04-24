import socket

host = '127.0.0.1'
port = 8090

# Kết nối đến server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Gửi thông điệp
message = "From CLIENT TCP"
client_socket.send(message.encode())

# Nhận phản hồi
data = client_socket.recv(1024).decode()
print(f"Nhận từ server: {data}")

client_socket.close()