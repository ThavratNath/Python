'''Nov 29, 2024'''

'''String'''

'''Strings in python are surrounded by either single quotation marks, or double quotation marks.'''

'''1. Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:'''

'''Ex'''
# print("You are my best friend,'Hero'")

'''2. Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:'''

a = 'Hi, there'
# print(a)

'''3. Multiline Strings
You can assign a multiline string to a variable by using three quotes:'''

# a = """ Hello,
# Thavrat. How are you?
# I am fine"""
# print(a)

'''or'''
# a = ''' Hello,
# Thavrat. How are you?
# I am fine'''
# print(a)

'''4. String are array.
Square brackets can be used to access elements of the string.

Example
Get the character at position 1 (remember that the first character has the position 0):'''

# a = "Hello, my friend"
# print(a[7]) # output: m

'''5. Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.

Example
Loop through the letters in the word "apple":'''


# for i in "apple":
#     print(i)
# # output:
# '''
# a
# p
# p
# l
# e
# '''

'''6. String Length
To get the length of a string, use the len() function.

Example
The len() function returns the length of a string:'''

# a = "I love you."
# print(len(a))  # output: 11


'''7. Check String

To check if a certain phrase or character is present in a string, we can use the keyword in.

Example:

Check if "free" is present in the following mytex:'''

# a = "I am so free now." # The value is boolean, True or False
# print("free" in a) # Output: True

'''7.1. Use a certain phrase or word in an if statement:'''

# a = "I am so free now."
# if "free" in a:
#     print("Free is in a is Ture")


'''8. Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Example
Check if "expensive" is NOT present in the following text:'''

# a = "My car is fancy."
# print("expensive" not in a) # Output: True

'''8.1. Use a certain phrase or word in an if statement:'''

# a = "My car is fancy."
# if "expensive" not in a:
#     print("Expensive is not present.")

'''9. Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

ExampleGet your own Python Server
Get the characters from position 2 to position 8 (not included):'''

# a = "Hi, friend. How are you?"
# print(a[4:8])   # Ouput: frie

'''9.1. Slice From the Start

By leaving out the start index, the range will start at the first character:

Example
Get the characters from the start to position 8 (not included):'''

# a = "Hi, friend. How are you?"
# print(a[:8])   # Ouput: Hi, frie


'''9.2. Slice To the End

By leaving out the end index, the range will go to the end:

Example
Get the characters from position 2, and all the way to the end:
'''
# a = "Hi, friend. How are you?"
# print(a[4:])   # Ouput: friend. How are you?

'''9.3 Negative Indexing

Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''

# b = "Hello, World!"
# print(b[-5:-2])  # orl

'''10. Modify Strings

Python has a set of built-in methods that you can use on strings.
'''
'''10.1 Upper Case'''

'''Example: 
The upper() method returns the string in upper case:'''
# a = "Hi, there"
# print(a.upper()) # Output: HI, THERE

'''10.2 Lower Case
Example
The lower() method returns the string in lower case:'''

# a = "Hi, there"
# print(a.lower()) # Output: hi, there

'''10.3 Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example

The strip() method removes any whitespace from the beginning or the end:'''
# a = " Hello, Hello "
# print(a.strip())

'''10.4 Replace String

Example
The replace() method replaces a string with another string:'''

# a = "Hello, World!"
# print(a.replace("H", "J")) # Jello, World!

'''10.5 Split String

The split() method returns a list where the text between the specified separator becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of the separator:

'''
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']


'''11. String Concatenation
To concatenate, or combine, two strings you can use the + operator.

Example

Merge variable a with variable b into variable c:

'''
# a = "Hello"
# b = "World"
# c = a + b
# print(c) # HelloWorld

'''Example

To add a space between them, add a " ":'''

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c) # Hello World

'''12. String Format

As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

Example
'''
# age = 36
# txt = "My name is John, I am " + age
# print(txt) # TypeError: can only concatenate str (not "int") to str

'''But we can combine strings and numbers by using f-strings or the format() method!'''

'''12.1 F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

Example
Create an f-string: '''

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt) # My name is John, I am 36

'''12.2 Placeholders and Modifiers

A placeholder can contain variables, operations, functions, and modifiers to format the value.

Example
Add a placeholder for the price variable:'''

# price = 59
# txt = f"The price is {price} dollars"
# print(txt) # The price is 59 dollars 

'''A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like 
.2f which means fixed point number with 2 decimals:

Example
Display the price with 2 decimals:'''

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt) # The price is 59.00 dollars

'''A placeholder "{}" can contain Python code, like math operations:

Example
Perform a math operation in the placeholder, and return the result:'''

# txt = f"The price is {2*3} dollars" # The price is 6 dollars
# print(txt)


