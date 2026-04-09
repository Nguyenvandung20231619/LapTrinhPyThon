 
import sys
from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from services.payroll import PayrollService
from utils.validators import validate_age, validate_salary, validate_email, validate_score
from utils.formatters import format_emp_info
from exceptions.employee_exceptions import *

company = Company()

def input_validated_data(is_dev=False):
    """Hàm hỗ trợ nhập và validate dữ liệu vòng lặp"""
    emp_id = input("Nhập ID: ")
    name = input("Nhập tên: ")
    
    while True:
        try:
            age = validate_age(int(input("Nhập tuổi (18-65): ")))
            break
        except ValueError:
            print("-> Lỗi: Vui lòng nhập số nguyên.")
        except InvalidAgeError as e:
            print(f"-> {e}")

    while True:
        try:
            email = validate_email(input("Nhập email: "))
            break
        except ValueError as e:
            print(f"-> {e}")

    while True:
        try:
            salary = validate_salary(float(input("Nhập lương cơ bản: ")))
            break
        except ValueError:
            print("-> Lỗi: Vui lòng nhập số cho lương.")
        except InvalidSalaryError as e:
            print(f"-> {e}")

    lang = input("Nhập ngôn ngữ lập trình: ") if is_dev else None
    return emp_id, name, age, email, salary, lang

def print_menu():
    print("\n" + "="*60)
    print("HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY MỘT MÌNH TÔI".center(60))
    print("="*60)
    print("1. Thêm nhân viên mới")
    print("   \na. Thêm Manager"  "\nb. Thêm Developer"  "\nc. Thêm Intern")
    print("2. Hiển thị danh sách nhân viên")
    print("   a. Tất cả  b. Theo loại  c. Theo hiệu suất")
    print("3. Tìm kiếm nhân viên")
    print("   a. Theo ID  b. Theo tên  c. Theo ngôn ngữ lập trình")
    print("4. Quản lý lương")
    print("   a. Lương từng cá nhân  b. Tổng lương  c. Top 3 lương cao")
    print("5. Quản lý dự án")
    print("   a. Phân công  b. Xóa dự án  c. Xem dự án của nhân viên")
    print("6. Đánh giá hiệu suất")
    print("   a. Cập nhật điểm  b. Xuất sắc (>8)  c. Cần cải thiện (<5)")
    print("7. Quản lý nhân sự")
    print("   a. Xóa (nghỉ việc)  b. Tăng lương cơ bản  c. Thăng chức")
    print("8. Thống kê báo cáo")
    print("   a. Số lượng theo loại  b. Số dự án TB/nhân viên")
    print("9. Thoát")
    print("="*60)

