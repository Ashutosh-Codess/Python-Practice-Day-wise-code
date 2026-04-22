#DAY1: ASSIGNED PRACTICE PROBLEMS
#program 1
#1.1 Adding two numbers
def add_num():
    return 150 + 100
print(add_num())
#1.2 Add two numbers measuring time
import time
def add_num_time(num1: int, num2: int) -> int:
    start_time = time.perf_counter()
    result = num1 + num2
    end_time = time.perf_counter()
    print(f"Result of adding {num1} and {num2} is: {result}")
    print(f"Time taken to add: {end_time - start_time} seconds")
    return result
add_num_time(150, 100)

#2 Descriptive Variable Name 
def multiply_numbers(num1: int, num2: int) -> int:
    return num1 * num2

a: int = int(input(""))
b: int = int(input(""))
print(result = multiply_numbers(a, b))

#3 Define Function
from math import pi

def calculate_area(radius: int) -> float:
    area = pi * (radius ** 2)
    return area
radius: int = int(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {radius} is: {calculate_area(radius)}")

#4 Proper Function Usage Practice
#4.1 Proper Function Usage
def greet_user(name: str) -> str:
    return f"Hello, {name}! Welcome to the programming world."  #greets user after taking name input
user_name: str = input("Please enter your name: ")  #Ask user's name and store it in a variable
print(greet_user(user_name))  # Function called to greet the user and print the message

#4.2 Function Parameter Type Annotation
def calculate_square(number: int) -> int:
    return number ** 2
num: int = int(input(""))
print(f"The square of {num} is: {calculate_square(num)}")

#6.1 Exception Handling
def divide_numbers(num1: int, num2: int) -> float:
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
#6.2 Exception Handling with User Input
def get_user_input_and_divide():
    try:
        num1: int = int(input("Enter the first number: "))
        num2: int = int(input("Enter the second number: "))
        result = divide_numbers(num1, num2)
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid integers.")


#SELF PRACTICE PROGRAMS
#PROG 1: Hello User Name Practice

def greet_user() -> str:
    try:
        name: str = input("Please enter your name: ")
        return f"Hello, {name}! Welcome to the programming world."
    except Exception as e:
        return f"An error occurred: {e}"
    finally: 
        print("Thank you for using the greeting program.")
        print ("End of Program")