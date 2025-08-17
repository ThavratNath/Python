'''Function:'''

''''
1. What is Fuction?

> A function is a block of code that performs a specific task. You can define a function once and call 
it multiple times throughout your program, which makes your code more organized and efficient.


2. Why Use Functions?

- Code Reusability: Write once, use multiple times.
- Code Organization: Break down complex problems into smaller, manageable parts.
- Avoiding Redundancy: Avoid repetitive code by defining a single function for a task.
- Easy Debugging: Easier to troubleshoot and maintain code.


> My Question: 
- What is the different between global variable, local variable, enclosing variable/nonlocal

Ex:

def function_name()
    print("I love you.")

function_name()

Note: 
Function in Python is classified into TWO types: 
1. None return Function
    a. without Paramater
    b. with Paramater
    
2. Return Function
    a. without Paramater
    b. with Paramater'''

'''
1. Non return Function'''

'''a. without Paramater

Ex 1: '''

# def ad ():
#     print("I love you.")
# ad()

'''Ex 2'''

# def add():
#     x = int(input("Enter x (integer): "))
#     y = int(input("Enter y (integer): "))
#     result = x + y
#     print(f"{x} + {y} = {result}")


# def subtraction():
#     x = int(input("Enter x (integer): "))
#     y = int(input("Enter y (integer): "))
#     result = x - y
#     print(f"{x} - {y} = {result}")


# def multiplication():
#     x = int(input("Enter x value: "))
#     y = int(input("Enter y value: "))
#     result = x * y
#     print(f"{x} * {y} = {result}")


# def division():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     if y == 0:
#         print("Error: Division by zero is undefined.")
#     else:
#         result = x / y
#         print(f"{x} / {y} = {result}")


# def modulus():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     result = x % y
#     print(f"{x} % {y} = {result}")


# def floor_division():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     result = x // y
#     print(f"{x} // {y} = {result}")


# def exponentiation():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     result = x ** y
#     print(f"{x} ** {y} = {result}")


# def menu():
#     print("""
#             [1]. Add
#             [2]. Subtraction
#             [3]. Multiplication
#             [4]. Division
#             [5]. Modulus
#             [6]. Floor Division
#             [7]. Exponentiation
#     """)


# def calculator():
#     menu()

#     choice = input("Please choose one operation: ")
#     if choice == "1":
#         add()
#     elif choice == "2":
#         subtraction()
#     elif choice == "3":
#         multiplication()
#     elif choice == "4":
#         division()
#     elif choice == "5":
#         modulus()
#     elif choice == "6":
#         floor_division()
#     elif choice == "7":
#         exponentiation()
#     else:
#         print("Invalid choice. Please try again.")


# calculator()



'''Ex 3'''

# def add():
#     x = int(input("Enter x (integer): "))
#     y = int(input("Enter y (integer): "))
#     result = x + y
#     print(f"{x} + {y} = {result}")


# def subtraction():
#     x = int(input("Enter x (integer): "))
#     y = int(input("Enter y (integer): "))
#     result = x - y
#     print(f"{x} - {y} = {result}")


# def multiplication():
#     x = int(input("Enter x value: "))
#     y = int(input("Enter y value: "))
#     result = x * y
#     print(f"{x} * {y} = {result}")


# def division():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     if y == 0:
#         print("Error: Division by zero is undefined.")
#     else:
#         result = x / y
#         print(f"{x} / {y} = {result}")


# def modulus():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     result = x % y
#     print(f"{x} % {y} = {result}")


# def floor_division():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     result = x // y
#     print(f"{x} // {y} = {result}")


# def exponentiation():
#     x = int(input("Enter the x value: "))
#     y = int(input("Enter the y value: "))
#     result = x ** y
#     print(f"{x} ** {y} = {result}")


# def menu():
#     print("""
#             [1]. Add
#             [2]. Subtraction
#             [3]. Multiplication
#             [4]. Division
#             [5]. Modulus
#             [6]. Floor Division
#             [7]. Exponentiation
#     """)


# def calculator():
#     menu()
#     while True:
        
#         choice = input("Please choose one operation: ")
        
