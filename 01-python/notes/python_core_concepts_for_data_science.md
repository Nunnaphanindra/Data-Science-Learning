# python core concepts we use in Data Science.

# 1. Data Types & Structures
1. Variables
2. Numbers (Integers & Floats)
3. Strings
4. Booleans & Masking
5. Lists
6. Tuples
7. Sets
8. Dictionaries

# 2. Control Flow & Logic
9. Comparison & Logical Operators
10. if / elif / else
11. for Loops
12. while Loops

# 3. Functions & Advanced Python
13. Functions (`def`)
14. Lambda Functions
15. List & Dictionary Comprehensions
16. Exception Handling (`try` / `except`)

# Python Core Concepts — Detailed Learning Notes

# Data Types & Structures :

1. **Variables :**

**Definition:** A named container used to store data values or objects in system memory.

**Example:** 
1.product stores the product name.
2.price stores the laptop price.
3.quantity stores how many laptops you want.
4.total stores the calculated amount.

Real life: When you add 2 laptops to a shopping cart, the website needs to remember the product, price, and quantity. These values can be stored in variables.

2. **Numbers (Integers & Floats):**

**Definition:** Numeric values divided into whole numbers (int) and decimal values (float).

**Example:**
Bank account balance: ₹25,000

Here, 25,000 is a number used to represent the amount of money in the account.

Other simple examples:

Age: 22
Product price: ₹500
Temperature: 32°C
Exam marks: 85
Quantity of products: 5

3. **Strings:**

**Definition:** Ordered sequences of text characters enclosed in quotes.

**Example:**
A person's name, such as "Rahul", is a string because it is text made up of characters.
Other examples: "Hello", "India", "Laptop", "rahul@gmail.com"

4. **Booleans & Masking:**

**Definition:** Binary truth values (True or False) used for conditional logic and filtering.

**Example:**
When you log in to an app, the system checks whether your password is correct.
Correct → True
Incorrect → False
Masking example: In a student list, you might filter students who scored more than 50 marks. Students meeting the condition are True, and the others are False.

5. **Lists:**

**Definition:** Ordered, mutable (changeable) collections that allow duplicate items.

**Example:**
A shopping cart containing multiple products: Laptop, Mouse, Keyboard, Mouse.
The order is maintained, items can be added or removed, and duplicate items are allowed.

6. **Tuples:**

**Definition:** Ordered, immutable (unchangeable) collections and allows duplicates.

**Example:**
A student's exam marks for three subjects could be:

(85, 90, 85)

Here, 85 appears twice, and that's perfectly valid in a tuple.

7. **Sets:**

**Definition:** Unordered collections of unique items (automatically eliminates duplicate values).

**Example:**
A list of unique customer IDs. If the same customer ID appears multiple times, a set keeps it only once.
Example: 101, 102, 101, 103 → 101, 102, 103

8. **Dictionaries:**

**Definition:** Key-value pairs designed for direct lookups and mappings.

**Example:**
A student record where you store information using labels.
Example: Name → Rahul, Age → 22, Marks → 85

Here, Name, Age, and Marks are keys, and Rahul, 22, and 85 are their values.

Dictionary = Key → Value.

# Control Flow & Logic

9. **Comparison & Logical Operators:**

**Definition:** Operators used to compare values and combine multiple conditions to make decisions. Conditional operators (==, >, <, and, or, not) used to evaluate checks.

**Example:**
Operators used to compare values and combine multiple conditions to make decisions.

Example: Checking whether a student's marks are greater than 50 and whether they attended the required classes.

10. **if / elif / else:**

**Definition:** Statements used to make decisions by checking conditions and executing the appropriate block of code.

if — Definition: Checks the first condition. If it is True, its code is executed.
elif — Definition: Checks an additional condition if the previous if condition was False.
else — Definition: Executes when all previous conditions are False.

**Example:**
A shopping website checks your order amount:
If amount is above ₹5,000 → give a 20% discount.
Else if amount is above ₹2,000 → give a 10% discount.
Else → no discount.

if = first condition
elif = another condition
else = when none of the conditions are true.

11. **for Loops:**

**Definition:** A for loop is used to repeat an action for each item in a sequence or collection.

**Example:**
A teacher wants to check the marks of every student in a class. Instead of checking each student separately, a for loop can go through the students one by one.

for loop = Repeat an action for each item.

12. **while Loops:**

**Definition:** A while loop repeats a block of code as long as a given condition remains True.

**Example:**
An ATM allows you to enter your PIN repeatedly while the PIN is incorrect, until you enter the correct PIN or reach the maximum number of attempts.

while loop = Keep repeating while a condition is True.

# Difference between for and while loop:

for loop:
1.Used when you know what items or how many times to iterate.
2.Example: Check marks of 10 students
3.Usually works with a sequence/range.

while loop:
1.Used when you repeat until a condition changes.
2.Example: Keep asking for a PIN until it is correct.
3.Works based on a condition.

**Note:**
for = Go through each item
while = Keep going while this is true.

#  Functions & Advanced Python

13. **Functions (def):**

**Definition:** A function is a reusable block of code designed to perform a specific task. It can take inputs and return an output.

**Example:**
A calculator can have a function for calculating the total price. You give it the price and quantity, and it gives you the total.

Function = Write once, use many times.

14. **Lambda Functions:**

*Definition:* A lambda function is a small, anonymous function used to perform a simple task in a single line.

**Example:**
In a shopping app, you want to quickly calculate the discounted price of a product.

Lambda = Small function for a simple task.

15. **List & Dictionary Comprehensions:**

**Definition:** A short and simple way to create new lists or dictionaries by processing items from an existing collection.

**Example:**
From a list of students' marks, you want to create a new list containing only students who scored above 50.

Comprehension = Create a new list/dictionary in a compact way.

16. **Exception Handling (try / except):**

**Definition:** A way to handle errors that occur while a program is running without stopping the entire program.

**Example:**
When you enter an incorrect password while logging into an application, instead of the app crashing, it shows "Incorrect password. Please try again."

Exception handling = Handle errors safely and keep the program running.

# try and except:
try → Contains the code that might cause an error.
except → Contains what to do if an error happens.

**Example:**
Try: Read the age entered by the user.
Except: If the user enters "hello" instead of a number, show "Please enter a valid age."

**Note:**
try = Try this code
except = If an error happens, handle it here

