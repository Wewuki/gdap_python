# ## create an empty class register
# class_reg = []

# # reg_count = int(input("Enter the number of students to register:"))
# # ## 25 participants
# # for each_user in range(1, reg_count + 1):
# #     ## ask for the users fullname
# #     user_input = input("Enter your fullname:")

# # ## store the users name in the class register
# # # class_reg.append(user_input)

# # # ## display the class register
# # # print(class_reg)

# # # timer = 0

# # # def function_name(parameters):
# #     # code block
# # #   return value

# # ## creating a function to add two numbers
# def users_inputs():
#     user_input1 = int(input("Enter your first number:"))
#     user_input2 = int(input("Enter your second number:"))
    
#     return user_input1, user_input2

## call user input function
# num1, num2 = users_inputs()

# ## call the addition function
# def addition(num1, num2):
#     add = addition(num1, num2)
#     print("The sum of adding two numbers: ", add)
#     print(f"The sum of adding two numbers: {add}")

# ## creating a function to subtract two numbers
# def subtraction(num1, num2):
#     ##
#     result = num1 - num2
#     return result

# ## call the subtraction function
# Subt = subtraction(12, 5)
# print("The difference of subtracting two numbers: ", Subt)
# print(f"The difference of  two numbers: {Subt}")


# create a function to compute commission
def users_inputs():
    user_input1 = float(input("sales amount:"))
    user_input2 = float(input("percentage of commission:"))
    
    return user_input1, user_input2

# call user_input function
user_input1, user_input2 = users_inputs()