#         if choice == "1":
#             add()
#         elif choice == "2":
#             subtraction()
#         elif choice == "3":
#             multiplication()
#         elif choice == "4":
#             division()
#         elif choice == "5":
#             modulus()
#         elif choice == "6":
#             floor_division()
#         elif choice == "7":
#             exponentiation()
#         else:
#             print("Invalid choice. Please try again.")
        
#         stop = input("Do you want to continue? Yes/No: ").upper()
#         if stop == "NO":
#             break

# calculator()



# def add() ->None:
# def add() -> String:
# def add() -> int:  
#     print("Hello, world")

'''5'''
# def ac():
#     x, y = int(input("Input x: ")), int(input("Input y: "))
#     c = x * y 
#     print(c)
# ac()


'''b with Parameter


Ex 1:'''

# def bc (x, y): 
#     a = x + y
#     print(a)

# if __name__ == '__main__':
#     print("Me")
#     bc(2,3)


# print(__name__)




# script.py
# def greet():
#     print("Hello from the greet function!")

# if __name__ == "__main__":
#     print("This script is running directly!")
#     greet()


'''2'''
# def greet(name):
#     print("Hello,", name, "How are you?")
    
# greet("Thavrat")



'''3'''


    
'''
2. Return Function

a. without Parameter : Generally, when we want the output as letter
 
Example: '''

'''1'''

# def add():      # If we do not put return, None will be the output
#     a = 2
#     b = 4
#     result = a + b
    

# print(add())        # Output None: because I did not put "return"

# '''2'''

# def add():      # If we do not put return, None will be the output
#     a = 2
#     b = 4
#     result = a + b
#     return result 


# print(add())        # Output None: because I did not put "return"

# '''3'''
# def ad():
    
#     pass

# print(ad())     # output: None

'''3'''
 

# def gf () -> str:
#     return "Hello, world!"
# print(gf())



# def add () -> str:
#     return "Hello"
# print(add())

# def message () -> None:
#     return None

# print(message())

'''b'''

# def getmessage():
#     message = input("Enter your message: ")
#     return message
# mss = getmessage
# print(mss())


'''c'''

# def getvoter () -> str:
#     age = int(input("Enter your age: ")) 
#     if age >= 18: 
#         return "You can vote"
#     else:
#         return"You cannot vote."

# print(getvoter())


'''d'''

# def my_sum():
#     """ 1 + 2 + 3 + 4 ...+ n """
#     n = int(input("Enter n: "))
#     my_sum = 0
#     for i in range(1, n+1):
#         my_sum = my_sum + i
#     return my_sum

# if __name__ == '__main__':

#     print(my_sum())

'''e'''

# def factorial():
#     """n! = ? 
#     ---------
#     enter `n` this function will \n calculate factorial
    
#     Reference: https://www.youtube.com/
#     """
#     n = int(input("Enter n: "))
#     result = 1                   
#     for i in range(1, n+1):
#         result = result * i
#     return result       # result will be returned to the viable above, factoria. 

# print(factorial() + factorial() * factorial())
    



# '''f'''
# def max ():
#     """Find the max of two numbers"""
#     a, b = int(input("Put a")), int(input("Put b"))
#     if a > b:
#         return a
#     else: 
#         return b  

# print(max())


# '''g'''

# def min (): 
#     """Find the min of two numbers"""
    
#     a, b = int(input("Put a")), int(input("Put b"))
#     if a < b: return a
#     return b
# print(min())

'''b. with Parameter: Generaly, we want the output as number

Example:'''

'''1'''

# def add (a, b)-> int:
#     result = a + b
#     return result
# result = add(2,3)
# print(result)
 
 
'''Nov 2, 2024'''
    
'''2. There are three Subjects. Find the grade''' 

'''Option 1'''

# def find_total (a, b, c):
#     result = a + b + c
#     return result


# def find_average(total, subject):
#     average = total/subject
#     return average


# def find_grade (average):
   
#     if average >= 90 and average  <= 100:
#         grade = "Grade A"
#     elif average > 80 and average  <90:
#         grade = "Grade B"
#     elif average  >70 and average  <80:
#         grade = "Grade C"
#     elif average  >60 and average  <70:
#        grade = "Grade D"
#     elif average  > 50 and average  < 60:
#         grade = "Grade E"
#     elif average  < 50:
#         grade = "Grade F"
#     else:
#         grade = "Invalid"
    
