from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, email, base_salary, programming_language):
        super().__init__(emp_id, name, age, email, base_salary)
        self.programming_language = programming_language

    def calculate_salary(self):
        # Developer: Lương cơ bản + Phụ cấp kỹ thuật cố định 3 triệu VND
        return self.base_salary + 3_000_000