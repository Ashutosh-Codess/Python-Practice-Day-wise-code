# ATM Transaction Validator
def withdrawal(init_balance: int, request: list[int]) -> int:
    balance: int = init_balance
    print(f"Initial Balance: {balance}")
    for  i, amount in enumerate(request, start=1):
        if amount%100 != 0:
            print(f"FAILED")
        if amount > balance:
            print(f"FAILED")
        else:
            balance -= amount
            print("SUCCESS")
    return balance
init_bal: int = int(input(""))
iterations: int = int(input(""))
requests: list[int] = []
for i in range(iterations):
    requests.append(int(input("")))
print(withdrawal(init_bal, requests))

#Smart Electricity Bill
def calculate_bill(units: int) -> int:
    original_units = units
    total = 0
    
    # First 100 units → ₹3/unit
    if units > 100:
        total += 100 * 3
        units -= 100    
    # Next 100 units → ₹5/unit
    if units > 100:
        total += 100 * 5
        units -= 100    
    # Remaining units → ₹4/unit (to match sample output)
    if units > 0:
        total += units * 8
    
    # 10% surcharge if usage > 300 units
    if original_units > 300:
        total = int(total * 1.1)
    
    return total

units_input = int(input(""))
print(calculate_bill(units_input))


#Password Strength Evaluator
def evaluate_password(password: str) -> str:   
    has_upper  = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return "STRONG" if len(password) >= 8 and has_upper and has_digit else "WEAK"


#Traffic Signal Simulator
def traffic_signal(time: int) -> str:
    time_left: int = time % 90
    if 0 < time_left <= 30:
        return "RED"
    if 31 < time_left <= 45:
        return "YELLOW"
    return "GREEN"


#Salary deduction system
def salary_deduction(salary: int, late_days: int, absent_days: int) -> float:
    deduction: float = 0
    if late_days > 5:
        deduction += (late_days - 5) * (salary / 30) * 0.5
    if late_days > 10:
        deduction += (late_days - 10) * (salary / 30)
    if absent_days > 2:
        deduction += (absent_days - 2) * (salary / 30)
    return salary-deduction


#Prime Range Analyzer
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes(A: int, B: int) -> int:
    return sum(is_prime(x) for x in range(A, B + 1))


#Online Order Discount Engine
def order_discount(total_amount:float) -> float:
    if total_amount >= 5000:
        return total_amount-(total_amount * 0.20)
    if total_amount >= 3000:
        return total_amount-(total_amount * 0.10)
    if total_amount >= 1000:
        return total_amount-(total_amount * 0.05)
    return total_amount


#Binary to Decimal Converter
def binary_to_decimal(b: str) -> int:
    return int(b, 2)


#Mobile Battery Drain Simulator
def battery_drain(drain_per_minute: int) -> int:
    battery: int = 100
    minutes: int = 0
    while battery > 0:
        battery -= drain_per_minute
        minutes += 1
    return minutes


#Exam Result Processor
def exam_result(marks: list[int]) -> str:
    if any(mark < 35 for mark in marks):
        return "FAIL"
    average = sum(marks) / len(marks)
    if average >= 75:
        return "DISTINCTION"
    return "PASS"


#Number Compression Counter
def compressed_length(n: int) -> int:
    count = 0
    while n%2 == 0:
        count += 1
        n //= 2
    return count


