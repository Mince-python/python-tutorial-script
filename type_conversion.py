# Type Conversion 
# Type conversion is the process of converting data of one type to another for example; converting integer (int) data types to string (str) data type. 

# Implicit Type Conversion is automatically performed by the python interpreter
# num1 = 50
# num2 = 0.10
# total = num1 + num2
# print('value: ', total)
# print("data type: ", type(total))

# Explicit type conversion is also called Type Casting, the data types of objects are converted using predefined functions or built in functions like int(), str(), 
num_string = '50'
num_integer = 20

# num_string = int(num_string)
# total_num = num_string + num_integer

# print('value: ', total_num)
# print("data type: ", type(total_num))

# Input Function 
# Input() is a function that is used to prompts the user to enter data, returns the entered data as a string 
# price = input("enter a product price: ")
# price = int(price)
# total = 500 + price

# print('totalprice: ', total)

# rules
# •	The value of input is a string, not a number
# •	Computer can’t add up integer and string values 
# •	We need to convert the string values into integer values before any math 

# create 3 varriable for shopping items
# A user can enter weight of the 3 items
# create a variable to add those 3 variable together
#  offer 20% discount on shopping weight
# print off total cost for shippment

# product1 = input("enter the weight of your item: ")
# print(product1 + 'kg')
# product2 = input("enter the weight of your item: ")
# print(product2 + 'kg')
# product3 = input("enter the weight of your item: ")
# print(product3 + 'kg')

# product1 = int(product1)
# product2 = int(product2)
# product3 = int(product3)

# total = (product1 + product2 + product3) * 0.20
# print(f'shipment total: , ${total}')


# Convert functions are int() and str()
# Int() and str() functions are used to switch between numbers and strings

# Create a user ID
# Collect their name, age
# Given that Their user ID number is 876241
# Convert everything to a string
# Then, print off their information

user = input("Enter user name: ")
age = input("Enter user age: ")
id_number = 876241
id_number = str(id_number)

print("Welcome " + user + "  you are " + age + "years old, your ID is: "+ id_number)


# Exercise
# 1. Remove Only Leading Spaces: Use lstrip() on the string " Start" and print the result.
# 2. Remove Only Trailing Spaces: Use rstrip() on the string "End " and print the result.
# 3. String to Integer: Convert the string "100" to an integer and add 50 to it. Print the result.
# 4. Integer to Float: Convert an integer 7 to a float. Print the result.
# 5. Check Before Converting: Given a string num_str = "45", check its type before and after converting it to an integer.

# 6. Convert User Input: Ask the user to enter their age. Convert the input to an integer and print a message like "You will be 30 in 5 years."
# 7. Simple Input: Ask the user for their name using input() and greet them.
# 8. Math with Input: Ask the user for two numbers and print their sum.
# 9. Age Calculator: Ask the user for their birth year, then calculate and display their age.

# 10. Input and Type Check: Ask the user for their height in centimeters. Convert it to an integer and print whether it’s more than 160 cm.
