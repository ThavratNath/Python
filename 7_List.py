
'''Nov 10, 2024'''

'''A. What is a List?
A list in Python is an ordered, mutable (changeable), and heterogeneous 
(can contain different types of data) collection of items.
	• Syntax: A list is defined using square brackets [].

Example:'''

# my_list = [1, 2, 3, "apple", True]

'''B. Characteristics of Lists
	1. Ordered:
		○ The items in a list have a defined order.
Example:'''
# my_list = [1, 2, 3]
# print(my_list[0])  # Output: 1

'''	2. Mutable:
		○ You can change items in a list after it is created.
Example:'''

# my_list = [1, 2, 3]
# my_list[1] = 10
# print(my_list)  # Output: [1, 10, 3]

'''	3. Heterogeneous:
		○ A list can contain different types of data.
Example:'''
# my_list = [1, "hello", True, 3.14]

'''C. Creating Lists'''
	
'''Empty List:'''

# empty_list = []

'''List with Initial Values:'''

# numbers = [1, 2, 3]
# fruits = ["apple", "banana", "cherry"]
# mixed = [1, "hello", True]

'''Using list() Constructor:'''

# numbers = list((1, 2, 3))  # Create a list from a tuple
# chars = list("hello")      # Create a list from a string
# print(chars)               # Output: ['h', 'e', 'l', 'l', 'o']


'''D. Accessing List Elements'''
'''1. Indexing:
        Use an index to access a specific element. Indexing starts from 0.'''

# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])  # Output: apple

'''2. Negative Indexing:
        Negative indices count from the end of the list.'''
    
    
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])  # Output: cherry

'''	3. Slicing:
        Extract multiple items using start:end (end is exclusive).'''

# numbers = [1, 2, 3, 4, 5]
# print(numbers[1:4])  # Output: [2, 3, 4]

'''E. List Operations'''

'''	1. Concatenation:
        Combine two lists using the + operator.'''
        
# list1 = [1, 2]
# list2 = [3, 4]
# print(list1 + list2)  # Output: [1, 2, 3, 4]

'''	2. Repetition:
        Repeat a list using the * operator.'''

# numbers = [1, 2]
# print(numbers * 3)  # Output: [1, 2, 1, 2, 1, 2]

'''3. Membership Testing:
        Check if an item is in the list.'''

# fruits = ["apple", "banana"]
# print("apple" in fruits)  # Output: True

'''	F. List Methods
    Here are the commonly used methods for working with lists:'''
    
'''	1. append():
                Adds an item to the end of the list.'''

# my_list = [1, 2]
# my_list.append(3)
# print(my_list)  # Output: [1, 2, 3]

'''     2. extend():
                Adds multiple items from another list or iterable.'''
                
# my_list = [1, 2]
# my_list.extend([3, 4])
# print(my_list)  # Output: [1, 2, 3, 4]

'''	3. insert():
                Inserts an item at a specific index.'''
# my_list = [1, 3]
# my_list.insert(1, 2) # 1 is the index, 2 is the value. 
# print(my_list)  # Output: [1, 2, 3]

'''	4. remove():
                Removes the first occurrence of an item.'''

# my_list = [1, 2, 3]
# my_list.remove(2)
# print(my_list)  # Output: [1, 3]

'''	5. pop():
            Removes and returns an item by index (default is the last item).'''
# my_list = [1, 2, 3]
# print(my_list.pop())   # Output: 3
# print(my_list)         # Output: [1, 2]

'''	6. index():
                Returns the index of the first occurrence of an item.'''
# my_list = [1, 2, 3]
# print(my_list.index(2))  # Output: 1

'''	7. count():
                Counts the occurrences of an item in the list.'''

# my_list = [1, 2, 2, 3]
# print(my_list.count(2))  # Output: 2

'''	8. reverse():
                Reverses the list in place.'''

# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  # Output: [3, 2, 1]

'''	9. sort():
            Sorts the list in ascending order (modifies the list in place)'''
# numbers = [3, 1, 2]
# numbers.sort()
# print(numbers)  # Output: [1, 2, 3]

'''or'''

# nn = [1, 3, 2, 4,2 ,5, 89]
# nn.sort()
# nn.reverse()
# print(nn)  # output: [89, 5, 4, 3, 2, 2, 1]

'''10. len()
	• Purpose: Returns the number of elements in a list.
        Example:'''
# my_list = [1, 2, 3, 4]
# print(len(my_list))  # Output: 4

'''11. min()
	• Purpose: Returns the smallest element in a list.
Example:'''

