import math

class PhanSo:
    # 1. Khởi tạo phân số
    def __init__(self, tu_so, mau_so=1):
        if mau_so == 0:
            print("Lỗi: Mẫu số không được bằng 0! Đã tự động gán mẫu = 1.")
            self.tu_so = tu_so
            self.mau_so = 1
        else:
            self.tu_so = tu_so
            self.mau_so = mau_so

    # Hiển thị theo cách bạn yêu cầu
    def hien_thi(self):
        print("Tử số:", self.tu_so)
        print("Mẫu số:", self.mau_so)
        print("Phân số:", f"{self.tu_so}/{self.mau_so}")

    # 2. Tối giản phân số
    def toi_gian(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so = self.tu_so // ucln
        self.mau_so = self.mau_so // ucln
        return self

    # 3. Nhân 2 phân số
    def nhan(self, phan_so_khac):
        tu_moi = self.tu_so * phan_so_khac.tu_so
        mau_moi = self.mau_so * phan_so_khac.mau_so
        return PhanSo(tu_moi, mau_moi).toi_gian()

    # 4. Chia 2 phân số
    def chia(self, phan_so_khac):
        if phan_so_khac.tu_so == 0:
            print("Lỗi: Không thể chia cho phân số có tử bằng 0.")
            return None
        tu_moi = self.tu_so * phan_so_khac.mau_so
        mau_moi = self.mau_so * phan_so_khac.tu_so
        return PhanSo(tu_moi, mau_moi).toi_gian()

    # 5. Tổng 2 phân số
    def cong(self, phan_so_khac):
        tu_moi = self.tu_so * phan_so_khac.mau_so + phan_so_khac.tu_so * self.mau_so
        mau_moi = self.mau_so * phan_so_khac.mau_so
        return PhanSo(tu_moi, mau_moi).toi_gian()

    # 6. Hiệu 2 phân số
    def tru(self, phan_so_khac):
        tu_moi = self.tu_so * phan_so_khac.mau_so - phan_so_khac.tu_so * self.mau_so
        mau_moi = self.mau_so * phan_so_khac.mau_so
        return PhanSo(tu_moi, mau_moi).toi_gian()

# --- CHƯƠNG TRÌNH CHÍNH ---

def nhap_phan_so(ten):
    print(f"\nNhập dữ liệu cho {ten}:")
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    return PhanSo(tu, mau)

# Nhập 2 phân số ban đầu
ps1 = nhap_phan_so("Phân số thứ nhất")
ps2 = nhap_phan_so("Phân số thứ hai")

while True:
    print("\n--- MENU CHỌN PHÉP TÍNH ---")
    print("1. Cộng 2 phân số")
    print("2. Trừ 2 phân số")
    print("3. Nhân 2 phân số")
    print("4. Chia 2 phân số")
    print("5. Tối giản 2 phân số ban đầu và hiển thị")
    print("6. Nhập lại phân số mới")
    print("0. Thoát")
    
    lua_chon = input("Nhập lựa chọn của bạn (0-6): ")

    if lua_chon == '1':
        kq = ps1.cong(ps2)
        print("\nKết quả phép Cộng:")
        kq.hien_thi()
    elif lua_chon == '2':
        kq = ps1.tru(ps2)
        print("\nKết quả phép Trừ:")
        kq.hien_thi()
    elif lua_chon == '3':
        kq = ps1.nhan(ps2)
        print("\nKết quả phép Nhân:")
        kq.hien_thi()
    elif lua_chon == '4':
        kq = ps1.chia(ps2)
        if kq:
            print("\nKết quả phép Chia:")
            kq.hien_thi()
    elif lua_chon == '5':
        print("\nPhân số 1 sau tối giản:")
        ps1.toi_gian().hien_thi()
        print("\nPhân số 2 sau tối giản:")
        ps2.toi_gian().hien_thi()
    elif lua_chon == '6':
        ps1 = nhap_phan_so("Phân số thứ nhất")
        ps2 = nhap_phan_so("Phân số thứ hai")
    elif lua_chon == '0':
        print("Đã thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")