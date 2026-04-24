import socket

host = '127.0.0.1'
port = 8091

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Nhập dữ liệu từ bàn phím
a = input("Nhập số nguyên a: ")
b = input("Nhập số nguyên b: ")

# Gửi sang server định dạng "a,b"
client_socket.send(f"{a},{b}".encode())

# Nhận kết quả tổng
result = client_socket.recv(1024).decode()
print(f"Tổng nhận được từ server: {result}")

client_socket.close()