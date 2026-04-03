def quan_ly_thong_tin():
    # Nhập dữ liệu
    ten = input("Nhập tên: ")
    tuoi = input("Nhập tuổi: ")
    email = input("Nhập email: ")
    skype = input("Nhập skype: ")
    dia_chi = input("Nhập địa chỉ: ")
    noi_lam_viec = input("Nhập nơi làm việc: ")

    # a) Lưu vào file setInfo.txt
    with open('setInfo.txt', 'w', encoding='utf-8') as f:
        f.write(f"Tên: {ten}\nTuổi: {tuoi}\nEmail: {email}\nSkype: {skype}\nĐịa chỉ: {dia_chi}\nNơi làm việc: {noi_lam_viec}")
    print("\n--- Đã lưu thông tin thành công ---")

    # b) Đọc và hiển thị
    with open('setInfo.txt', 'r', encoding='utf-8') as f:
        print("Kết quả đọc từ file:")
        print(f.read())

quan_ly_thong_tin()