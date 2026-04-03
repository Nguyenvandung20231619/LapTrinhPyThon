# Tạo file mẫu theo yêu cầu
content = "Thuc \nn hanh \nvoi \nfile\n IO\n"
with open('demo_file1.txt', 'w', encoding='utf-8') as f:
    f.write(content)

# a) In ra trên một dòng
with open('demo_file1.txt', 'r', encoding='utf-8') as f:
    # Đọc toàn bộ, thay thế các dấu xuống dòng bằng khoảng trắng
    print("In trên một dòng:", f.read().replace('\n', ' '))

# b) In ra theo từng dòng
with open('demo_file1.txt', 'r', encoding='utf-8') as f:
    print("In theo từng dòng:")
    for line in f:
        print(line.strip())