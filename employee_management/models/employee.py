class Employee:
    def __init__(self, emp_id, name, age, email, base_salary):
        self.id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.performance_score = 0.0
        self.projects = []

    def calculate_salary(self):
        """Method overriden bởi các class con"""
        return self.base_salary