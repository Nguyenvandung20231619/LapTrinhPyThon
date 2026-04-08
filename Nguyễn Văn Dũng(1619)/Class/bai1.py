# a) Tạo class hoc_vien với các thuộc tính cơ bản
class hoc_vien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Phương thức show_info trả về đầy đủ thông tin
    def show_info(self):
        print("----- THÔNG TIN HỌC VIÊN -----")
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)
    # c) Phương thức change_info với tham số mặc định
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop
        print("--- Đã cập nhật thông tin thành công ---")

# d) Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng học viên mới
    hv1 = hoc_vien("Nguyễn Văn A", "01/01/2005", "vanA@gmail.com", "0987654321", "TP HCM", "IT-01")

    print("Thông tin ban đầu:")
    print(hv1.show_info())

    # Gọi phương thức thay đổi thông tin (sử dụng tham số mặc định) 
    hv1.change_info()

    print("\nThông tin sau khi thay đổi:")
    print(hv1.show_info())