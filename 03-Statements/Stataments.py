"""\nPython Statements — Complete Self-Study & Revision Notebook\nCopy this file into Jupyter, VS Code, or Spyder. Lines beginning with # %% mark cells.\n"""\n\n# %% [markdown]\n# # Python Statements — Complete Self-Study & Revision Notebook\n#\n# This notebook combines the major statement topics into one organized guide:\n#\n# 1. Python indentation and statement structure  \n# 2. `if`, `elif`, and `else`  \n# 3. `for` loops  \n# 4. `while` loops  \n# 5. Useful operators and built-in functions  \n# 6. List comprehensions  \n# 7. Mixed practice exercises  \n# 8. Assessment with solutions  \n#\n# Run the notebook from top to bottom. Every code cell includes an example and produces an output.\n\n# %% [markdown]\n# ## 1. Python Statements and Indentation\n#\n# Python uses indentation to define blocks of code. The standard convention is **four spaces** per indentation level.\n\n# %%\ntemperature = 75

if temperature > 70:
    weather = "Warm"
else:
    weather = "Cool"

print("Weather:", weather)\n\n# %% [markdown]\n# ### Multiple statements in one block\n\n# %%\nage = 25

if age >= 18:
    print("You are an adult.")
    print("You may register independently.")\n\n# %% [markdown]\n# ## 2. Conditional Statements: `if`, `elif`, and `else`\n#\n# Conditional statements allow a program to make decisions.\n\n# %% [markdown]\n# ### Basic `if` statement\n\n# %%\nscore = 85

if score >= 70:
    print("You passed!")\n\n# %% [markdown]\n# ### `if` and `else`\n\n# %%\nnumber = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")\n\n# %% [markdown]\n# ### `if`, `elif`, and `else`\n\n# %%\nscore = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)\n\n# %% [markdown]\n# ### Combining conditions with `and`, `or`, and `not`\n\n# %%\nage = 30
has_license = True

if age >= 18 and has_license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")\n\n# %%\nday = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")
else:
    print("It is a weekday.")\n\n# %%\nis_raining = False

if not is_raining:
    print("You do not need an umbrella.")\n\n# %% [markdown]\n# ### Nested conditions\n\n# %%\nusername = "vinay"
password = "python123"

if username == "vinay":
    if password == "python123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")\n\n# %% [markdown]\n# ## 3. `for` Loops\n#\n# A `for` loop processes each item in an iterable, such as a list, string, tuple, dictionary, or range.\n\n# %% [markdown]\n# ### Looping through a list\n\n# %%\nfruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)\n\n# %% [markdown]\n# ### Looping through a string\n\n# %%\nfor letter in "Python":
    print(letter)\n\n# %% [markdown]\n# ### Calculating a total\n\n# %%\nnumbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total += number

print("Total:", total)\n\n# %% [markdown]\n# ### Using a condition inside a loop\n\n# %%\nnumbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")\n\n# %% [markdown]\n# ### Looping through tuples with unpacking\n\n# %%\nemployees = [("Aisha", "Developer"), ("John", "Analyst"), ("Maria", "Manager")]

for name, role in employees:
    print(f"{name} works as a {role}.")\n\n# %% [markdown]\n# ### Looping through a dictionary\n\n# %%\nstudent = {"name": "Alex", "score": 92, "status": "Passed"}

for key, value in student.items():
    print(f"{key}: {value}")\n\n# %% [markdown]\n# ### Nested `for` loops\n\n# %%\nfor row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")
    print()\n\n# %% [markdown]\n# ## 4. `while` Loops\n#\n# A `while` loop repeats as long as its condition remains `True`.\n\n# %% [markdown]\n# ### Basic counter\n\n# %%\ncounter = 1

while counter <= 5:
    print("Counter:", counter)
    counter += 1\n\n# %% [markdown]\n# ### Accumulating values\n\n# %%\nnumber = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Sum from 1 to 5:", total)\n\n# %% [markdown]\n# ### `while` with `else`\n\n# %%\nattempt = 1

while attempt <= 3:
    print("Attempt:", attempt)
    attempt += 1
