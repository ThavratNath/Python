'''I. Condition Statement: '''
'''
1. if statement
2. if elif statement
3. if else statement'''

'''1. if statement'''
'''A'''
# age = 18
# if age > 17:
#     print("You can get married and can be my wife.")

'''B'''
# age = 17 
# if age < 17: 
#     print("You can get married.")
# else: 
#     print("You cannt get married.")

'''C'''
# ans = input("Do you love me? Yes/No :")
# if ans == "Yes" or ans == "yes" or ans == "YES":
#     print("I love your so much. ")
# else:
#     print("I hate you.")
    
'''D'''

'''if the user put the ANSWER (No), his computer will be shut down.'''

# import os         # We use this function when we want to shut down the user's computer.

# ans = input("Do you love me? Yes/No :")
# if ans == "Yes" or ans == "yes" or ans == "YES":
#     print("I love your so much. ")
# else:
#     os.system("shutdown /s /t 0")


'''E'''

# a, b, c = int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))

# if a > b and a > c:
#     print("a is the maximum number.")
# if b > a and b > c:
#     print("b is the maximun number.")
# if c > a and c > b:
#     print("c is the maximun number.")
    
# if a == b and a > c:
#     print("a and b are the maximun number.")
# if a == b and b < c:
#     print(" c is the maximun number.")
# if a == c and c > b:
#     print(" a and c are the maximun number.")
# if a == c and a < b:
#     print("b is the maximun number")
# if c == b and b > a:
#     print(" c and b are the maximun number.")
# if b == c and b < a:
#     print("b and c are the maximun number.")
# if a == b and a == c:
#     print("a, b and c are equal.")


'''
2. if elif statement & 
3. if else statement'''

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

'''b: Homework: Create grade for students. A to F
'''
# score = int(input("Enter your score: "))
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70: 
#     print("Grade: D")
# elif score >= 50 and score < 60:
#     print("Grade: E")
# else: 
#     print("Fail")


''' 
Special Case: a = value 1 if condition else value 2

Note: if condition is true, so the value 1 is assigned to a. if not, the value 2 will be assigned to a'''

'''1.'''
# a , b = 10, 20
# c = a if a > b else b
# print(c)


'''2. Find even or odd number'''

# num = int(input ("Enter a numbe: "))
# result = "even" if num % 2 == 0 else "odd"
# print(result)
    
'''Or'''
# num = int(input ("Enter a numbe: "))
# result = "even" if num % 2 == 0 else "odd"
# print("even" if num % 2 == 0 else "odd")

'''Or'''
# print("even" if int(input ("Enter a number: ")) % 2 == 0 else "odd")

'''3'''

# cart = {"id" : 1001,          # This value is called Dictionary
#         "Name: Coca": 12,
#         "price": 10}
# data = "No item in your cart" if not cart else cart
# print(data)

'''Or'''

# cart = None
# data = "No item in your cart" if not cart else cart
# print(data)

'''4'''

# is_single = True      # Value is "Boolean"
# status = "She is single." if is_single == True else "She have a boy friend."
# print(status)


#username = int(input("Enter your correct username: "))

# a = 34 % 7
# print(a)


