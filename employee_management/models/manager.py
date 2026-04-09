from .employee import Employee

class Manager(Employee):
    def calculate_salary(self):
        # Manager: Lương cơ bản + thưởng hiệu suất (1 triệu VND / 1 điểm)
        return self.base_salary + (self.performance_score * 1_000_000)