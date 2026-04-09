from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError

def validate_age(age):
    if not isinstance(age, int) or age < 18 or age > 65:
        raise InvalidAgeError("Lỗi: Tuổi không hợp lệ (phải từ 18-65).")
    return age

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Lỗi: Lương không hợp lệ (phải > 0).")
    return salary

def validate_email(email):
    if "@" not in email:
        raise ValueError("Lỗi: Email sai định dạng (thiếu @).")
    return email

def validate_score(score):
    if not (0 <= score <= 10):
        raise ValueError("Lỗi: Điểm hiệu suất phải nằm trong khoảng 0-10.")
    return score