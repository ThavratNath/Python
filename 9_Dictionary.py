'''Dictionary


Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:'''



'''ExampleGet your own Python Server
Create and print a dictionary:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


'''1. Dictionary Items

Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

Example
Print the "brand" value of the dictionary:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])


'''1.1. Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order 
will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.


1.2. Changeable

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has 
been created.

1.3 Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

Example
Duplicate values will overwrite existing values:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

'''1.4. Dictionary Length

To determine how many items a dictionary has, use the len() function:

Example

Print the number of items in the dictionary:

print(len(thisdict))


1.5. Dictionary Items - Data Types

The values in dictionary items can be of any data type:

Example
String, int, boolean, and list data types:'''

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]}

# print(thisdict)

''' 1.6 type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>
Example
Print the data type of a dictionary:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))   # Output: <class 'dict'>


'''1.7 The dict() Constructor

It is also possible to use the dict() constructor to make a dictionary.

Example
Using the dict() method to make a dictionary:'''

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict) 

# Output: {'name': 'John', 'age': 36, 'country': 'Norway'}


'''Note: 

Python Collections (Arrays)

>>There are four collection data types in the Python programming language:

1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.'''


'''2. Accessing Items

You can access the items of a dictionary by referring to its key name, inside square brackets:

Example

Get the value of the "model" key:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"] 
# print(x) # Output: Mustang

''' Or There is also a method called get() that will give you the same result:

Example
Get the value of the "model" key:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)   # Output: Mustang

'''2.2  Get Keys
The keys() method will return a list of all the keys in the dictionary.

Example
Get a list of the keys:'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()

print(x) # Output: dict_keys(['brand', 'model', 'year'])


'''The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary 
will be reflected in the keys list.

Example
Add a new item to the original dictionary, and see that the keys list gets updated as well:'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change # Ouput: dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change # Output: dict_keys(['brand', 'model', 'year', 'color'])


'''2.3 Get Values

The values() method will return a list of all the values in the dictionary.

Example
Get a list of the values:

x = thisdict.values()
The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

Example
Make a change in the original dictionary, and see that the values list gets updated as well:'''

# student = {"Name" : "Joe", "Age" : 23, "Birth Place": "Svay Rieng"}

# x = student.values()
# print(x)  # before change # Output: dict_values(['Joe', 23, 'Svay Rieng']) 

# student["Grade"] = 12

# print(x) # After changing the value: Output:  dict_values(['Joe', 23, 'Svay Rieng', 12])


'''2.4 Get Items

The items() method will return each item in a dictionary, as tuples in a list.

Example
Get a list of the key:value pairs'''

# student = {"Name" : "Joe", "Age" : 23, "Birth Place": "Svay Rieng"}

# x = student.items()
# print(x) # Output: dict_items([('Name', 'Joe'), ('Age', 23), ('Birth Place', 'Svay Rieng')])


'''The returned list is a view of the items of the dictionary, meaning that any changes done to the 
dictionary will be reflected in the items list.

Example
Make a change in the original dictionary, and see that the items list gets updated as well:'''


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change: output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# car["year"] = 2020

# print(x) #after the change : Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

'''Example
Add a new item to the original dictionary, and see that the items list gets updated as well:'''

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change: Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# car["color"] = "red"

# print(x) #after the change : # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])


'''2.5 Check if Key Exists

To determine if a specified key is present in a dictionary use the in keyword:

Example
Check if "model" is present in the dictionary:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
#   # Output: Yes, 'model' is one of the keys in the thisdict dictionary
  
  
'''3.1 Change Values
You can change the value of a specific item by referring to its key name:

ExampleGet your own Python Server
Change the "year" to 2018:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# print(thisdict) # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


'''3.2 Update Dictionary

The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

Example

Update the "year" of the car by using the update() method:'''


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


'''4. Python - Add Dictionary Items'''

'''4.1 Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

Example'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict) # Ouput: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

'''4.2 Update Dictionary

The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.

Example
Add a color item to the dictionary by using the update() method:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"}) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# print(thisdict)

'''5. Python - Remove Dictionary Items'''

'''5.1 Removing Items
There are several methods to remove items from a dictionary:

Example
The pop() method removes the item with the specified key name:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict) # Oupput: {"brand": "Ford", "year" : 1964}


'''Or. Example

The del keyword removes the item with the specified key name:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


'''5.2 del keyword
The del keyword can also delete the dictionary completely:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

'''5.2 clear() method

The clear() method empties the dictionary:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict) # {}


'''6. Python - Loop Dictionaries'''

'''6.1 Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Example

Print all key names in the dictionary, one by one:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964}
  
# for x in thisdict:
#   print(x)
  
#   # Output: 
# # brand
# # model
# # year

'''Example
Print all values in the dictionary, one by one:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964}
  
# for x in thisdict:
#   print(thisdict[x])
  
# #   Output: 
# # brand
# # model  
# # year   
# # Ford   
# # Mustang
# # 1964

'''Example
Loop through both keys and values, by using the items() method:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964}
# for x, y in thisdict.items():
#       print(x, y)
# # Output:
# # brand Ford
# # model Mustang
# # year 1964

'''7. Python - Copy Dictionaries'''

'''7. 1 Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Example
Make a copy of a dictionary with the copy() method:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

'''Another way to make a copy is to use the built-in function dict()
Example
Make a copy of a dictionary with the dict() function:'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


'''8. Python - Nested Dictionaries'''

'''8.1  Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

ExampleG
Create a dictionary that contain three dictionaries:'''

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
 
# print(myfamily)

# Ouput: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

'''Example
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:'''

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)

# #Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


'''Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

Example
Print the name of child 2:'''

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily["child2"]["name"]) # Ouput: Tobias


'''8.2 Loop Through Nested Dictionaries

You can loop through a dictionary by using the items() method like this:

Example
Loop through the keys and values of all nested dictionaries:'''

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for x, obj in myfamily.items():
#       print(x)

# for y in obj:
#     print(y + ':', obj[y])



'''9. Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary'''