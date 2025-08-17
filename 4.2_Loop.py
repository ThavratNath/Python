'''August 13, 2024'''

'''II. Loop: finite loop
while vs for: 

I. For loop: '''

'''The `for` loop is used to iterate over a sequence (like a list, tuple, or string).

Syntax

for item in sequence:
    # Code block to execute for each item
```'''

'''Example: '''

# for i in range(10+1):
#     print(f"{i} I am sorry baby.")
    
# for i in range(1, 10):
#     print(f"{i} I am sorry baby.")

# for i in range(100):
#     if i % 2 == 0:
#         print(i)

# for i in range(100):
#     if i % 2 != 0:
#         print(i)

# for i in range(100):
#     if not i % 2 == 0:
#         print(i**5)

'''August 14, 2024'''

# fruits = ["apple", "banana", "wood apple", "coconut"]
# for fruit in fruits: 
#     print(fruit)
    

# "or"

# i = 0
# while i < fruits.__len__():
#     print(fruits[i])
#     i += 1

# sum = 0 
# for i in range (5):
#     if i%2==1:
#         continue
#     sum+=1
# print(sum)


'''August 15, 2024'''

'''Argument is the value in range.
From Small to Big '''

# print("hello", end=" ")
# print("Hello world2")

'''or'''
 
# print("hello", end=" 23 ")
# print("Hello world2")


'''1'''

# for i in range(100):
#     print(i, end=" ")
    
'''2'''
# for i in range(10, 81):
#     print(i, end=" ")
    
'''3'''

# for i in range(10, 125+1):
#     print(i, end=" ")

'''4'''
# for i in range(10, 125, 3):
#     print(i, end=" ")

'''5'''
# start, stop = int(input("enter start: ")), int(input("enter stop: "))
# for i in range(start, stop +1):
#     print(i, end=", ")

'''6'''
# start, stop = int(input("enter start: ")), int(input("enter stop: "))
# for i in range(start, stop +1):
#     print(i**2, end=", ")

'''7'''

# start, stop = int(input("enter start: ")), int(input("enter stop: "))
# for i in range(start, stop +1):
#     if i%2==0:
#         continue
#     print(i, end=", ")
    
'''8'''
# start, stop = int(input("enter start: ")), int(input("enter stop: "))
# for i in range(start, stop +1):
#     if i%2 !=0:
#         break
#     print(i, end=", ")

'''Form Big to Small'''

'''9'''

# for i in range(100, 10-1, -1):
#     print(i)

'''10'''

# for i in range(50, 10-1, -3):
#     print(i)

'''11'''

# for i in range(5):
#     for j in range(3):
#         print('A', end=" ")
        
        


'''Oct 12, 2024'''
'''13'''
# for i in range (5):
#     for i in range(i+1):
#         print("*", end =" ")
#     print()     

# '''Or'''

# for i in range (5):
#       print("* "*(i+1))
      

# for i in range (4):   # i work one time, 
#       for j in range (1):   # j work one time
#           print("* * * * *", end=" ")
#       print()



'''14'''
# n = 5

# for i in range(1, n+1):
#     for j in range (i):
#           print(j+1, end =" ")
#     print()

'''15'''
# n = int(input("Enter n: "))
# for i in range(0, n +1):
#       for k in range(i):
#             print(k+1, end = " ")
#       print()
      
'''16'''
# for j in range(5): 
#   print("*", end=" ")
# print()

# for j in range(4): 
#   print("*", end=" ")
# print()

# for j in range(3): 
#   print("*", end=" ")
# print()

# for j in range(2): 
#   print("*", end=" ")
# print()

# for j in range(1): 
#   print("*", end=" ")
# print()


'''Write the exercise 16 in loop'''

# for i in range(5):
#     for j in range(5-i):
#           print("*", end="")
#     print()

'''Or'''

# n = 5 
# for i in range(n):
#       for j in range (n-i):
#             print("*", end =" ")
#       print()

'''Reduce 2 every time'''
# n = 5 
# for i in range(n):
#       for j in range (n-(i*2)):
#             print("*", end =" ")
#       print()



'''17'''
# print("# "*4, end =" ")
# print("* "*1)
# print("# "*3, end =" ")
# print("* "*2)
# print("# "*2, end= " ")
# print("* "*3)
# print("# "*1, end= " ")
# print("* "*4)
# print("# "*0, end= " ")
# print("* "*5)


