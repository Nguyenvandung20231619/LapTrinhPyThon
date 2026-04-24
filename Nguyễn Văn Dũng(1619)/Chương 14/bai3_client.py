import socket

host = '127.0.0.1'
port = 8092

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

user_input = input("Nhập danh sách mật khẩu (cách nhau bởi dấu phẩy): ")

# Gửi dữ liệu lên server
client_socket.send(user_input.encode())

# Nhận kết quả lọc từ server
result = client_socket.recv(1024).decode()

print(f"Các mật khẩu hợp lệ là: {result}")

client_socket.close()