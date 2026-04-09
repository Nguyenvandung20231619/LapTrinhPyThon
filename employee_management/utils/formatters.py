def format_emp_info(emp):
    role = emp.__class__.__name__
    info = f"ID: {emp.id:<8} | Tên: {emp.name:<15} | Role: {role:<10} | Tuổi: {emp.age} | Email: {emp.email:<20} | Điểm: {emp.performance_score}"
    if role == 'Developer':
        info += f" | Ngôn ngữ: {emp.programming_language}"
    return info