'''Or'''

# print("  "*4, end =" ")
# print("* "*1)
# print("  "*3, end =" ")
# print("* "*2)
# print("  "*2, end= " ")
# print("* "*3)
# print("  "*1, end= " ")
# print("* "*4)
# print("  "*0, end= " ")
# print("* "*5)



'''Or'''

# print("  "*(4-0), end =" ")
# print("* "*1)
# print("  "*3, end =" ")
# print("* "*2)
# print("  "*2, end= " ")
# print("* "*3)
# print("  "*1, end= " ")
# print("* "*4)
# print("  "*0, end= " ")
# print("* "*5)



'''Or'''

# for j in range (4):
#       print("# ", end=" ")
# for j in range(1):
#       print("* ", end=" ")
# print()
# for j in range(3):
#       print("# ", end =" ")
# for j in range(2):
#       print("* ", end=" ")
# print()
# for j in range(2):
#       print("# ", end =" ")
# for j in range(3):
#       print("* ", end =" ")  
# print()
# for i in range(1):
#       print("# ", end =" ")
# for j in range(4):
#       print("* ", end= " ")
# print()
# for J in range(0):
#       print("# ", end =" ")
# for j in range(5):
#       print("* ", end=" ")
# print() 


'''Or : '''

# for j in range (4):
#       print("  ", end=" ")
# for j in range(1):
#       print("* ", end=" ")
# print()
# for j in range(3):
#       print("  ", end =" ")
# for j in range(2):
#       print("* ", end=" ")
# print()
# for j in range(2):
#       print("  ", end =" ")
# for j in range(3):
#       print("* ", end =" ")  
# print()
# for i in range(1):
#       print("  ", end =" ")
# for j in range(4):
#       print("* ", end= " ")
# print()
# for J in range(0):
#       print("  ", end =" ")
# for j in range(5):
#       print("* ", end=" ")
# print() 

'''17_Final Product'''


# for i in range (5):
#     print("  "*(4-i), end =" ")
#     print("* "*(i+1))


'''18: We you want to number printed out skipped a particul number, do as following'''

# for i in range(1, 10, 2):   # Start from 1, end before 10, increment by 2
#   print(i)

'''19'''
# n = int(input("put n: "))

# for i in range(1, n, 4):
#       print(i)
      

'''20'''

# n = int(input("put n: "))

# for i in range(1, n+5, 4):
#       print(i)


'''II. While loop: 

The `while` loop is used to execute a block of code as long as a condition is `True`.'''
''' 
while condition:
    # Code block to execute while the condition is True
 '''

'''1. '''

# count = 0

# while count < 3:
#     print("Count is:", count)
#     count += 1

'''2'''

# n = 0
# while n <10:
#     print(n)
#     n +=1
    

'''III. Control Flow Tools
These include `break`, `continue`, and `pass` statements that modify the behavior of loops.'''

'''A. break statement
The `break` statement is used to exit a loop before it finishes all its iterations.'''

# for number in range(5):
#     if number == 3:
#         break
#     print("Number:", number)
    
'''B. continue statement
The `continue` statement skips the rest of the code inside the loop for the current iteration 
and goes to the next iteration.'''

# for number in range(5):
#     if number == 3:
#         continue
#     print("Number:", number)


# - Output:
#   ```
#   Number: 0
#   Number: 1
#   Number: 2
#   Number: 4


'''C. `pass` Statement
The `pass` statement does nothing; it is used as a placeholder for future code.'''

# for number in range(5):
#     if number == 3:
#         pass  # Placeholder for future code
#     print("Number:", number)

# - Output:
#   ```
#   Number: 0
#   Number: 1
#   Number: 2
#   Number: 3
#   Number: 4

'''IV. '''

'''12: Nest loop, loop in loop'''
# big = 0
# for i in range(5):
#     for j in range(3):
#         for k in range(5): 
#             print(big)
#             big+=1




'''21'''

# def bb ():
#       n = int(input(" put n: "))
#       for i in range(1, n +5, 2):
#             print(i)

# bb()
# bb()

'''22'''

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

'''23: Using else` statement in for loop'''
for i in range(5):
    print(i)
