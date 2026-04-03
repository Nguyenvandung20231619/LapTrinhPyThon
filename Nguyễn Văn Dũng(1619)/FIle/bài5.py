def dem_tu_trong_file(file_path):
    # Tạo file mẫu để test
    sample_text = "Dem so luong tu xuat hien abc abc abc 12 12 it it eaut"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(sample_text)

    # Xử lý đếm từ
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            words = content.split()
            
            tu_dien_dem = {}
            for word in words:
                # Xóa dấu phẩy hoặc chấm nếu có để đếm chính xác hơn
                word = word.strip('.,') 
                tu_dien_dem[word] = tu_dien_dem.get(word, 0) + 1
            
            return tu_dien_dem
    except FileNotFoundError:
        return "File không tồn tại"

# Kết quả trả về
ket_qua = dem_tu_trong_file('demo_file2.txt')
print("Kết quả trả về:", ket_qua)