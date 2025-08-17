
Exception
'''Code in python is different from code in C++, as it is compiled or converted to binary code 
line by line.
If we dont want our code to be error, we can use try and error
Example: '''

# try:
#     num = int(input("Enter number: "))  # if the user put the letter, it will show error,
#     print("You enter", num)             # but if the user put number, there is no error
# except ValueError as e: # Note: try and except is similar to if and else. if if statment is true, then else statement doesnt work            
#     pass          # pass is put here so that the code below can be functioned
    
# print("Hello, friend")


'''If we want the user to put the value until corect, we can use while loop'''

# while True:
#     try:
#         num = int(input("Enter number: "))  
#         print("You enter", num)
#         break             
#     except ValueError as e: 
#         print("Invalid number")


'''Or If I want to def function, I can write it this way'''
  
# def correctnum ():     
#     while True:
#         try:
#             num = int(input("Enter number: "))  
#             return num           
#         except ValueError as e: 
#             print("Invalid number")  

# print(correctnum())