else:
    print("Loop completed.")



''' Oct 13, 2024'''

'''While loop: We use it when we dont know how many time of actions: Or we can call it infinite loop'''

'''0: Using else` statement in while loop'''

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed.")
    

'''Ex 0'''
# user_input = " "  # 
# while user_input.lower() != "exit":
#       user_input = input("Type 'exit' to stop: ")

'''0'''
# def bb ():
#       count = 1
#       while count < 10:
#         print(count)
#         count += 2

# bb()
# bb()




'''1'''
# i = 0
# while i <5:
#       print("I like python")
#       i = i + 1
      
# print(i)    # the output od this is when the while loop is not true. So here, the output is 5. Because 5 is bigger the value in while  


'''2. Traffice light'''

# import time

# while True:
#       print("Red light")
#       time.sleep(3)
      
     
#       print("Green light")
#       time.sleep(3)
      
      
#       print("Yellow light")
#       time.sleep(3)
      
 
 
'''3''' 
# import time
# import os
# while True:
      
#       print("Red light")
#       time.sleep(3)
#       os.system("cls")
      
#       print("Green light")
#       time.sleep(3)
#       os.system("cls")
      
#       print("Yellow light")
#       time.sleep(3)
#       os.system("cls")
      
'''4'''

# answer = None
# while answer!= "yes": 
#       answer = input("Do you like me? Yes/No: ").lower()
#       print(answer)   # answer "Yes" is printed first, the condition is checked. The loop stop. 
      
'''5'''
# answer = None # insteat of using None, we can use (" ")
# while answer!= "yes": 
#       answer = input("Do you like me? Yes/No: ").lower()
# print(answer)   # output is (yes, because the condition is not true. Then print outside the loop works. 


'''6: Hour and Day'''
'''a. second'''

# import time
# import os 

# second = 57

# while True:

#       print(second)
#       time.sleep(1)
#       os.system("cls")
#       second +=1
      
      
'''b. minutes'''
      
# import time
# import os 

# second = 55
# minute = 0

# while True:
#       if second>59:
#           minute +=1
#           second =57
#       print(f"{minute}:{second}")
#       time.sleep(1)
#       os.system("cls")
#       second +=1


'''c. hours'''

# import time
# import os 

# second = 57
# minute = 59
# hour = 0

# while True:
#       if second==60:
#           minute +=1
#           if minute ==60:
#                 hour +=1
#                 minute =58
#           second = 56
#       print(" "*30,f"{hour}:{minute}:{second}")
#       time.sleep(1)
#       os.system("cls")
#       second +=1

'''d. day'''      

# import time
# import os 

# second = 57
# minute = 59
# hour = 23
# day = 0

# days =["Sunday", "Monday", "Tuesday", "Wednesday"]
# while True:
#       if second==60:
#           minute +=1
#           if minute ==60:
#                 hour +=1
#                 if hour ==24:
#                       day +=1
#                       hour =23
#                 minute =55
#           second =55
#       print(" "*30,f"{days[day]}:{hour}:{minute}:{second}")
#       time.sleep(1)
#       os.system("cls")
#       second +=1



'''e'''

# import time
# import os
# second = 55
# minute = 55
# hour =23
# day = 5
# days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday" ]
# week =2
# weeks = ["week 1","week 2","week 3","week 4" ]
# month =10
# months =["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"  ]
# year =0
# years =["year 1","year 2","year 3","year 4","year 5","year 6","year 7","year 8","year 9","year 10","year 11","year 12","year 1","year 1", ]

# while True:
#       if second == 60:
#             minute +=1
#             if minute==60:
#                   hour +=1
#                   if hour == 24:
#                        day +=1
#                        if day == 7:
#                              week +=1
#                              if week ==4:
#                                    month +=1
#                                    if month ==12:
#                                          year +=1
#                                    week =3
#                              day =6
#                        hour =23 
#                   minute =58
#             second =58
#       print(" "*50, f"{years[year]}: {months[month]}:{weeks[week]}:{days[day]}:{hour}:{minute}:{second}")
#       time.sleep(1)
#       os.system("cls")
#       second +=1
      


'''Junk statment: break, continue'''
'''I. break '''
'''1'''
# step = 0
# while True:
#       print(step)
#       if step ==3:
#             break
#       step +=1
      