#     return grade 


# total = find_total(65, 67,87)
# average = find_average( total, 3)
# grade = find_grade(average)

# print("Total =", total)
# print("Average =", average)
# print("Grade =", grade)

'''Option 2'''

# def find_total(Math, Khmer, English):
#     tol = Math + Khmer + English
#     return tol
# total = find_total(60, 54, 100)   # total become the global variable
    
# def find_average(total, subject): 
#     avg = total/subject
#     return avg

# average = find_average(total, 3)

# def find_grade(average):
#     if average <50:
#         grade = "Grade F"
#     elif average <=60:
#         grade = "Grade E"
#     elif average <= 70:
#         grade = "Grade D"
#     elif average <= 80:
#         grade = "Grade C"
#     elif average <=90:
#         grade = "Grade B"
#     elif average <= 100:
#         grade = "Grade A"
#     else:
#         grade = "Invalid"
    
#     return grade
# real_grade = find_grade(average)

        
# print(f"""
#       Total = {total}
#       Average = {average:.2f}
#       Grade = {real_grade}
#       """ )



# def ae (x, y):
#     return x + y

# print(ae(2, 4))


'''Nov 3, 2024'''


'''In Function, there in ONE Variable which is called Variable Scope: 
Variable Scope  is Classified into 3:

1. Local scope
2. Global scope
3. Enclosing Scope (Nonlocal)

Example

1. Local scope: it only works in Function'''

# def ah ():
#     local_scope = "It is local scope. We cannot use local variabl in other block. "
#     print(local_scope)

# ah()


'''2. Global scope: We place this data above the function, and we can use it in the Function
# when we want.'''

'''a'''
# global_scope = "Global scope"
# def ab1(): 
#     print(global_scope)

# ab1()

# '''b'''

# x = 500
# def ab2(): 
#     global x       
#     x = 200     # x is no longer the local variable. It is the global vairaible. 
#     print(x)

# # ab2()



'''a'''

# def container ():
#     def add(a, b):
#         print(a + b)
#     add(3, 4)
# container()

'''b'''

# def container ():
#     def add(a, b):
#         print(a + b)
#     return add

# a = container()
# a(3, 5)


'''c'''

# def container ():
#     def add(a, b):
#         print(a + b)
    
#     def sub (a, b):
#         print(a - b)
        
#     return add, sub    # tupl
#     return [add, sub]   # list: (it doesnt work as it return of tupl stop the everything below it)
#     return (add, sub)   # set

# a = container()[1]
# a(3, 5)


'''d'''

# def container ():
#     def add(a, b):
#         print(a + b)
    
#     def sub (a, b):
#         print(a - b)
        
#     return (add, sub)       # tupl
#     return [add, sub]       # list: (it doesnt work as it return of tupl stop the everything below it)
#     return {add, sub}       # set 

# a = container()[0]      # [0] is the index
# a(3, 5)


'''e'''

'''f'''

'''g'''

'''h'''



'''3. Enclosing scope (Nonlocal):the concept of the enclosing scope is used when dealing 
with nested functions, where one function is defined inside another. WIth Nonlocal, we can change the local 
variable without changing the variable name.   

# Example a '''

# def outer_function ():    
#     outer_variable = "Local variable/enclosing scope"
    
#     def inner_function(): # Nested Function where one Function is defined inside another Function. 
#         nonlocal outer_variable
#         outer_variable = "Modified value"
#     inner_function() # Call the inner function first so that the value of variable is changed before printing out. 
#     print(outer_variable) # We cannot put the print(outer_variable) before calling inner_function()
#     # Doing so can make the result different. The original value_Local variable/enclosing scope is printed
#     # printed out first, then call the inner_funtion later. 

# outer_function()
    
    
    
# '''Example 2: '''

# def outer_function():
#     x = 10  # This variable is in the enclosing scope

#     def inner_function():
#         nonlocal x  # Declare that x refers to the variable in the enclosing scope
#         x += 5

#     inner_function()
#     print(x)

