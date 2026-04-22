#PROG 4: Find Generation
birth_year: int = int(input("Enter your birth year: "))
def find_generation(year: int) -> bool:
    print(f"You were born in the year {year}.",
          f"\nBaby Boomer: {1946 <= year <= 1964}",
          f"\nGeneration X: {1965 <= year <= 1980}",
          f"\nMillennial: {1981 <= year <= 1996}",
          f"\nGeneration Z: {1997 <= year <= 2012}",
          f"\nGeneration Alpha: {year > 2012}"
          )
find_generation(birth_year)

#PROG5: Time Conversion
def convert_seconds(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    print(f"{hours} hours, {minutes} minutes, and {remaining_seconds} seconds")
convert_seconds(3721)

#PROG6: Bill Generator App
APPLE_GST = 0.12 # 12% GST
ORANGE_GST = 0.05 # 5% GST
#  Enter Buyer Name, Price for Apple and Orange per kg, and quantity of Apples and Oranges in kg purchased by the buyer
buyer_name = input("Enter Buyer Name: ")
apple_price_kg = int(input("Enter Apple price per kg: ") )
apple_quantity_kg = float(input("Enter Apple Quantity in kg: "))
orange_price_kg = int(input("Enter Orange price per kg: "))
orange_quantity_kg = float(input("Enter Orange Quantity in kg: ") )
def calculate_bill(buyer: str, apple_price: int, apple_qty: float, orange_price: int, orange_qty: float) -> None:
    apple_cost = apple_price * apple_qty
    orange_cost = orange_price * orange_qty
    total_cost = apple_cost + orange_cost
    gst_amount = (apple_cost * APPLE_GST) + (orange_cost * ORANGE_GST)
    final_amount = total_cost + gst_amount
    print(f"Buyer Name: {buyer}")
    print(f"Total Cost (without GST): {total_cost:.2f}")
    print(f"GST Amount: {gst_amount:.2f}")
    print(f"Final Amount to Pay: {final_amount:.2f}")
calculate_bill(buyer_name, apple_price_kg, apple_quantity_kg, orange_price_kg, orange_quantity_kg)

#PrOG7: School Report Generator
students = 3
subjects = ["Physics", "Chemistry", "Maths"]

names = []
marks = []
totals = []
subject_totals = [0, 0, 0]

# Input
for i in range(students):
    name = input(f"\nEnter name of student {i+1}: ")
    names.append(name)
    
    student_marks = []
    total = 0
    
    for j in range(len(subjects)):
        m = float(input(f"Enter marks for {subjects[j]}: "))
        student_marks.append(m)
        total += m
        subject_totals[j] += m
    
    marks.append(student_marks)
    totals.append(total)

# Student Results
for i in range(students):
    print(f"\n--- Result for {names[i]} ---")
    print(f"Total Marks: {totals[i]}")
    
    for j in range(len(subjects)):
        percentage = (marks[i][j] / 100) * 100
        print(f"{subjects[j]} Percentage: {percentage}%")

# Class Averages
print("\n--- Class Averages ---")
for j in range(len(subjects)):
    avg = subject_totals[j] / students
    print(f"{subjects[j]} Average: {avg}")

# Overall Percentage
grand_total = sum(totals)
overall_percentage = grand_total / (students * len(subjects))

print(f"\nOverall Percentage: {overall_percentage}%")
