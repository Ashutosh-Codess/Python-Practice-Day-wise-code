"""
@Author: Sidharth S K
@Date: 2026-04-17 16:33:00
@Last Modified by: Sidharth S K
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim: To practice the concepts of python learned today.
"""
#1 Greet function
def greet(name):
    """
    Description:
        This function takes a name as input and prints a greeting message.
    Parameter:
        name (str): The name of the person to greet.
    Returns:
        None
    """
    print(f"Hello, {name}! Welcome to Python programming.")

#2 Car Loan fucntion
def calculate_car_loan(principal, annual_rate, years):
    """
    Description:
        This function calculates the monthly payment for a car loan.
    Parameters:
        principal (float): The amount of the loan.
        annual_rate (float): The annual interest rate (in percentage).
        years (int): The number of years for the loan.
        Uses EMI formula: EMI = [P x R x (1+R)^N]/[(1+R)^N-1]
        """
    monthly_rate = annual_rate / 12 / 100
    total_payments = years * 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    return emi

#3 Factorial function
def factorial(n):
    """
    Description:
        This function calculates the factorial of a given number.
    Parameter:
        n (int): The number to calculate the factorial for.
    Returns:
        int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)