# outer_function()

# # output is: 15


# '''Practice'''

# # '''Argument is the value that is passed to the fuction when it is called, 
# # while Paramater is the variable that is put in the parenthesis. 
# # When the Fuction does not have an argument, we just call the fuction. Then the code
# # under the function will be called out.

# #  No paramater and argument

# '''1'''
# # def greeting ():
# #     print("Hello, guys")
# #     print(2 * 3)
# #     print(4/5)
# #     print(4+4+6)
# # greeting()

# # def ilove ():
# #     for i in range(10):
# #         print(i)
# #         i +=1
# # ilove()


# # def ilike ():
# #     b = 0
# #     while b <=10:
# #         if b == 5:
# #             print("ok")
# #         print(b)
# #         b +=1

# # ilike()

# '''2'''

# def add():
#     x, y = int(input("Enter x: ")), int(input("Enter y: "))
#     print(f"x + y = {x + y}")

# def sub():
#     x, y = int(input("Enter x: ")), int(input("Enter y: "))
#     print(f"x - y = {x - y}")

# def multiply():
#     x, y = int(input("Enter x: ")), int(input("Enter y: "))
#     print(f"x * y = {x * y}")

# def divide():
#     x, y = int(input("Enter x: ")), int(input("Enter y: "))
#     print(f"x / y = {x / y}")

# def floor_division():
#     x, y = int(input("Enter x: ")), int(input("Enter y: "))
#     print(f"x // y = {x // y}")

# def power():
#     x, y = int(input("Enter x: ")), int(input("Enter y: "))
#     print(f"x ** y = {x ** y}")

# def calculator():

#     print("""
#         || [+] Add                  ||
#         || [-] Subtract             ||
#         || [*] Multiply             ||
#         || [/] Divide               ||
#         || [//] Floor Division      ||
#         || [**] Power               ||
#     """)
#     choice = input("Please select an operation: ")
    
#     if choice == "+":
#         add()
#     elif choice == "-":
#         sub()
#     elif choice == "*":
#         multiply()
#     elif choice == "/":
#         divide()
#     elif choice == "//":
#         floor_division()
#     elif choice == "**":
#         power()
#     else:
#         print("Invalid choice. Please try again.")

# calculator() 



'''August 22, 2024'''

'''No paramater and argument_return'''
# def positive ():
#     while True: 
#         n = int(input("Enter positive number: "))
#         if n < 0:
#             return   #(return = break. The code execution is not procceded. )
#         print(f"the positive number you entered is {n}")
        
'''2'''     

# def positive():
#     return
# print(positive())

'''Output: None'''

'''3'''
# def positive():
#     return 123
# print(positive())

'''Output: 123'''

'''4'''
# def positive():
#     return "Hello"
# print(positive())

'''Output: Hello'''

'''5'''
# def _List(): 
#     return[1, 2, 3, "Hello", 0.3]
# print(_List())

'''Output: 1, 2, 3, "Hello", 0.3'''


'''With paramater and argument
+ Paramater refers to the variable in the bracket
+ Argument refers to the value assigned to the viable'''
'''6'''
# def sum (x, y):       # x and y are called paramater
#     return x + y
# print(sum(3, 4))      # 3 and 4 are called argumnet. 


'''Output: 7 '''

'''7'''

# def sum (x, y):
#     return x + y
# x, y = int(input("Enter the value of x: ")), int(input("Enter the value of y: "))

# print(sum (x, y))


'''Or'''
# def sum ():
#     x, y = int(input("Enter x: ")), int(input("Enter y: "))
#     return x + y

# print(sum())

'''Or'''
# def sum ():
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
    
#     return x + y

# print(sum())

'''or'''
# def sum():
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     return x + y

# s = sum
# print(s())



'''8'''

# def sum(n): 
#     s = 0
#     for i in range(1, n+1):
#         s = s + i
#     return s
# print(sum(5))

'''9'''

# def is_even(a):
#     if a % 2==0:
#         return True
#     else:
#         return False
# a = int(input("Enter the value of a: "))

# print(is_even(a)) 
        

# def db():
#     a = 0
#     while a < 5:
#         a += 1
#         print(a)