# numbers = [5, 3, 8, 1]
# print(min(numbers))  # Output: 1

'''12. max()
	• Purpose: Returns the largest element in a list.
Example:'''
# numbers = [5, 3, 8, 1]
# print(max(numbers))  # Output: 8

'''13. sum()
	• Purpose: Returns the sum of all elements in a numeric list.
Example:'''

# numbers = [5, 3, 8, 1]
# print(sum(numbers))  # Output: 17

'''14. all()
	• Purpose: Returns True if all elements in the list are truthy.
Example:'''

# numbers = [1, 2, 3, 4]
# print(all(numbers))  # Output: True (all non-zero values are truthy)

# mixed = [0, 1, 2]
# print(all(mixed))  # Output: False (0 is falsy)


'''15. any()
	• Purpose: Returns True if at least one element in the list is truthy.
Example:'''
# numbers = [0, 0, 3]
# print(any(numbers))  # Output: True (3 is truthy)

# empty = [0, 0, 0]
# print(any(empty))  # Output: False (all are falsy)

'''16. enumerate()
	• Purpose: Returns an enumerate object, which gives index-value pairs as you loop 
 through the list.
Example:'''

# items = ['a', 'b', 'c']
# for index, value in enumerate(items):
#     print(index, value)
# # Output:
# # 0 a
# # 1 b
# # 2 c

'''17. list()
	• Purpose: Converts an iterable (like a string, tuple, or set) to a list.
Example:'''

# string = "hello"
# print(list(string))  # Output: ['h', 'e', 'l', 'l', 'o']

'''18. map()
	• Purpose: Applies a function to each element of the list and returns a map object 
 (convertible to a list).
Example:'''

# numbers = [1, 2, 3]
# squares = map(lambda x: x**2, numbers)
# print(list(squares))  # Output: [1, 4, 9]

'''19. filter()
	• Purpose: Filters elements in a list based on a condition (predicate) and returns 
 a filter object.
Example:'''

# numbers = [5, 3, 8, 1]
# greater_than_3 = filter(lambda x: x > 3, numbers)
# print(list(greater_than_3))  # Output: [5, 8]


'''20. zip()
	• Purpose: Combines multiple lists into a list of tuples.
Example:'''

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# print(list(zip(list1, list2)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

'''21. type()
	• Purpose: Returns the type of the object (useful to confirm an object is a list).
Example:'''

# my_list = [1, 2, 3]
# print(type(my_list))  # Output: <class 'list'>

'''21. id()
	• Purpose: Returns the memory address of the list object.
Example:'''
# my_list = [1, 2, 3]
# print(id(my_list))  # Output: Memory address (varies)

'''22. copy()
	• Purpose: Returns a shallow copy of the list.
Example:'''

# original = [1, 2, 3]
# copied = original.copy()
# print(original)
# print(copied)  # Output: [1, 2, 3]


'''G. List Iteration
	1. Using for Loop:'''

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
    
'''     2. Using while Loop:'''

# numbers = [1, 2, 3]
# i = 0
# l = leng(numbers)
# while i < l:
#     print(numbers[i])
#     i += 1

'''H. List Comprehension

	• A concise way to create lists.
	• Syntax: [expression for item in iterable if condition]
	• Example:'''

# numbers = [1, 2, 3, 4]
# squares = [x**2 for x in numbers]
# print(squares)  # Output: [1, 4, 9, 16]

'''I. Nested Lists
	• A list can contain other lists.
	• Access elements using multiple indices.
	• Example:'''

# nested = [[1, 2], [3, 4]]
# print(nested[0][1])  # Output: 2


'''A nested list is a list that contains other lists as its elements. In Python, lists can store any type of object, including other lists, allowing for a hierarchical or multi-level structure.

Example of a Nested List'''