'''2'''
# step = 0
# while True:
#       if step==10:
#             print(step)
#             break 
#       step +=2
            
# Output = 10

'''3'''
# step = 0
# while True:
    
#       if step == 10:
#             print("End") 
#             break
#       print(step, end =", ") 
#       step += 2
      
'''0, 2, 4, 6, 8, End'''
                      
'''4'''

# ad = int(input("Enter the positive number: "))
# if ad >0 and ad <5:
#       print("I like you.")
# elif ad >5 and ad < 10:
#       print("I love you")
# elif ad>10 and ad <15:
#       print("You are my everything.")
# else:
#       int(input("Enter the positive number: "))
#       print("No more chance")
      
      
'''Oct 19, 2024'''
  
'''II. Continue'''  

'''1'''

# gf = 0
# while True:
#       print (gf)
#       gf +=1
#       if gf ==5:
#             continue
#       elif gf ==10:
#             break


'''2'''      
# answer =None
# print("Can you be my girlfriend?")
# while True:
#       answer =input("[Yes/No]: ")
#       if answer == "yes" or answer=="no": 
#         break

# print("end loop! your answer is ", answer)


'''1'''
# counter =1 
# while counter <= 10:
#     print(counter)
#     counter+=1

'''2.'''
# n = 5
# factoria = 1   # We cannot give the value, zero to Factotoria
# while n >= 1:
#     factoria *= n
#     n-=1
# print(factoria)

'''3'''
# n = int(input("Enter the value of n: "))
# old_n = n
# factorial = 1
# while n >= 1:
#     factorial = factorial * n
#     n -= 1
# print(f"{old_n}! = {factorial}")

'''Or'''

# n = int(input("Enter the value of n: "))
# old_n = n
# factorial = 1
# while n >= 1:
    
#     # factorial = factorial * n
#     factorial *= n
#     n -= 1
# print(f"{old_n}! = {factorial}")



'''Example:
If the user enters n = 5:

old_n is set to 5.
The loop runs as follows:
Iteration 1: factorial = 1 * 5 = 5
Iteration 2: factorial = 5 * 4 = 20
Iteration 3: factorial = 20 * 3 = 60
Iteration 4: factorial = 60 * 2 = 120
Iteration 5: factorial = 120 * 1 = 120
The program then prints 5! = 120.'''

# n = int(input("Enter the value of n: "))
# old_n = n
# factorial = 1
# while n >= 1:
#     factorial = factorial * n
#     n -= 1
    
# print(f"{old_n}! = {factorial}")

'''How to create folders in Python'''

# import os
# dir_name = input("Enter dir name: ")
# n = int(input("Enter the number of dir: "))
# i = 1
# while i <=n:
#     os.system("f{makdir_name}{i}")
#     i+=1


'''API is the data that is already analyed from Data Science.''' 


# import time
# import os
# hour = 0
# seconds = 55
# minute = 59

# while True:
#     if seconds ==60: 
#         minute += 1
#         seconds = 0
#     if minute == 60:
#         hour += 1
#         minute = 0
#         seconds = 0
    
#     print(f"Hour = {hour}, Minute = {minute}, Seconds = {seconds}s")
#     seconds +=1
#     time.sleep(1)
#     os.system("cls")
#     if hour == 1: 
#         break 


'''August 20, 2024'''
'''Junk statment in python: break, continue, return, and exit(0)'''

'''break'''

'''1. '''
# i = 0
# while i <= 10:
#     print (i)
#     i += 1
#     if i == 4:
#         break


'''2'''

# i = 1
# while i <= 10:
#     print (i, end=", ")
#     i += 1
#     if i == 4:
#         print("I love you.")
#         break
    

'''3'''

# i = 1
# while i <= 10:
#     print (i, end=", ")
#     if i == 4:
#         print("I love you.")
#         break
#     i += 1

'''4'''

# i = 2
# while i <= 7:
#     print(i, end=", ")
#     if i%2 == 0:
#         print("Ok", end =", ")
#     i += 1



'''4. Exerciese about puting Password and waiting second'''

import time
import os

attempts = 3
correct_password = "Thavrat123"

