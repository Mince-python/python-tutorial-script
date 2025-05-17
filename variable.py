# Variables/Identifiers
# A variable is a container for value. Which can be of various types (String Literals, Number Literals; integer and float, Boolean Literals)

#  (=)
# _name and NAME
num1 = 20



# A string is a series of characters. Any enclose text quotes, can be both single as well as double quotes. Uses triple quotes for multi-line strings

name = "Hackustaz"
email = 'infohack@fake.com'
age = 50

# concatenation
# This is a method to concatenate, or combine two strings together. You can use the + operator or the f-strings method.

print('Hello, my name is ' + name + ' and I am ' + str(age) + 'years old')
print(f'Hello, my name is {name}  and I am {str(age)} years old')


# # common string methods
# nickName = 'hackustaz' 
# # capitalize string
# print(nickName.capitalize())
# # # make all uppercase
# print(nickName.upper())
# # # make all lowercase
# print(nickName.lower())

# # # Get length
# print(len(nickName))
# # # Replace
# print(nickName.replace("hackustaz", "Tutor"))

# # # is all numeric
# print(nickName.isnumeric())
# # # is all alphabetic
# print(nickName.isalpha())
# # # is all alphanumeric
# print(nickName.isalnum())
# # find position
# print(nickName.find('c'))
# # split into list
# print(nickName.split())
# print(type(nickName))




# Stripping Whitespace
# Extra whitespace in a string can cause problems in your program. For example, 'python' and 'python ' might look the same to you, but Python sees them as two completely different strings. 


# Integers
# A whole number. In programming you can add (+), subtract (-), multiply (*), and divide (/) integers in python
# print(5 + 5)
# print(5 - 5)
# print(5 * 5)
# print(5 / 1)

# Float
# In Python, any number that includes a decimal point is known as a float. This term is common across many programming languages and comes from the idea that the decimal point can “float” to different positions within the number.
print(0.5 + 0.5)
# print(5 - 5)
# print(5 * 5)
# print(5 / 1)


# Booleans Literals
# Boolean can have either TRUE or FALSE values. These values are used to represent truth values and are commonly used in conditions, comparisons, and control flow like if statements.


# Exercise
# 1. Add Comments: Write a Python program that prints your name. Add a single-line comment above the print statement to describe what the program does.

# 2. Multi-Line Comment Practice: Create a multi-line comment that describes the purpose of a simple program that calculates the sum of two numbers.

# 3. Explain the Code: Given the following code:
# x = 10
# y = 20
# print(x + y)
# Add appropriate comments to explain each line.

# 4. Disable Code with Comments: Comment out a line of code that prints "Hello World" and write a new line that prints "Hello Python!".

# 5. Multiple Variables: Assign the values "Alice", 25, and "Engineer" to the variables name, age, and profession, respectively. Print them in a sentence.

# 6. Swap Variables: Swap the values of two variables a = 5 and b = 10 using a third variable, and print the new values.

# 7. Strip Leading and Trailing Spaces: Create a string with extra spaces like " Hello World " and use the strip() method to remove them.

# 8. Strip User Input: Ask the user to enter their name with spaces (e.g., " John "). Use strip() to clean it up and greet them properly.