# db()  # Call the function with an initial value for `a`


# def cd():
#     for a in range(10):
#         print(a)

# cd()
        
        
''' Code for Traffic light in Cambodia.'''

# import time

# def traffic_light():
#     while True:  # Infinite loop to keep the traffic light running
#         # Green Light
#         print("Green light - Go!")
#         time.sleep(5)  # Green light for 5 seconds
        
#         # Yellow Light
#         print("Yellow light - Slow down!")
#         time.sleep(2)  # Yellow light for 2 seconds
        
#         # Red Light
#         print("Red light - Stop!")
#         time.sleep(5)  # Red light for 5 seconds

# # Run the traffic light simulation
# traffic_light()



'''Traffic light with time and date'''

# import time
# import datetime

# def traffic_light():
#     while True:
#         # Red light for 60 seconds
#         print("\033[1;31mRed Light - Stop")
#         display_time()
#         time.sleep(60)
        
#         # Yellow light for 5 seconds
#         print("\033[1;33mYellow Light - Get Ready")
#         display_time()
#         time.sleep(5)
        
#         # Green light for 60 seconds
#         print("\033[1;32mGreen Light - Go")
#         display_time()
#         time.sleep(60)

# def display_time():
#     # Display the current time
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"Current Time: {current_time}\n")

# # Run the traffic light simulation
# traffic_light()


'''Traffic Light Project'''
# import time

# def traffic_light():
#     while True:  # Infinite loop to keep the traffic light running
       
#         for i in range(30, 0, -1):  # Red light (45 seconds)
#             print(f"\rRed Light: {i} second", end="")
#             time.sleep(1)

#         for i in range(30, 0, -1): # Green light (40 seconds)
#             print(f"\rGreen Light: {i} second", end="")
#             time.sleep(1)

#         for i in range(5, 0, -1):  # Yellow light (5 seconds)
#             print(f"\rYellow Light: {i} second", end="")
#             time.sleep(1)

# if __name__ == "__main__":
#     traffic_light()

'''Explanation:
Red Light (45 seconds): The light stays red for 45 seconds. A countdown is displayed showing the remaining seconds.
Green Light (40 seconds): After red, the light turns green for 40 seconds with a similar countdown.
Yellow Light (5 seconds): Finally, the light turns yellow for 5 seconds before the cycle repeats.
The \r character is used to overwrite the line in the console, giving the appearance of a countdown timer.
The time.sleep(1) function pauses the program for 1 second between each iteration to simulate the passage of time.
Running the Program:
When you run the code, it will continuously cycle through the traffic light sequence, displaying the seconds remaining for each light. To stop the program, you'll need to manually interrupt it (e.g., using Ctrl+C in the terminal).'''



'''August 26, 2024'''


'''Database: is like Exel, Words,.... Database is software. We need hardware to proceed software.
Enterty: sth where we put our data. 
Server is sth that run database. '''



# x = 100
# def fd ():
#     x = 200
#     print(x)
# print(x)
# fd()

# x = 100
# def fd():
#     global x
#     x = 200
#     print(f"x inside function = {x}")
#     return x
# fd()

# print(f"x outside function = {x}")

# x = 100
# def fd():
#     global x
#     x = 200
#     print(f"x inside function = {x}")
# fd()
# print()


# def sum():
#     a = 10
#     b = 20
#     return a + b
# print(sum())

# def sum(a+b):
#     return a+b
# print(sum(1,3))

# for i in range (5,)

'''Sep 5, 2024'''

'''Lambda
In Python, a lambda expression (or lambda function) is a way to create small, anonymous functions at runtime. The syntax is:

```python
lambda arguments: expression
```

Here’s a quick breakdown:
- **`lambda`**: The keyword that introduces the lambda function.
- **`arguments`**: A list of parameters that the lambda function accepts.
- **`expression`**: A single expression that is evaluated and returned.

### Example

```python
# A lambda function that adds 10 to the input
add_ten = lambda x: x + 10

print(add_ten(5))  # Output: 15
```

### Common Use Cases

1. **With `map()`**: Apply a lambda function to each item in an iterable.

    ```python
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16]
    ```

2. **With `filter()`**: Filter items in an iterable based on a lambda function.

    ```python
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4]
    ```

3. **With `sorted()`**: Use a lambda function to sort elements based on a specific criterion.

    ```python
    pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
    sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
    print(sorted_pairs)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]
    ```

Lambda functions are useful for short, throwaway functions that are used only once or twice in your code.'''





