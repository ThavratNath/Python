
'''Here are some of the best websites for practicing Python exercises online, each offering interactive 
challenges for a range of skill levels:

1. **LeetCode**: Known for coding challenges that test problem-solving skills, LeetCode is great for data 
structures, algorithms, and coding interview prep. It has a vast library of problems, from beginner to 
advanced, with many users sharing solutions and explanations.

2. **HackerRank**: HackerRank offers Python exercises sorted by difficulty, covering various domains 
like algorithms, data structures, and database management. Its interactive coding interface is user-friendly,
and it provides hints and solution discussions.

3. **Codecademy**: For those who want structured Python courses with interactive exercises, Codecademy 
offers beginner-friendly Python exercises and projects. Their learning paths include guided projects and 
quizzes, which help reinforce concepts.

4. **Exercism.io**: Exercism is a unique platform that provides Python exercises you can solve locally, 
with feedback from mentors. Its "mentored mode" offers personalized feedback on solutions, ideal for both 
beginners and intermediate coders.

5. **Codewars**: Codewars gamifies coding practice with a wide range of "katas" (challenges) designed by 
the community. You can level up as you complete challenges, and it has Python problems across multiple 
levels of difficulty. 

These websites should help you strengthen your Python skills through interactive and diverse challenges!'''



'''Homework: 

Create formular for basic Geometry'''


'''Math Formula exercies'''

'''1. រកផ្ទៃក្រឡា Square'''

# width = int(input("Put width: "))
# length = 50
# print(f"A = {width*length} m^2")


# '''2. រកផ្ទៃក្រឡា Rectangle, fumular: A = L*W'''

# width = int(input("Put width:  "))
# length = 50
# print(f"A = {width*length} m^2")
# print(f"P ={2*length + 2*width} m^2")


# '''3. រកផ្ទៃក្រឡា Circle, fumular: A = pi*r*r'''

# r = int(input("Put the value of r:  "))
# pi = 3.14
# print(f"A = {pi*r*r} m^2")

# '''4. រកផ្ទៃក្រឡា Triangle, fumular: A = 1/2*b*h'''

# b = int(input("Input bart: "))
# h = int(input("Input high: "))
# print("A =", 1/2*b*h, "m^2")

# '''5. រកផ្ទៃក្រឡា Prallelogram, fumular: A = b*h'''

# b = int(input("Put bart:  "))
# h = int(input("Put high:  "))
# print(f"A = {b*h} m^2")


# '''6. រកផ្ទៃក្រឡា Circular Sector, fumular: A = 3.14*r*r*m/360*l'''

# r = int(input("Put value of r: "))
# m = int(input("Put value of m: "))
# l = int(input("Put value of l: "))
# print(f"A = {3.14*r*r*m/360*l} m^2")


# '''7. រកផ្ទៃក្រឡា Circular Ring, fumular: Area = 3.14*((R*R)-(r*r))]'''

# R = int(input("Put value of R: "))
# r = int(input("Put value of r: "))
# print(f"Area = {3.14*((R*R)-(r*r))} m^2")

# '''8. រកផ្ទៃក្រឡា Sphere, fumular: V = 4/3*3.14*r*r'''

# r = int(input("Put value of r: "))
# print(f"V = {4/3*3.14*r*r} m^2")

# '''8. រកផ្ទៃក្រឡា Trapezoid, fumular: Arear = h*(b1+b2)/2'''

# h = int(input("Put the value of heigh: "))
# b1 = int(input("Put the value of b1: "))
# b2 = int(input("Put the value of b2: "))
# print(f"Area = {h*(b1+b2)/2} m^2")

# '''8. រកផ្ទៃក្រឡា Rectangular Prism, fumular: V = l*w*h'''

# l = float(input("Please enter the value of length: "))
# w = float(input("Please input the value of width: "))
# h = int(input("Please enter the value of height: "))
# print(f"V = {l*w*h} m^2")


# '''9. រក V of Cube, fumular: V = s*s*s'''

# s = float(input("Please enter the value of s: "))
# print(f"V = {s*s*s} m^3")

# '''10. រក V of Cylinder, fumular: V = 4/3*3.14*r*r*r'''

# r = int(input("Please enter the value of r: "))
# print(f"V = {4/3*3.14*r*r*r} m^3")

# '''11. រក V of the right Circular Cone, fumular: V = 1/3*3.14*r*r*h'''

# r = int(input("Please enter the value of r: "))
# h = int(input("Please put the values of height: "))
# print(f"V = {1/3*3.14*r*r*h} m^3")




