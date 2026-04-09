from .employee import Employee

class Intern(Employee):
    def calculate_salary(self):
        # Intern: Nhận 80% lương cơ bản
        return self.base_salary * 0.8