while True:   # infinite loop
    password = input("Enter your password: ")
    
    if password == correct_password:
        print("Welcome to your account.")
        break
    else:
        attempts -= 1
        os.system("cls")
        print(f"Incorrect password. You have {attempts} attempts left.")
        
    if attempts == 0: # if attemps == 0, it means that the attem is not correct. 
        count = 8
        while count >= 0:
            os.system("cls")
            print(f"Wait for {count}s")
            time.sleep(1)
            count -= 1
        attempts = 3  # Reset attempts after the wait


'''Certainly! Let's go through the corrected code step by step to understand how it works:

### Code Overview

This Python script is a simple password-checking program that allows the user to input a password and gives them a limited number of attempts to enter it correctly. If the user fails to enter the correct password within the allowed attempts, they must wait a certain amount of time before they can try again. The script uses a combination of loops, conditionals, and system commands to achieve this.

### Step-by-Step Explanation

```python
import time
import os
```

- **Imports**: The script starts by importing two Python modules:
  - `time`: This module provides various time-related functions. In this code, it's used to create a delay between actions.
  - `os`: This module provides a way to interact with the operating system. Here, it's used to clear the screen using the `cls` command (on Windows) or `clear` (on Unix-based systems).

```python
attempts = 3
correct_password = "Thavrat123"
```

- **Initialization**:
  - `attempts = 3`: This variable keeps track of how many attempts the user has left to enter the correct password. The user is initially given 3 attempts.
  - `correct_password = "Thavrat123"`: This is the correct password that the script expects the user to enter.

```python
while True:
    password = input("Enter your password: ")
```

- **Infinite Loop**:
  - `while True`: This creates an infinite loop that will keep running until it's explicitly broken. The loop continues to prompt the user to enter their password.
  - `password = input("Enter your password: ")`: This line prompts the user to enter a password and stores the input in the variable `password`.

```python
    if password == correct_password:
        print("Welcome to your account.")
        break
```

- **Password Check**:
  - `if password == correct_password`: This condition checks if the user's input matches the correct password.
  - `print("Welcome to your account.")`: If the password is correct, this message is displayed.
  - `break`: This breaks out of the infinite loop, effectively ending the script since the user has successfully logged in.

```python
    else:
        attempts -= 1
        os.system("cls")
        print(f"Incorrect password. You have {attempts} attempts left.")
```

- **Incorrect Password Handling**:
  - `else`: If the password entered is incorrect, the code inside this block is executed.
  - `attempts -= 1`: This line decreases the number of attempts by 1 each time the user enters an incorrect password.
  - `os.system("cls")`: This command clears the console screen, removing the previous output.
  - `print(f"Incorrect password. You have {attempts} attempts left.")`: This line informs the user that the password is incorrect and shows how many attempts they have remaining.

```python
    if attempts == 0:
        count = 8
        while count >= 0:
            os.system("cls")
            print(f"Wait for {count}s")
            time.sleep(1)
            count -= 1
        attempts = 3  # Reset attempts after the wait
```

- **Out of Attempts**:
  - `if attempts == 0`: This condition checks if the user has used up all their attempts.
  - `count = 8`: If the user is out of attempts, a countdown is initiated starting from 8 seconds.
  - `while count >= 0`: This creates another loop that will run until the countdown reaches 0.
  - `os.system("cls")`: Clears the screen before displaying the countdown.
  - `print(f"Wait for {count}s")`: Displays the current countdown timer, instructing the user to wait for the specified number of seconds.
  - `time.sleep(1)`: Pauses the script for 1 second between each countdown step, creating a delay.
  - `count -= 1`: Decreases the countdown by 1 each time the loop runs.
  - `attempts = 3`: After the countdown is complete, the number of attempts is reset to 3, allowing the user to try entering the password again.

### Summary

- The code is a simple password authentication script.
- It gives the user 3 chances to enter the correct password.
- If the user fails to enter the correct password within 3 attempts, they must wait 8 seconds before they can try again.
- The screen is cleared after each incorrect attempt and during the countdown to provide a clean interface for the user.

This kind of script could be used as a basic security feature in a command-line application, ensuring that unauthorized users cannot easily guess the password without some delay.'''


'''August 21, 2024'''

# while Condition: 
#   print()

# else:
#   print()
  
  
# for i in range ():
#   print()
# else: 
#   print()



