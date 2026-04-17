import sqlite3
import os

def connect_db():
    thu_muc = os.path.dirname(os.path.abspath(__file__))
    duong_dan = os.path.join(thu_muc, 'quanlybanhang')
    conn = sqlite3.connect(duong_dan)
    conn.execute("PRAGMA foreign_keys = ON") 
    return conn

def quan_ly_mat_hang():
    while True:
        print("\n--- QUẢN LÝ MẶT HÀNG ---")
        print("1. Hiển thị danh sách")
        print("2. Thêm mặt hàng")
        print("3. Sửa mặt hàng")
        print("4. Xóa mặt hàng")
        print("5. Tìm kiếm (Mã/Tên/Nguồn gốc)")
        print("0. Quay lại")
        
        chon = input("Chọn: ")
        conn = connect_db()
        
        if chon == '1':
            rows = conn.execute("SELECT * FROM mat_hang").fetchall()
            for r in rows: print(f"Mã: {r[0]} | Tên: {r[1]} | Nguồn: {r[2]} | Giá: {r[3]:,.0f}")
        
        elif chon == '2':
            data = (input("Mã MH: "), input("Tên: "), input("Nguồn gốc: "), float(input("Giá: ")))
            conn.execute("INSERT INTO mat_hang VALUES (?,?,?,?)", data)
            conn.commit()
            print("=> Đã thêm.")
            
        elif chon == '3':
            ma = input("Nhập mã cần sửa: ")
            gia_moi = float(input("Giá mới: "))
            conn.execute("UPDATE mat_hang SET don_gia = ? WHERE ma_mh = ?", (gia_moi, ma))
            conn.commit()
            print("=> Đã cập nhật.")

        elif chon == '4':
            ma = input("Nhập mã cần xóa: ")
            conn.execute("DELETE FROM mat_hang WHERE ma_mh = ?", (ma,))
            conn.commit()
            print("=> Đã xóa.")

        elif chon == '5':
            tk = f"%{input('Nhập từ khóa tìm kiếm: ')}%"
            rows = conn.execute("SELECT * FROM mat_hang WHERE ma_mh LIKE ? OR ten_mh LIKE ? OR nguon_gooc LIKE ?", (tk, tk, tk)).fetchall()
            for r in rows: print(r)

        elif chon == '0': break
        conn.close()

def quan_ly_khach_hang():
    while True:
        print("\n--- QUẢN LÝ KHÁCH HÀNG ---")
        print("1. Hiển thị danh sách")
        print("2. Thêm khách hàng")
        print("3. Tìm kiếm (Mã/Tên/SĐT)")
        print("0. Quay lại")
        
        chon = input("Chọn: ")
        conn = connect_db()

        if chon == '1':
            rows = conn.execute("SELECT * FROM khach_hang").fetchall()
            for r in rows: print(f"Mã: {r[0]} | Tên: {r[1]} | SĐT: {r[3]}")
        
        elif chon == '2':
            data = (input("Mã KH: "), input("Họ tên: "), input("Địa chỉ: "), input("SĐT: "))
            conn.execute("INSERT INTO khach_hang VALUES (?,?,?,?)", data)
            conn.commit()
            print("=> Đã thêm.")

        elif chon == '3':
            tk = f"%{input('Nhập từ khóa tìm kiếm: ')}%"
            rows = conn.execute("SELECT * FROM khach_hang WHERE ma_kh LIKE ? OR ho_ten LIKE ? OR sdt LIKE ?", (tk, tk, tk)).fetchall()
            for r in rows: print(r)

        elif chon == '0': break
        conn.close()

def quan_ly_don_hang():
    while True:
        print("\n--- QUẢN LÝ ĐƠN HÀNG ---")
        print("1. Hiển thị danh sách hóa đơn (có tổng tiền)")
        print("2. Thêm đơn hàng mới")
        print("3. Xem chi tiết 1 hóa đơn (hiển thị mặt hàng)")
        print("4. Tìm kiếm đơn hàng (Mã ĐH/Mã KH)")
        print("0. Quay lại")
        
        chon = input("Chọn: ")
        conn = connect_db()

        if chon == '1':
            query = """
            SELECT dh.ma_dh, kh.ho_ten, SUM(ct.so_luong * mh.don_gia)
            FROM don_hang dh
            JOIN khach_hang kh ON dh.ma_kh = kh.ma_kh
            LEFT JOIN chi_tiet_don_hang ct ON dh.ma_dh = ct.ma_dh
            LEFT JOIN mat_hang mh ON ct.ma_mh = mh.ma_mh
            GROUP BY dh.ma_dh
            """
            rows = conn.execute(query).fetchall()
            print("\nDANH SÁCH ĐƠN HÀNG:")
            for r in rows:
                tong = r[2] if r[2] else 0
                print(f"Mã ĐH: {r[0]} | Khách: {r[1]} | Tổng tiền: {tong:,.0f} VNĐ")

        elif chon == '2':
            ma_dh = input("Nhập mã đơn hàng mới: ")
            ma_kh = input("Nhập mã khách hàng: ")
            ngay = input("Ngày đặt (DD/MM/YYYY): ")
            try:
                conn.execute("INSERT INTO don_hang VALUES (?, ?, ?)", (ma_dh, ma_kh, ngay))
                while True:
                    ma_mh = input("Nhập mã mặt hàng (hoặc 'x' để dừng): ")
                    if ma_mh.lower() == 'x': break
                    sl = int(input("Số lượng: "))
                    conn.execute("INSERT INTO chi_tiet_don_hang VALUES (?, ?, ?)", (ma_dh, ma_mh, sl))
                conn.commit()
                print("=> Tạo đơn hàng thành công!")
            except Exception as e:
                print(f"=> Lỗi: {e}")

        elif chon == '3':
            ma_dh = input("Nhập mã hóa đơn cần xem: ")
            query = """
            SELECT mh.ten_mh, ct.so_luong, mh.don_gia, (ct.so_luong * mh.don_gia)
            FROM chi_tiet_don_hang ct
            JOIN mat_hang mh ON ct.ma_mh = mh.ma_mh
            WHERE ct.ma_dh = ?
            """
            rows = conn.execute(query, (ma_dh,)).fetchall()
            print(f"\nCHI TIẾT ĐƠN HÀNG {ma_dh}:")
            tong_bill = 0
            for r in rows:
                print(f"- {r[0]}: {r[1]} x {r[2]:,.0f} = {r[3]:,.0f} VNĐ")
                tong_bill += r[3]
            print(f"==> TỔNG CỘNG: {tong_bill:,.0f} VNĐ")

        elif chon == '4':
            tk = f"%{input('Nhập mã ĐH hoặc mã KH: ')}%"
            rows = conn.execute("SELECT * FROM don_hang WHERE ma_dh LIKE ? OR ma_kh LIKE ?", (tk, tk)).fetchall()
            for r in rows: print(r)

        elif chon == '0': break
        conn.close()

def main_menu():
    while True:
        print("\n========== HỆ THỐNG QUẢN LÝ BÁN HÀNG ==========")
        print("1. Quản lý Mặt Hàng")
        print("2. Quản lý Khách Hàng")
        print("3. Quản lý Đơn Hàng")
        print("0. Thoát chương trình")
        
        chon = input("Chọn menu: ")
        if chon == '1': quan_ly_mat_hang()
        elif chon == '2': quan_ly_khach_hang()
        elif chon == '3': quan_ly_don_hang()
        elif chon == '0': 
            print("Cảm ơn bạn đã sử dụng!")
            break

if __name__ == "__main__":
    main_menu()