else:
    print("All attempts completed.")\n\n# %% [markdown]\n# ## 5. Loop-Control Statements\n#\n# - `break` ends the loop immediately.\n# - `continue` skips the rest of the current iteration.\n# - `pass` is a placeholder that performs no action.\n\n# %% [markdown]\n# ### `break`\n\n# %%\nnumbers = [2, 4, 6, 7, 8, 10]

for number in numbers:
    if number % 2 != 0:
        print("First odd number found:", number)
        break\n\n# %% [markdown]\n# ### `continue`\n\n# %%\nfor number in range(1, 8):
    if number == 4:
        continue
    print(number)\n\n# %% [markdown]\n# ### `pass`\n\n# %%\nfor value in range(3):
    if value == 1:
        pass
    print("Value:", value)\n\n# %% [markdown]\n# ## 6. Useful Operators and Built-In Functions\n\n# %% [markdown]\n# ### `range()`\n\n# %%\nprint(list(range(0, 11)))
print(list(range(2, 11, 2)))\n\n# %% [markdown]\n# ### `enumerate()`\n\n# %%\nlanguages = ["Python", "C#", "JavaScript"]

for index, language in enumerate(languages, start=1):
    print(index, language)\n\n# %% [markdown]\n# ### `zip()`\n\n# %%\nnames = ["Aisha", "Ben", "Carlos"]
scores = [91, 84, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")\n\n# %% [markdown]\n# ### `in` and `not in`\n\n# %%\ncourses = ["Python", "Machine Learning", "SQL"]

print("Python" in courses)
print("Java" not in courses)\n\n# %% [markdown]\n# ### `min()`, `max()`, and `sum()`\n\n# %%\nvalues = [14, 8, 27, 5, 19]

print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))\n\n# %% [markdown]\n# ### `sorted()`\n\n# %%\nnames = ["Zara", "Alex", "Michael", "Ben"]

print("Alphabetical:", sorted(names))
print("By length:", sorted(names, key=len))\n\n# %% [markdown]\n# ### `random` examples with a fixed seed\n\n# %%\nfrom random import randint, shuffle, seed

seed(42)

numbers = list(range(1, 6))
shuffle(numbers)

print("Shuffled:", numbers)
print("Random integer:", randint(1, 10))\n\n# %% [markdown]\n# ### Getting user input — simulated for repeatable output\n\n# %%\n# In an interactive notebook, use:
# name = input("Enter your name: ")

name = "Vinay"
print("Hello,", name)\n\n# %% [markdown]\n# ## 7. List Comprehensions\n#\n# A list comprehension is a concise way to create a new list.\n\n# %% [markdown]\n# ### Basic list comprehension\n\n# %%\nsquares = [number ** 2 for number in range(1, 6)]
print(squares)\n\n# %% [markdown]\n# ### List comprehension with a condition\n\n# %%\neven_numbers = [number for number in range(1, 11) if number % 2 == 0]
print(even_numbers)\n\n# %% [markdown]\n# ### Transforming strings\n\n# %%\nnames = ["alice", "bob", "charlie"]
capitalized_names = [name.title() for name in names]

print(capitalized_names)\n\n# %% [markdown]\n# ### `if`–`else` inside a comprehension\n\n# %%\nlabels = ["Even" if number % 2 == 0 else "Odd" for number in range(1, 7)]
print(labels)\n\n# %% [markdown]\n# ### Nested list comprehension\n\n# %%\nmatrix = [[1, 2, 3], [4, 5, 6]]
flattened = [number for row in matrix for number in row]

print(flattened)\n\n# %% [markdown]\n# ## 8. Practical Mixed Examples\n\n# %% [markdown]\n# ### Example 1: Find words beginning with a specific letter\n\n# %%\nsentence = "Python statements support simple and structured solutions"

words_starting_with_s = []

for word in sentence.split():
    if word.lower().startswith("s"):
        words_starting_with_s.append(word)

print(words_starting_with_s)\n\n# %% [markdown]\n# ### Example 2: FizzBuzz\n\n# %%\nfor number in range(1, 16):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)\n\n# %% [markdown]\n# ### Example 3: Count vowels\n\n# %%\ntext = "Machine Learning"
vowels = "aeiou"
vowel_count = 0