'''We can use Lambda to replace expression (culculation of number under the def function)'''

# def add(x):
#     return x + 10   # the row is the expression _culcution of number

'''Invoke function: cause it to function'''
# add = lambda x: x + 10          # This row is called a lambda expression
# print(add(30))


'''Example 1'''

# def is_event_number(n):
#     if n % 2 == 0:
#         return True
#     else: 
#         return False

'''or'''

# def is_event_number(n): # Make the processor can run faster
#     return n % 2 == 0

'''or: using lambda expression: It is shorter'''

# is_even_number = lambda n: n % 2 == 0
# print(is_even_number(4))
# ''' output: True'''

# is_even_number = lambda n: n % 2 == 0
# print(is_even_number(5))
# ''' output: False'''


'''Example 2'''

# count = 1
# odd_month =[]

# for month in range(1, 13):
#     if count % 2 !=0:
#         odd_month.append(month)
#     count += 1
#     if count > 7:  # Because July and August are both odd month
#         count = 1
# print(f"These are the month ending on 31th: {odd_month} ")
    

# leap_year = []
# for year in range (1950, 2025):
#     # print(year)
#     if year % 400 == 0:
#         leap_year.append(year)
#     elif year % 4 == 0 and year % 100 !=0:
#         leap_year.append(year)

# print(leap_year)




# leap_year = []

# start_year = int(input("Enter the start year: "))
# end_year = int(input("Enter the end year: "))
# for year in range (start_year, end_year + 1):
#     # print(year)
#     if year % 400 == 0:
#         leap_year.append(year)
#     elif year % 4 == 0 and year % 100 !=0:
#         leap_year.append(year)

# print(leap_year)

'''Enter the data in the list'''

# leap_year = []
# file = open('leap_year.txt', "w")
# start_year = int(input("Enter the start year: "))
# end_year = int(input("Enter the end year: "))
# for year in range (start_year, end_year + 1):
#     # print(year)
#     if year % 400 == 0:
#         file.write(f"{str(year)}, ")
#         leap_year.append(year)
#     elif year % 4 == 0 and year % 100 !=0:
#         file.write(f"{str(year)}, ")

# print(leap_year)


'''day = 19
month = 3
year = 2004
'''


"Write code that allow th user to put their birth date, birth month, and birth year. And they can see the remaining day, month, and year"


# def greeting() -> None:
#     print("Hello, dear")
    
# def display ():
#     print("I am Joe")

# def me():
#     print ("How are you?")


# if __name__ == '__main__':
    
#     greeting()
#     display()
#     me()
#     print('Can we be friend?')     # the code under the (if__name__== '__main__':) will not be executed in other 
    # module because __name__=='_main_'
    
    
# if __name__ == 'function':  # the code under the (if__name__== '__main__':) will be executed in other 
    # module because __name__=='__the name of the other file_'
# function is the name of the file. Then when we print it at other file, then the block of code under if name ==, will be called. 
    
#     greeting()
#     print()
       


'''Nov 9, 2024'''

'''A lambda function is a small, anonymous function defined using the `lambda` keyword.

 Syntax
```python

lambda parameter: expression

Ex 1: '''

# add = lambda a, b: a + b 
# print("Sum:", add(2, 4))

'''Ex 2'''
    

# def leap_year(year):
#     if year % 400 ==0:
#         return True
#     elif year % 4 == 0and year % 100 != 0: 
#         return True
#     else:
#         return False
    
# print("Leap year", leap_year(2024))

"or"

def leap_year(year):
    return year % 100 ==0 or year % 4 == 0 and year % 100 !=0

yr = int(input("Enter Year: "))
print("Leap year: ", leap_year(yr))


'''or '''

# leap_year = lambda year: year % 100 ==0 or year % 4 == 0 and year % 100 !=0
# print("Leap year: ", leap_year(2024))



'''Nov 10, 2024'''

