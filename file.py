
'''August 27, 2024'''




'''1. x _ creacte file: I can use this file to store the text.'''

'''Ex 1'''

# filename = 'file_1.txt'   # txt is the file extention.
# file = open(filename, 'x')  # Creates the file; raises an error if it exists
# file.write("This file was created using the 'x' mode.")

'''Ex 2'''
# filename = 'my_file2.txt'
# file =open(filename, 'x')
# file.write("This is my second file. I use it for test only. 123")


'''2. Write'''
'''Ex 1'''
# filename ='my_data.txt'  
# file = open(filename, 'w')
# file.write("Hello world. HoW are you doing?")

'''Ex 2'''
# filename = 'my_data.txt'
# file = open(filename, 'w')
# file.write("Hello, students. I hope this message find you well. I am writing to inform you that we dont have class next Monday. Enjoy your holodiay, class.")

'''3. R'''

# filename ='file_1.txt'  
# file = open(filename, 'r')
# content = file.read()
# print(content)

'''practice:'''
 
# filename = 'file_1.txt'
# file = open(filename, 'r')
# content = file.read()
# print(content)

# filename = 'file_1.txt'
# file = open(filename, 'r')
# content = file.read()
# print(content)


# filename = 'file_1.text'
# file = open(filename, 'r')
# content = file.read()
# print(content)


'''3. a (append)'''
'''Ex 1'''

# from getpass import getpass as get
# username = input('enter your username: ')
# password = input("enter your password: ")
# confirm_password = get("Enter your confirm password: ")

# if password == confirm_password:
#     filename = "userdata.txt"
#     file = open(filename, "a")
#     file.write(f"{username}, {password}")
#     print("Register successfully!!")
# else:
#     print("Invalid confirm password...")



'''August 28, 2024'''

'''Ex 1'''

# from getpass import getpass as get
# import os

# answer = ''

# while answer != 'Yes' and answer != 'No':
#     answer = input("Do you have an account? (Yes/No): ")
    
# filename = 'userdata.txt'    # Global variable

# if answer == 'No':
#     filename ='userdata.txt'
#     file = open(filename,'a')
#     print("Welcome to registering your account")
    
#     username = input('Enter your username: ')
#     password = get("Enter your passwor: ")
#     confirm_pass = get("Enter your confirm password: ")
    
#     if password != confirm_pass:
#         print("Invalide confirm password. Please try again.")
#     else:
#         file.write(f"{username}, {password}\n")
#         print('Your account has been created successufully.')
        

# else:
#     os.system("cls")
#     print("Log in for accessing your account.")
#     file = open(filename, 'r')      # file can be replaced by other name
#     userdata = file.read(). split(',')
#     print(userdata)
    
#     username = input("Enter your username: ")
#     password = get("Enter your password: ")

#     if username == userdata[0] and password == userdata[1]:
#         print("Log in successfully.")
#     else:
#         print("Invalid credential")
    
 

'''August 29, 2024'''
'''Homework: It was the day I was absent. I met Bong Srey'''
 
# from getpass import getpassas get
# def register (filename): 


'''Sep 2, 2024'''
import matplotlib.pyplot as pyplot # type: ignore
def person_vote():
    vote1 = 0
    vote2 = 0
    vote3 = 0
    student = int(input("How many students: "))
    for i in range(0, student):
        print("1. ka\n2. Jun\n3.Dom")
        choice = input("Enter your choice: ").upper()
        if choice == "ka":
            vote1 +=1
        elif choice == "Jun":
            vote2 +=1
        elif choice =="Dom":
            vote3 +=1
        else:
            print("Something is wrong!")
    lis = str(vote1) + str(vote2) + str(vote3)
    sizes = [int(char) for char in lis]
    index = (1, 2, 3)
    label = ("ka", "Juu", "Dom")
    pyplot.bar (index, sizes, tick_label=label, color=('red', 'green', 'blue'))
    pyplot.ylabel("Votes")
    pyplot.xlabel("Who will be the president?")
    pyplot.title("Student vote")
    pyplot.show()

person_vote()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
'''2'''
# username = input("Enter your usersername: ")
# password = int(input("Enter your correct password: "))
# corrected_password = 1122

# if password == corrected_password:


'''August 28, 2024

OOD
- Start
already have an account? 
- if already have an account, say yes
> log in 
    - username
    - password 
    after successful log in
    > use the system
    
- if do not have an account, say no, then create an account and log in again. 
    - Request admin to pay for the product
    - log in
        . username
        . password 
        . confirm password
        . key (payment)'''











# filename = 'file_1.txt'
# file = open(filename, 'x')  # Creates the file; raises an error if it exists
# file.write("This file was created using the 'x' mode.")

# try:
    
    
    
    
# except FileExistsError:
#     print(f"The file '{filename}' already exists.")
# finally:
#     file.close()  # Make sure to close the file
