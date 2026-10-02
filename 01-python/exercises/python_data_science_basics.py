# variable:
# code:
model_name = "RandomForest"
learning_rate = 0.01
print(model_name, learning_rate)

# numbers:
# code:
age = 22          # Integer
price = 99.50     # Float
print(age)
print(price)

# strings:
# code:
raw_text = "  Customer Review: Great Product!  "
clean_text = raw_text.strip().lower()
print(clean_text)

# Booleans & Masking:
# code:
price = 15000
is_expensive = price > 10000
print("Is High Value?:", is_expensive)

# lists:
# properties: ordered,mutable,duplicates,different data types,indexed
# code:
features = ["age", "income", "credit_score"]
features.append("loan_amount")
print("First feature:", features[0])

# tuples:
# properties: ordered,immutable,duplicates,allow different data types,indexed
# code:
student_marks = (85, 90, 85)
print("Marks:", student_marks)

# sets:
# prroperties: no duplicates,unordered,mutable,different data types,no indexing
# code:
classes = {"cat", "dog", "cat", "bird"}
print(classes)

# Dictionaries:
# properties:key-value pairs,ordered,mutable,no duplicates in keys(unique),duplicates in values,different data types are allowed.
# code:
student = {
    "name": "Rahul",
    "age": 22,
    "marks": 85
}
print(student["name"])

# Comparison & Logical Operators:
# code:
marks = 75
attendance = 80
eligible = marks >= 50 and attendance >= 75
print("Eligible:", eligible)

# if/elif/else:
# code:
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print("Grade:", grade)

# for loop:
# code:
columns = ["age", "income", "salary"]
for col in columns:
    print("Processing column:", col)

# while loop:
# code:
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# functions:
# code:
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
marks = [80, 75, 90, 85]
result = calculate_average(marks)
print("Average Marks:", result)

# lambda:
# code:
calculate_discount = lambda price, discount: price - (price * discount / 100)
price = 2000
discount = 10
final_price = calculate_discount(price, discount)
print("Final Price:", final_price)

# List & Dictionary Comprehensions:
# code:
marks = {"Rahul": 80, "Priya": 45, "Arun": 70, "Anu": 35}
# List Comprehension
passed_names = [name for name, mark in marks.items() if mark >= 50]
# Dictionary Comprehension
passed_students = {name: mark for name, mark in marks.items() if mark >= 50}
print("Passed Names:", passed_names)
print("Passed Students:", passed_students)

# Exception Handling (try / except):
# code:
marks = "85"
try:
    marks = int(marks)
    average = 500 / marks
    print("Result:", average)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Marks cannot be zero.")

