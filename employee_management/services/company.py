import random
from exceptions.employee_exceptions import EmployeeNotFoundError, ProjectAllocationError, DuplicateEmployeeError

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        # Kiểm tra trùng lặp ID
        for emp in self.employees:
            if emp.id == employee.id:
                # Tự động sinh ID mới nếu trùng
                new_id = f"{employee.id}_{random.randint(100, 999)}"
                print(f"[!] Trùng mã nhân viên. Đã tự động sinh ID mới: {new_id}")
                employee.id = new_id
                break
        self.employees.append(employee)
        print("-> Thêm nhân viên thành công!")

    def get_all(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu nhân viên trong hệ thống.")
        return self.employees

    def find_by_id(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        raise EmployeeNotFoundError(emp_id)

    def assign_project(self, emp_id, project_name):
        emp = self.find_by_id(emp_id)
        if len(emp.projects) >= 5:
            raise ProjectAllocationError(f"Nhân viên {emp.name} đã tham gia tối đa 5 dự án. Từ chối phân công.")
        emp.projects.append(project_name)
        print(f"-> Đã phân công dự án '{project_name}' cho {emp.name}")

    def remove_project(self, emp_id, project_name):
        emp = self.find_by_id(emp_id)
        if project_name in emp.projects:
            emp.projects.remove(project_name)
            print("-> Đã xóa nhân viên khỏi dự án.")
        else:
            print("-> Nhân viên không tham gia dự án này.")

    def remove_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        self.employees.remove(emp)
        print("-> Đã xóa nhân viên khỏi hệ thống (nghỉ việc).")