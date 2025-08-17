
'''Operator:

1. Arithmetic Operator      (Result: number)
+, -, *, /, //, %, **

2. Assigment Operator       (Result: number)

=, +=, -=, *=, /=, //=, %=, **=

3. Comparison Operator      (Result: True or False)

1. >
2. >=
3. ==
4. <
5. <=
6. !=

. == : when the two value is the same on the left and the right side is the same. (Compare the two values
on the left or on the right of the sign)
. = : is called the assignment operator. We give the value to the variable
Ex: 2==2: true
    x = 2: (2 is the value of 2 that is assigned to variable x)
'''
# print("_"*(20) + "Comparison Operator" + "_"*(20))
# print(f"10>3 is {10>3}.")  # Expression is the value that is calculated or compare
# print(f"3<7 is {3<7}.")
# print(f"5==5 is {5==5}.")
# print(f"5>=4 is {5>4}.")
# print(f"7<=9 is {7<=9}.")
# print(f"3!=4 is {3!=4}.")
# print(f"5 > 4 + 6 {5> 4 + 6}")
# print("2020<=2021-1", 2020<=2021-1)
# print("5*3<3*5", 5*3<3*5)

# print("A <= B", 5 * 10 /2 <= 8*12/2)


'''Compare letter and letter
A= 65
B = 66
C = 67
...Z = 90'''

'''Ex 1: From Number to Character'''
# ch = chr(65)
# print(ch)

'''Ex 2: from Character to number'''

# c = ord("Z")
# print(c)

# a, b, c = 30, 40, 50
# print(a, b, c)

# my_id, name, gender =int(input("Put your ID: ")), input("Name: "), input("Gender: ")
# print(f"ID: {my_id + 1}")
# print(f"Name: {name}")
# print(f"Gender: {gender}")          # business logic

# bank = 100
# bank = bank + int(input("Enter your new salary: "))
# print(f"My total salary is {bank} $.")


# m = 250 
# m -= int(input("How much did you spend this month?: "))
# print(f"So, the money in your bank account is {m} $.")



'''4. Logical Operator                  Result: True or False'''
'''Logical Operator is used to combine Conditional Statments.
x > 3 and y < 5, or x < 3 and y > 5: 
x > 4 or y < 7, or x < 4 or y > 7  :

not(x>5): Logical Operator
x is y : Identity Operator
x is not y: Identity Operator
x in y    : Membership Operator
x not in y: Membership Operator'''

# '''We use logical operator when we want to make the code true or false
# There are two types of logical operator: or & and

# and: condition 1 and Condition 2 => True if both conditions are Correct.
 
# If one of the conditions is not correct, the output is False.
# Ex: print (3 < 6 and 6 == 5): output is false. 
# priint(5 <=8 and 8 >=50 : output is true. 

# or: condition 1 or codition 2 => true, false'''


'''4.1 Logical operator_and'''

# a= 3 >= 2 and 4 < 8
# print(a)                    #Output: True

# print(3 >= 2 and 4 < 8)     #Output: True"

# print(4!=3 and 5==2 and 3>2) #Output: False"

# print ((6==4 and 2 >-2) and 4<5 )   # Output is False. 

# 5 < 10 and print("It works.")  # or
# print(5<10 and "It works.")

'''True C and False C
s =" ": False
s = none: False'''

# print(3==3 and "Python" and "Java")

# '''Note: We can put more than 2 conditions. Ex: 3 ==3, 3> 1 and 2 < 3
# The code will check the first condtion starting from the left side.'''


# Note: 

# 1 = true
# 0 = false'''

# '''Note: number beside 0 is all true although negative number.'''

# '''Example: 
# -1, -2, -3, -4, 1, 2, 3, 4, 5, 6...: true
# 0: False'''

# # a = True and 5 > 8
# # print(a)    : # Output: False     because the second condition is not true. 
    

# # b = True and 5 < 8

# # print(b)    # Output: True. becasue the first condition is true and the second condition is also true. 

# '''Note: Letter: '''

# # Example: 
# # a = False and "Hello world" 
# # print (a)                   # Output: Fale    because the first vairalbe is False


# # a = -10 and 10
# # print(a)                    # Output: -10  because -10 is strill true. 

# '''For letter, when the value is None, it is not true. Ex: 

# a = "Hello"
# a = None
# a and print("It is true.")
# True '''


''' 4.2 Logical Operator: OR'''

# ''' OR is used when the first value is False, it will check the second value. If the first
# value is true, then we have to print the first value. If the first value is false, we print the second value.'''

# # a = 5 or 4        Note: 5 is true. Therefore, we print 5. 
# # print(a)            # Output a = 5
# # a = 0 or 4        Note: O is not not true. Therefore, we print 4. 
# # print(a)            # Output: a = 4

# # a = (50 > 4 and 5==5) or False
# # print(a)            # Output: Tue

print("Hello World")