# Nested list example
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''In this example:'''

'''The outer list has three elements.
Each element is itself a list.
Accessing Elements in a Nested List
You can use indexing to access specific elements. To access elements inside the inner lists, 
you need to chain indices.'''


# Access the second list
# print(nested_list[1])  # Output: [4, 5, 6]

# # Access the first element of the second list
# print(nested_list[1][0])  # Output: 4

# # Access the last element of the last list
# print(nested_list[2][2])  # Output: 9
'''Modifying a Nested List
You can modify elements inside nested lists by specifying their indices.'''


# nested_list[0][1] = 99  # Change the second element of the first list to 99
# print(nested_list)  # Output: [[1, 99, 3], [4, 5, 6], [7, 8, 9]]

'''Iterating Over a Nested List
You can use loops to iterate over nested lists.'''

'''Single-level iteration:'''

# for inner_list in nested_list:
#     print(inner_list)
    
# Output:
# [1, 99, 3]
# [4, 5, 6]
# [7, 8, 9]

'''Accessing individual elements:
python'''

# for inner_list in nested_list:
#     for element in inner_list:
#         print(element, end=" ")
# # Output: 1 99 3 4 5 6 7 8 9

'''Use Cases
Representing matrices or grids (e.g., for 2D games, spreadsheets).
Grouping related data hierarchically.
Nested lists are powerful for organizing and manipulating complex data structures.'''


'''J. Common Pitfalls
	1. Mutability:
	○ Modifications to one list can affect another if they're referencing the same object.'''

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)  # Output: [1, 2, 3, 4]
	
'''    2. Shallow Copy:
	○ Use .copy() or list() for a shallow copy.'''

# original = [1, 2, 3]
# copy = original.copy()
# copy.append(4)
# print(original)  # Output: [1, 2, 3]
# print(copy)

'''     3. Deep Copy: refers to creating a new object that is a completely independent copy of 
the original object, including all objects it contains (recursively).'''

'''This means:

Any changes made to the deep copy will not affect the original object, and vice versa.
It is a recursive operation, meaning that for objects containing other objects (like lists of lists, dictionaries containing other dictionaries, etc.), the nested objects are also copied.
Example:'''

# import copy

# # Original object
# original_list = [[1, 2, 3], [4, 5, 6]]

# # Deep copy
# deep_copied_list = copy.deepcopy(original_list)

# # Modify the deep copy
# deep_copied_list[0][0] = 99

# # Check both lists
# print("Original List:", original_list)      # Original List: [[1, 2, 3], [4, 5, 6]]
# print("Deep Copied List:", deep_copied_list) # Deep Copied List: [[99, 2, 3], [4, 5, 6]]

'''Key Characteristics:'''
'''Independent: Changes in the deep copy do not affect the original object. 
Recursion: Copies every nested object down to the most basic elements.'''

'''This is particularly useful when working with complex data structures 
like nested lists or dictionaries, where you want to ensure complete independence between the original and the copied objects.'''





# '''Practice'''

# Ex 1'''

# # my_list = list([1, 2,3, 5, 7])  # list() is called list constructor. 

# # print(my_list)
# # print(type(my_list))

# '''or'''

# # my_list = [1, 2,3, 5, 7]  # list() is called list constructor. 

# # print(my_list)
# # print(type(my_list))

# '''Ex 2'''

# # list_name = []
# # print(type(list_name))
# # print(list_name)
# # print(f"Empty list ={list_name}")

# '''Indext of list is classified into two Positive Index and Negative Index

# Positive Index: 0, 1, 2, 3, 4 (n-1)
# Negative Index: -5, -4, -3, -2, -1'''




# '''While loop with list'''

# '''Ex 3'''
    
# # fruit = ["apple", "mangoes", "Banana", "wood apple", False, True, 34, 4.5]
# # i = 0
# # while i < 4: 
# #     print(f"Fruit{i}:", fruit[i])
# #     i +=1


# '''or'''


# # fruit = ["apple", "mangoes", "Banana", "wood apple", False, True, 34, 4.5]
# # l = len(fruit)
# # i = 0
# # while i < l: 
# #     print(f"Fruit{i}:", fruit[i])
# #     i +=1

# '''3: Reverse the position of the item in list'''

# # fruit = ["apple", "mangoes", "Banana", "wood apple", False, True, 34, 4.5]

# # print(fruit[::-1])


# '''or'''

# # fruit = ["apple", "mangoes", "Banana", "wood apple", False, True, 34, 4.5]

# # i = -1
# # l = len(fruit)
# # while i >= -l:
# #     print(f"Fruit {i}", fruit[i])
# #     i -=1
    

# '''or'''

# # fruit = ["apple", "mangoes", "Banana", "wood apple", False, True, 34, 4.5]

# # i = 1
# # l = len(fruit)
# # while i <= l:
# #     print(f"Fruit {i}", fruit[-i])
# #     i +=1


# '''or'''
# # fruit = ["apple", "mangoes", "Banana", "wood apple", False, True, 34, 4.5]

# # l = len(fruit)
# # i = l-1
# # while i >=0:
# #     print(fruit[i])
# #     i -=1


# '''4'''

# # fruit = ["apple", "mangoes", "banana", "wood apple", False, True, 34, 4.5]