def main():
    while True:
        print_menu()
        choice = input("Chọn chức năng (1-9 hoặc vd 1a): ").strip().lower()

        try:
            if choice.startswith('1'):
                if choice == '1a':
                    id, name, age, email, sal, _ = input_validated_data()
                    company.add_employee(Manager(id, name, age, email, sal))
                elif choice == '1b':
                    id, name, age, email, sal, lang = input_validated_data(is_dev=True)
                    company.add_employee(Developer(id, name, age, email, sal, lang))
                elif choice == '1c':
                    id, name, age, email, sal, _ = input_validated_data()
                    company.add_employee(Intern(id, name, age, email, sal))
                else:
                    print("Lựa chọn không hợp lệ (chọn 1a, 1b, hoặc 1c).")

            elif choice.startswith('2'):
                try:
                    emps = company.get_all()
                    if choice == '2a':
                        for e in emps: print(format_emp_info(e))
                    elif choice == '2b':
                        t = input("Nhập loại (Manager/Developer/Intern): ")
                        for e in emps:
                            if e.__class__.__name__ == t: print(format_emp_info(e))
                    elif choice == '2c':
                        sorted_e = sorted(emps, key=lambda x: x.performance_score, reverse=True)
                        for e in sorted_e: print(format_emp_info(e))
                except IndexError as e:
                    print(f"-> {e}")

            elif choice.startswith('3'):
                try:
                    company.get_all() # Check empty
                    if choice == '3a':
                        emp = company.find_by_id(input("Nhập ID: "))
                        print(format_emp_info(emp))
                    elif choice == '3b':
                        kw = input("Nhập tên: ").lower()
                        for e in company.employees:
                            if kw in e.name.lower(): print(format_emp_info(e))
                    elif choice == '3c':
                        lang = input("Nhập ngôn ngữ: ").lower()
                        for e in company.employees:
                            if isinstance(e, Developer) and lang in e.programming_language.lower():
                                print(format_emp_info(e))
                except IndexError as e: print(f"-> {e}")
                except EmployeeNotFoundError as e: print(f"-> {e}")

            elif choice.startswith('4'):
                try:
                    company.get_all()
                    if choice == '4a':
                        for e in company.employees:
                            print(f"{e.name} - Lương: {e.calculate_salary():,.0f} VND")
                    elif choice == '4b':
                        print(f"Tổng lương công ty: {PayrollService.calc_total_salary(company):,.0f} VND")
                    elif choice == '4c':
                        top3 = PayrollService.get_top_3_highest_paid(company)
                        for e in top3:
                            print(f"{e.name} - {e.calculate_salary():,.0f} VND")
                except IndexError as e: print(f"-> {e}")

            elif choice.startswith('5'):
                if choice == '5a':
                    try:
                        emp_id = input("Nhập ID nhân viên: ")
                        company.find_by_id(emp_id) # Kích hoạt lỗi nếu không có
                        proj = input("Nhập tên dự án: ")
                        company.assign_project(emp_id, proj)
                    except EmployeeNotFoundError as e: print(f"-> {e}")
                    except ProjectAllocationError as e: print(f"-> {e}")
                elif choice == '5b':
                    try:
                        company.remove_project(input("Nhập ID: "), input("Nhập tên dự án cần xóa: "))
                    except EmployeeNotFoundError as e: print(f"-> {e}")
                elif choice == '5c':
                    try:
                        emp = company.find_by_id(input("Nhập ID: "))
                        print(f"Dự án của {emp.name}: {', '.join(emp.projects) if emp.projects else 'Chưa có'}")
                    except EmployeeNotFoundError as e: print(f"-> {e}")

            elif choice.startswith('6'):
                if choice == '6a':
                    try:
                        emp = company.find_by_id(input("Nhập ID: "))
                        while True:
                            try:
                                score = validate_score(float(input("Nhập điểm mới (0-10): ")))
                                emp.performance_score = score
                                print("-> Cập nhật điểm thành công!")
                                break
                            except ValueError as e:
                                print(f"-> {e}")
                    except EmployeeNotFoundError as e: print(f"-> {e}")
                elif choice in ['6b', '6c']:
                    try:
                        for e in company.get_all():
                            if choice == '6b' and e.performance_score >= 8: print(format_emp_info(e))
                            if choice == '6c' and e.performance_score < 5: print(format_emp_info(e))
                    except IndexError as e: print(f"-> {e}")

            elif choice.startswith('7'):
                if choice == '7a':
                    try:
                        company.remove_employee(input("Nhập ID cần xóa: "))
                    except EmployeeNotFoundError as e: print(f"-> {e}")

            elif choice.startswith('8'):
                try:
                    emps = company.get_all()
                    if choice == '8a':
                        stats = {'Manager': 0, 'Developer': 0, 'Intern': 0}
                        for e in emps: stats[e.__class__.__name__] += 1
                        print(stats)
                    elif choice == '8b':
                        total_proj = sum(len(e.projects) for e in emps)
                        print(f"Trung bình dự án/nhân viên: {total_proj/len(emps):.2f}")
                except IndexError as e: print(f"-> {e}")

            elif choice == '9':
                print("Thoát chương trình. Tạm biệt!")
                sys.exit()

            else:
                raise ValueError("Vui lòng nhập từ 1 đến 9 hoặc cấu trúc menu (VD: 1a).")

        except ValueError as e:
            # Xử lý nhập số cho menu nếu nhập linh tinh
            print(f"-> Lỗi nhập liệu: {e}")

if __name__ == "__main__":
    main()