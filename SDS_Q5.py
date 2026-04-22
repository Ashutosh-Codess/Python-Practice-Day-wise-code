#Salary deduction system
def salary_deduction(salary: int, late_days: int, absent_days: int) -> float:
    deduction: float = 0
    if late_days > 10:
        deduction += 0.1 * salary
    if 5 < late_days <= 10:
        deduction += 0.05 * salary
    if absent_days > 2:
        deduction += 0.2 * salary
    return salary-deduction