for character in text.lower():
    if character in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)\n\n# %% [markdown]\n# ### Example 4: Find the largest value without using `max()`\n\n# %%\nnumbers = [18, 42, 7, 99, 23]
largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print("Largest value:", largest)\n\n# %% [markdown]\n# ### Example 5: Simple password validation\n\n# %%\npassword = "Python@123"

has_uppercase = any(character.isupper() for character in password)
has_lowercase = any(character.islower() for character in password)
has_digit = any(character.isdigit() for character in password)
is_long_enough = len(password) >= 8

if has_uppercase and has_lowercase and has_digit and is_long_enough:
    print("Password is valid.")
else:
    print("Password is invalid.")\n\n# %% [markdown]\n# # 9. Assessment Exercises\n#\n# Try solving each exercise before viewing the solution directly below it.\n\n# %% [markdown]\n# ### Exercise 1\n#\n# Print only the words that begin with the letter **s** from:\n#\n# `"Print only the words that start with s in this sentence"`\n\n# %%\nsentence = "Print only the words that start with s in this sentence"

for word in sentence.split():
    if word.lower().startswith("s"):
        print(word)\n\n# %% [markdown]\n# ### Exercise 2\n#\n# Print all even numbers from 0 through 10.\n\n# %%\nfor number in range(0, 11):
    if number % 2 == 0:
        print(number)\n\n# %% [markdown]\n# ### Exercise 3\n#\n# Create a list containing every number from 1 through 50 that is divisible by 3.\n\n# %%\ndivisible_by_three = [number for number in range(1, 51) if number % 3 == 0]
print(divisible_by_three)\n\n# %% [markdown]\n# ### Exercise 4\n#\n# Print `"Even!"` for every word with an even number of letters.\n\n# %%\nsentence = "Print every word in this sentence that has an even number of letters"

for word in sentence.split():
    if len(word) % 2 == 0:
        print(f"{word}: Even!")\n\n# %% [markdown]\n# ### Exercise 5\n#\n# Create a list containing the first letter of every word in a sentence.\n\n# %%\nsentence = "Create a list of the first letters of every word"
first_letters = [word[0] for word in sentence.split()]

print(first_letters)\n\n# %% [markdown]\n# ### Exercise 6\n#\n# Calculate the sum of all integers from 1 through 100.\n\n# %%\ntotal = sum(range(1, 101))
print("Sum:", total)\n\n# %% [markdown]\n# ### Exercise 7\n#\n# Count how many positive, negative, and zero values appear in a list.\n\n# %%\nvalues = [5, -2, 0, 8, -7, 0, 3, -1]

positive_count = 0
negative_count = 0
zero_count = 0

for value in values:
    if value > 0:
        positive_count += 1
    elif value < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)\n\n# %% [markdown]\n# ### Exercise 8\n#\n# Generate a multiplication table for 5.\n\n# %%\nnumber = 5

for multiplier in range(1, 11):
    print(f"{number} × {multiplier} = {number * multiplier}")\n\n# %% [markdown]\n# # 10. Final Revision Challenge\n\n# %% [markdown]\n# Given a list of student scores:\n#\n# - Assign each score a letter grade.\n# - Print the student name, score, and grade.\n# - Calculate the class average.\n# - Print the highest-scoring student.\n\n# %%\nstudent_scores = {
    "Aisha": 91,
    "Ben": 76,
    "Carlos": 88,
    "Diana": 64,
    "Ethan": 95
}

total_score = 0
highest_name = None
highest_score = -1

for name, score in student_scores.items():
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: score={score}, grade={grade}")
    total_score += score

    if score > highest_score:
        highest_score = score
        highest_name = name

class_average = total_score / len(student_scores)

print(f"Class average: {class_average:.2f}")
print(f"Highest-scoring student: {highest_name} ({highest_score})")\n\n# %% [markdown]\n# # Quick Revision Summary\n#\n# - Use `if`, `elif`, and `else` to make decisions.\n# - Use `for` when iterating through an iterable.\n# - Use `while` when repeating based on a condition.\n# - Use `break`, `continue`, and `pass` to control loop behavior.\n# - Use `range`, `enumerate`, and `zip` for common iteration patterns.\n# - Use list comprehensions to build lists concisely.\n# - Prefer clear variable names and consistent four-space indentation.\n