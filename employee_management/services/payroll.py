class PayrollService:
    @staticmethod
    def calc_total_salary(company):
        return sum(emp.calculate_salary() for emp in company.employees)

    @staticmethod
    def get_top_3_highest_paid(company):
        if not company.employees:
            raise IndexError("Chưa có dữ liệu để tính toán.")
        sorted_emps = sorted(company.employees, key=lambda x: x.calculate_salary(), reverse=True)
        return sorted_emps[:3]