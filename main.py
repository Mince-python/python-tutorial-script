# print("Hi Guys, I'm Learning python")
# # This is a Decision Statement
# if 10>5:
#     print("Ten is Greater Than Five!")
#     print("Ten is Greater Than Five!")
    
# Git Version Control

# We are taking a step forward when it comes to our python learning
# nickName = 'Hackustaz' 
# age = 250 
# email= 'infohack@fake.com'
# message = f"Welcom..!, My nickName is {nickName} \n\t  And I am {str(age)}  years old\n\t\t you can reach me at {email}\n ******Thanks"
# print(message)

# nickName = 'hackustaz' 
# # capitalize string
# print(nickName.capitalize())
# # # make all uppercase
# print(nickName.upper())
# # # make all lowercase
# print(nickName.lower())
# # # Get length
# print(len(nickName))
# # # Repace
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
# 'python'
# 'python  '

# num1 = 50
# num2 = 0.10
# total = num1 + num2
# # display total and resulting data type
# print("value: ", total)
# print("Datatype: ", type(total))

# num1 = '50'
# num2 = 20
# print("Data type of num1 before type casting : ", type(num1))
# # explicit type conversion 
# num1 = int(num1)
# print("Data type of num1 after type casting : ", type(num1))
# total = num1 + num2
# print("value: ", total)
# print("Data type of total : ", type(total))

# price = input('Price of item: ')
# total = 500 + price
# price('Totalprice: ', total)

# price = input('Price of item: ')
# price = int(price)
# total = 500 + price
# print('Totalprice: ', total)

# shopping
# create 3 varriable for shopping items
# A user can enter weight of the 3 items
# create a variable to add those 3 variable together
#  offer 20% discount onn shopping weight
# print off total cost for shippment

# product1 = input("Enter the weight of product1: ")
# print(product1 + 'kg') 
# product2 = input("Enter the weight of product2: ") 
# print(product2 + 'kg') 
# product3 = input("Enter the weight of product3: ") 
# print(product3 + 'kg') 

# product1 = int(product1)
# product2 = int(product2)
# product3 = int(product3)

# total = (product1 + product2 + product3) * 0.20
# print("shipment total: ", f'${total}')

# create a user ID
# collect their name, age
# Given that Their user iD number is 876241
# convert everything to a string
# Then, print off their information

user = input("Enter user name: ")
age = input("Enter your age: ")

id_number = 876241
id_number = str(id_number)
print(f"Welcome {user}, You're {age}, Your ID is: {id_number}")