# # search = "banan"
# # i = 0
# # l = len(fruit)
# # while i < l:
# #     if search == fruit[i]:
# #         print(f"{search} is found in fruit.")
        
# #     i +=1


# '''5'''

# # namegroup = ["Jay", "Joe", "Mike", "John"]

# # name = input("Enter the name you like: ")

# # isfound = False
# # l = len(namegroup)
# # i = 0
# # while i <l:
# #     if name == namegroup[i]:
# #         print(f"{name} is found in the list.")
# #         isfound = True 
# #         break 
# #     i +=1

# # if not isfound:
# #     print("Not found")

# '''Nov 23, 2024'''

# '''Membership Operator'''
# # 1
# # number = [2, 3, 4, 5, 6, 7]
# # print(3 in number)

# # 2
# # number = [2, 3, 4, 5, 6, 7]
# # result = 3 not in number
# # print(3 in number)

# '''Identity Operator'''

# # l1 = [1, 2, 3]
# # l2= l1
# # print(l1 is l2)

# # l1 = [1, 2, 3]
# # l2 = [1, 2, 3]

# # print(l1 is not l2)

# '''Shallow copy'''

# # l1 = [1, 2, 3, 88, 99]
# # l2 = l1
# # l2[3] = 800

# # print(l1)
# # print(l2)


# '''Deep copy: ex: I have a house. Then Mr. B copy house style. 
# So, if Mr. B change some part of his house, it doesnt affect my house. It is called a deep copy
# We can use Two ways: 

# 1. I have to import the build-in function, " Copy" '''

# # import copy

# # l1 = [1, 2, 3, 88, 99, "Joe"]
# # l2 = copy.deepcopy(l1)
# # l2[0] = 12
# # print("L1 =", l1)
# # print("L2 =", l2)

# '''2_ I simply use the [:]'''

# # l1 = [1, 2, 3, 88, 99, "Joe"]
# # l2 = l1[:]  # [:] help l2 have it own value now. Even if I have change the value in the 
# list of l2, it does not affect l1. 
# # l2[0] = 12
# # print("L1 =", l1)
# # print("L2 =", l2)


# '''Slice list'''

# # l1 = [1, 2, 3, 88, 99, "Joe"]
# # l2 = l1[1:4]  # 1 is start and 4 is the (end - 1). ()

# # print("L1 =", l1)
# # print("L2 =", l2)


# '''or'''
# # l1 = [1, 2, 3, 88, 99, "Joe"]
# # l2 = l1[4:len(l1)]  # l1 is the length of the list ()

# # print("L1 =", l1)
# # print("L2 =", l2)

# '''or'''

# # l1 = [1, 2, 3, 88, 99, "Joe"]
# # l2 = l1[3:len(l1)] # 
# # l3 = l1[1:]   # " : "
# # print("L1 =", l1)
# # print("L2 =", l2)
# # print("l3 =", l3)


# '''For loop with list'''

# # l1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for item in (l1): # item is the name of the value in the list. We dont need initialization, we dont need to bok kern
# #     print(item)


# '''If I want the value starting from the middle of the list is the number even or odd: '''

# # l1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # l2 = l1[len(l1)//2:]

# # print("L2 =", l2)

# '''1'''

# # l1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # search = int(input("Enter number you want to find: "))
# # for item in l1:
# #     if item == search: 
# #         print(f"{search} is found in the list.")
        
        
# '''2'''

# # l1 = [ 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 10]
# # search = int(input("Enter number you want to find: "))
# # isfound = False
# # for item in l1:
# #     if item == search: 
# #         isfound = True
# # if isfound:
# #     print(f"{search} is found in the list.")
# # else:
# #     print(f"{search} is not found in the list.")
    
    
# '''Build in generate'''

# # _list = []
# # _list.append(1) # We can add only 1 value using the append function
# # _list.append(1)
# # _list.append(2)
# # print(_list)


# '''if I want to generage number 1 - 100, I can use For loop'''

# # _list = []
# # for item in range (1, 101):
# #     _list.append(item)
# # print(_list)



# '''or'''
# # _list = []
# # item = int(input("Enter the number of the number in the list: "))
# # for item in range (1, item+1):
# #     _list.append(item)
# # print(_list)


# '''But if we want the frequency of the number, we can use : '''
# # _list = []
# # item = int(input("Enter the number of the number in the list: "))
# # for i in range (5):
# #     _list.append(item)
# # print(_list)

# '''Add the number in the list 5 times'''
# # _list = []
# # for i in range (5):
# #     item = int(input("Enter the number you want to put in the list: "))
# #     _list.append(item)
# # print()