'''Practice'''

'''1. Arithmetic Calculation'''

# print("20 + 30 + 40 =", 20 + 30 + 40, "$") # or We can try as follow. 
# print(f"20 + 30 + 40 = {20 + 30 + 40} $") 

# result = 3 * 45 / 6 + 6
# print(str(result) + "m^3")

'''2. Inputing Float'''

# len = float(input("Enter the leng of the triangle: "))
# print(len)


'''3. Inputing String'''

'''a'''

# # Ex:
# name = input("Enter your name: ")
# print(f"Hello Mr {name}, nice to meet you here. ?")


# age = int(input("How old are you? "))
# print("You are a middle age. I am grad to see you here.")
# birth_year = int(input("When were you born? I was born in "))
# print("I see.")
# answer = input("Are you married? ")
# print("Oh, really?")
# heigh = float(input("How tall are you? "))
# print("It is a good height.")

'''b'''

# birth_year = int(input("Input your birth year: "))
# age = 2024 - birth_year
# print(f"I guess you are {age} year old this year. You look so young.")


'''C: using 'and': Create code where user can put their username and password'''

'''Output: Login Fail if the user used the incorrect user name, or incorrect password.''' 

# username = input("Enter your name: ")
# password = int(input("Enter your correct password: "))

# if username == "Thavrat" and password == 123:
#     print("Login Successful")
# else:
#     print("Login Fail")
    
'''Another way'''
# username = input("Enter your name: ")
# password = int(input("Enter your password: "))
# a = "Login successfully" if username == "Thavrat" and password == 123 else "Login fail"
# print(a)

'''d: using 'or' ''' 

# username = input("Enter your name: ")
# password = int(input("Enter your password: "))

# if username == "Thavrat" or password == 123:
#     print("Login successfully")
# else:
#     print("login fail")

'''Another way'''

# username = input("Enter your name: ")
# password = int(input("Enter your correct password: "))
# a = "Login Successful" if (username == "Thavrat" or password == 123) else "Login Fail"
# print(a)


'''e'''

# email = input("Enter your correct email: ")
# password = int(input("Enter your correct password: "))
# a = "Login successful" if email == "thavratnath@gmail.com" and password == 123 else "Login failed"
# print(a)


'''Another way'''

# email = input("Enter your correct email: ")
# password = int(input("Enter your correct password: "))

# if email == "thavratnath@gmail.com" and password == 123:
#     print("Login successul")

# else:
#     print("Login failed")
    

'''Another way '''

# email = input("Enter your correct email: ")
# password = int(input("Enter your correct password: "))

# a = (email == "thavratnath@gmail.com" and password == 123)
# print("Login Success" if a else "Login Fail")



'''Practice Exercies from the Handout 1_ETEC (Operator)'''


'''1. P and A of Rectangle'''

# w = int(input(" Enter the value of width of the rectangle: "))
# l = int(input(" Enter the value of length of the rectangle: "))
# print("P = ", 2*l + 2*w)
# print("A = ", l*w)

'''2_Find each score, Total score and Average score'''

# sc1 = float(input("Enter your score 1: "))
# sc2 = float(input("Enter your score 2: "))
# sc3 = float(input("Enter your score 3: "))
# sc4 = float(input("Enter your score 4: "))
# sc5 = float(input("Enter your score 5: "))

# each_score = (sc1, sc2, sc3, sc4, sc5)  # Group scores into a tuple
# total_score = sc1 + sc2 + sc3 + sc4 + sc5
# average_score = total_score / len(each_score)


# print("Each score: ", each_score)
# print("Total score: ", total_score)
# print("Average score: ", average_score)

'''3_Show the toal price and payment of the Product after discount'''


# code = int(input("Put the code number: "))
# name = input("Put the name of product: ")
# qty = int(input("Put the quantity of product: "))
# price = float(input("Enter the price of item: "))
# discount = int(input("Input the discount percentage: "))  # discount is in percentage

# # Calculate total before discount
# total_price = qty * price

# # Calculate payment after discount
# discount_amount = total_price * (discount / 100)  # discount percentage converted to a decimal
# payment = total_price - discount_amount

# print("Total before discount:", total_price)
# print("Discount amount:", discount_amount)
# print("Total payment after discount:", payment)




'''4_Write the code that allow the user to enter three numbers. Then find Average, Maximun number, Minimun number'''


# n1, n2, n3 = int(input("a: ")), int(input("b: ")), int(input("c value: "))

# # Calculate the average
# average = (n1 + n2 + n3) / 3

