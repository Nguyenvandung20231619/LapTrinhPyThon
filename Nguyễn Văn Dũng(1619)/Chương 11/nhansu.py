import sqlite3
import os

def connect_db():
    thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))
    duong_dan_db = os.path.join(thu_muc_hien_tai, 'quanlynhansu')
    
    return sqlite3.connect(duong_dan_db)

def tao_nhan_su():
    print("\n--- THÊM MỚI NHÂN SỰ ---")
    cccd = input("Nhập số CCCD: ")
    ten = input("Nhập họ và tên: ")
    ns = input("Nhập ngày sinh (DD/MM/YYYY): ")
    gt = input("Nhập giới tính: ")
    dc = input("Nhập địa chỉ thường trú: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO nhan_su (cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi) VALUES (?, ?, ?, ?, ?)", 
                       (cccd, ten, ns, gt, dc))
        conn.commit()
        print("=> Thêm mới nhân sự thành công!")
    except sqlite3.IntegrityError:
        print("=> Lỗi: Số CCCD này đã tồn tại!")
    except sqlite3.OperationalError as e:
        print(f"=> Lỗi kết nối: {e}. Hãy kiểm tra xem file database có nằm đúng thư mục không.")
    finally:
        conn.close()

def xem_danh_sach():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM nhan_su")
        rows = cursor.fetchall()
        
        print("\n--- DANH SÁCH NHÂN SỰ ---")
        if not rows:
            print("Danh sách trống.")
        for r in rows:
            print(f"CCCD: {r[0]} | Tên: {r[1]} | NS: {r[2]} | GT: {r[3]} | DC: {r[4]}")
    except Exception as e:
        print(f"=> Lỗi: {e}")
    finally:
        conn.close()

def sua_nhan_su():
    cccd = input("Nhập số CCCD của nhân sự cần sửa: ")
    ten_moi = input("Nhập họ tên mới: ")
    dc_moi = input("Nhập địa chỉ mới: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE nhan_su SET ho_ten = ?, dia_chi = ? WHERE cccd = ?", (ten_moi, dc_moi, cccd))
    if cursor.rowcount > 0:
        conn.commit()
        print("=> Cập nhật thành công!")
    else:
        print("=> Không tìm thấy nhân sự có CCCD này.")
    conn.close()

def xoa_nhan_su():
    cccd = input("Nhập số CCCD cần xóa: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM nhan_su WHERE cccd = ?", (cccd,))
    conn.commit()
    if cursor.rowcount > 0:
        print("=> Đã xóa nhân sự thành công.")
    else:
        print("=> Không tìm thấy CCCD để xóa.")
    conn.close()

def tim_kiem():
    tu_khoa = input("Nhập CCCD, Tên hoặc Địa chỉ cần tìm: ")
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM nhan_su WHERE cccd LIKE ? OR ho_ten LIKE ? OR dia_chi LIKE ?"
    param = f"%{tu_khoa}%"
    cursor.execute(query, (param, param, param))
    results = cursor.fetchall()
    
    print("\n--- KẾT QUẢ TÌM KIẾM ---")
    if not results:
        print("Không tìm thấy kết quả phù hợp.")
    for r in results:
        print(f"CCCD: {r[0]} | Tên: {r[1]} | DC: {r[4]}")
    conn.close()

def menu():
    while True:
        print("\n=== PHẦN MỀM QUẢN LÝ NHÂN SỰ ===")
        print("1. Thêm mới nhân sự")
        print("2. Xem danh sách nhân sự")
        print("3. Sửa thông tin nhân sự")
        print("4. Xóa nhân sự")
        print("5. Tìm kiếm nhân sự")
        print("0. Thoát")
        
        chon = input("Chọn chức năng: ")
        if chon == '1': tao_nhan_su()
        elif chon == '2': xem_danh_sach()
        elif chon == '3': sua_nhan_su()
        elif chon == '4': xoa_nhan_su()
        elif chon == '5': tim_kiem()
        elif chon == '0': break
        else: print("Chọn sai, vui lòng nhập lại!")

if __name__ == "__main__":
    menu()