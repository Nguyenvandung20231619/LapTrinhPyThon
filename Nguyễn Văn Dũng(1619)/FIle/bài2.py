def ghi_va_hien_thi(file_path, noi_dung):
    # Ghi file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(noi_dung)
    
    # Đọc và hiển thị
    with open(file_path, 'r', encoding='utf-8') as f:
        print("Nội dung trong file là:")
        print(f.read())

ghi_va_hien_thi('bai2.txt', 'Lập trình Python rất thú vị!')