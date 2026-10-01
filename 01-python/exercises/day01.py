# Day 1: Python Practice Problems

# 1. Store your name and age
# 2. Calculate your age next year
# 3. Check whether a number is even or odd
# 4. Find the largest of three numbers
# 5. Reverse a string
# 6. Count vowels in a string
# 7. Find the sum of numbers in a list
# 8. Find the largest number in a list
# 9. Count how many times each word occurs
# 10. Print numbers from 1 to 100

# 1. Store your name and age
name = "Phanindra"
age = 23
print(f"Name: {name}, Age: {age}")

# 2. Calculate your age next year
age_next_year = age + 1
print(f"Age next year: {age_next_year}")

# 3. Check whether a number is even or odd
num = 7
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 4. Find the largest of three numbers
a, b, c = 12, 45, 29
largest = max(a, b, c)
print(f"The largest of {a}, {b}, and {c} is: {largest}")

# 5. Reverse a string
text = "Phanindra"
reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")

#without using reverse operation 
#method 1 : using for loop:
text = "Phanindra"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # Prepend each character
print(f"Reversed string: {reversed_text}")

#method 2 : using while loop:
text = "Phanindra"
reversed_text = ""
index = len(text) - 1  # Start at the last character's index

while index >= 0:
    reversed_text += text[index]
    index -= 1  # Move one step backward
print(f"Reversed string: {reversed_text}")

# 6. Count vowels in a string
sample_text = "Hello Phanindra"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in sample_text:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in '{sample_text}': {vowel_count}")

# 7. Find the sum of numbers in a list
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)
print(f"Sum of numbers: {total_sum}")

# 7. Find the sum of numbers in a list
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)
print(f"Sum of numbers: {total_sum}")

#second method without using sum operation:
numbers = [10, 20, 30, 40, 50]
total_sum = 0
for num in numbers:
    total_sum += num  # same as: total_sum = total_sum + num

print(f"Sum of numbers: {total_sum}")

# 8. Find the largest number in a list
scores = [45, 89, 12, 99, 67]
max_number = max(scores)
print(f"Largest number in list: {max_number}")

#second method:
scores = [45, 89, 12, 99, 67]

# Start by assuming the first element is the largest
max_number = scores[0]

for score in scores:
    if score > max_number:
        max_number = score
print(f"Largest number in list: {max_number}")

# 9. Count how many times each word occurs
name = "Phanindra"
letter_counts = {}  # Empty dictionary (our notepad)
for char in name:
    if char in letter_counts:
        letter_counts[char] += 1  
    else:
        letter_counts[char] = 1   
print(f"Letter frequency: {letter_counts}")

# 10. Print numbers from 1 to 100
for i in range(1, 101):
    print(i, end=" ")

#second method:
counter = 1

while counter <= 100:
    print(counter, end=" ")
    counter += 1  