# '''Find the sum of the number in the list'''

# # _list = []
# # for i in range (5):
# #     item = int(input("Enter the number you want to put in the list: "))
# #     _list.append(item)
# # sum = 0
# # for item in _list:
# #     sum = sum + item
# # print(sum)


# '''or we can use the shortest way, using sum() function'''


# # _list = []
# # for i in range (5):
# #     item = int(input("Enter the number you want to put in the list: "))
# #     _list.append(item)    
# # print(sum(_list))



# '''Practice 1'''


# # my_list = [10, "apple", 12, 3.14, True]
# # print(my_list)

# # print(my_list[1]) # Or
# # print(my_list[-4])

# '''I. Select Element: '''
# # a = [1, 2, 4]
# # print(a[0])   # Output: 1
# # print(a[1])   # Output: 2
# # print(a[2])   # Output: 4 


# '''II. Update Element: '''
# # a = [1, 2, 3]
# # a[2]=5
# # print(a)
# # Output : [1, 2, 5]

# '''III. Add Element: 

# append() add the element at the end of a list

# insert() insert an element to a desired position of a list'''

# '''1'''

# # a = []

# '''I. Shallow Copy'''

# '''Example 1'''


# # original_list = [10, "apple", 12, 3.14, True]

# # print(f"Original list = {original_list}") # We print the original value first. 
# # copy_list = original_list
# # copy_list[2] = "Wood apple"
# # print(f"Copy_list ={copy_list}")


# '''Example 2'''
# '''But'''

# # original_list = [10, "apple", 12, 3.14, True]

# # copy_list = original_list
# # copy_list[2] = "Wood apple"

# # print(f"Original list = {original_list}") # The original list has been modified then the original list
# # # and copy list show the same output. 
# # print(f"Copy_list ={copy_list}")



# '''II. Deep copy:
# New position is created then the '''

# # original_list = [10, "apple", 12, 3.14, True]

# # copy_list = original_list.copy()  # or we can use [:] to replace. .copy()
# # copy_list[2] = "Wood apple"

# # print(f"Original list = {original_list}")  
# # print(f"Copy_list ={copy_list}")



# '''Buid-in function: function that is already created
# Ex: 
# len(): is the number of item in the list. It count the total number of the items. 
# length = len(list_name)
# print(length)'''
# '''If we are lazy to write 1 to number 100, we can use range to generate the number first, then copy 
# the number and pass in the list.'''

# # my_list = list(range(1,101))
# # print(my_list)

# # Pass the number in the list
# # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
# #            22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
# #            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
# #            60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
# #            80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
# #            ]
# # length = len(my_list)
# # print(length)


# '''III. Add element: Append/Insert'''

# '''Expression work as number
# Imput: work as statment'''

# '''IV. Remove element: remove()/ del'''



# '''Nov 24, 2024'''

# '''Built-in functions used with List in Python
# '''


# '''list: Converts an iterable (like a string, tuple, or set) to a list.'''

# # ss = (1,3,4)
# # print(type(ss))
# # print(list(ss))


# '''Sorted()'''
# 	# • Purpose: Returns a new list that is a sorted version of the original list.
# 	# • Example:

# # numbers = [5, 3, 8, 1]
# # print(sorted(numbers))       # Output: [1, 3, 5, 8]
# # print(sorted(numbers, reverse=True))  # Output: [8, 5, 3, 1]

# '''reverse'''

# # numbers = [5, 3, 8, 1]
# # print(list(reversed(numbers)))



# # zip()
# # 	• Purpose: Combines multiple lists into a list of tuples.
# # 	• Example:


# # list1 = [1, 2, 3]
# # list2 = ['a', 'b', 'c']
# # print(list(zip(list1, list2)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# nn = [3, 4, 2, 3, 4]
# print(dir(nn))

# ouput: the method we can used with list (['__add__', '__class__', '__class_getitem__', 
# '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
# '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
# 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'])

# print(help(nn))


'''Nov 29, 2024: Practice'''

'''We can use "len" function to measure the leng of string'''
# a = "I love you"
# print(len(a))  # output: 10
# a = ''' Hello my 
# friend. How are you doing?'''
# print(a)

'''Check the if a certain word or phrase is present in the string, we can use "in" operator '''

# a = "I love you baby."
# # print("you" in a) # output: True
# a = 'Check the if a certain word or phrase is present in the string, we can use "in" operator '
# print("check" in a) # output: False because "check" should begin with uppercase letter. 