# # Find the maximum and minimum values
# max_value = max(n1, n2, n3)
# min_value = min(n1, n2, n3)

# # Print the results
# print("Average:", average)
# print("Maximum:", max_value)
# print("Minimum:", min_value)

'''5: Write the Code that allows the user to input the value of princile (ប្រាក់កម្ចី), rate and duration for returning the loan (time)'''

# Get inputs from the user
# principal = float(input("Enter the amount of money you borrow from the bank: "))
# rate = float(input("Enter the interest rate that the bank charges (as a percentage): "))
# duration = int(input("Enter the duration (in years): "))

# # Calculate the total payment (simple interest)
# total_payment = (rate / 100 * principal * duration) + principal

# # Display the result
# print("The total amount to be paid after", duration, "years is:", total_payment)

'''lower()'''

# a = input("Enter your correct name: ").lower()
# if a  == "thavrat" or a == "tyhour":
#     print("Hello,", a)
# else:
#     print("Invalid")

'''upper()'''

# a = input("Enter your correct name: ").upper()
# if a  == "THAVRAT" or a == "tyhour":
#     print("Hello,", a)
# else:
#     print("Invalid")



'''Sample'''
'''a. Find the Payment after discount'''

# price =float(input("Enter price: "))

# qty = int(input("Enter Qty: "))
# total = price * qty 

# if total >=0 and total <10:
#     discount = 0
# elif total >= 10 and total < 25:
#     discount = 5
# else:
#     discount = 10

# payment = total - (total * discount/100)

# print(f"Total = {total}$")
# print(f"After discount {discount}%")
# print(f"Payment = {payment}$")




# import Function
# # Function.positive()

# Function.print(sum(x, y

# def sum_experimental(x, n):
#     if n==1:
#         y = k
#     else:
#         y = 0
#     for i in range(1, n):
#         y + 5*((10**k)-1)/9
#         return y




#from function import my_sum
# from function import bc
# if __name__ == '__main__':
#     bc()

# from function import greet



'''Homework 1'''
'''Homework 2'''

'''1'''
# def add_number(a,b):
#     add = a + b
#     return add
# print(add_number(45, 67))
'''or'''

# def add_number(a, b):
#     return a + b

# a, b = eval(input("Enter a: ")), eval(input("Enter b: ")) # The eval() function in Python is a powerful built-in function that takes a string as input and evaluates it as a Python expression. Essentially, it parses the input string and executes it as if it were a Python expression.

# print(add_number(a, b))

'''or'''

# def add (a, b):
#     print("a", a)
#     print("b", b)
#     return a + b
# print(add(b=50, a = 30))



'''2'''
# def is_even(a):
#     if a % 2==0:
#         return True
#     else:
#         return False


# print(is_even(4544))


'''or'''

# def is_even(a):
#     if a % 2==0:
#         return True
#     else:
#         return False

# number = int(input("Enter a: "))
# print(is_even(number))


'''or'''

# def is_even(a):
#     return a % 2==0  # the value will be given as boolean (True or False)

# print(is_even(59))


'''3'''
# def factorial(n):
#     fac = 1
#     for i in range(1, n):
#         fac = fac * i
#     return fac

# print(factorial(4))

'''or'''

# def factorial(n):
#     n = abs(n)      # abs is the built-int function that convert all number to positive. 
#     fac = 1
#     for i in range(1, n+1):
#         fac = fac * i
#     return fac

# print(factorial(-4))

'''4'''

# def find_max(a, b, c):
#     my_max = max(a, b, c)
#     return my_max

# print(find_max(2,4,89))


'''or'''


# def find_max(a, b, c):
#     return max(a, b, c)

# print(find_max(2,4,89))


'''or'''

# def find_max(a, b, c):
#     m = a 
#     if m > b:
#         m = b
#     if m < c:
#         m = c
#     return m

# print(find_max(2,4,89))


# data = [10, 20, "apple", 30, 40, 34, 50]
# total = 0
# co = 0
# for data in data:
#     # total =total + data
#     co = co + 1

# # mean = total/count 
# print(len(data))

# Pow()

# print(pow(9,0.5))

# def per (x, y):
#     a = 1
#     for i in range(x):
#         a *= i +1
#     b = 1
#     for i in range (x-y):
#         b *= i+ 1
#     return a/b
# print(per(5, 3))
        
# def funs(x,y):
#     sum = 0
#     for i in range(x):
#         sum +=i
#         if sum >y:
#             print(i)
#             break

# funs(10, 20)


