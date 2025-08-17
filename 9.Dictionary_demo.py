
'''1. What is a Dictionary in Python?

A dictionary is a collection of key-value pairs, where each key is unique, and is used to retrieve its 
associated value.'''

'''======================================================================================================================='''

'''1. Syntax

dictionary_name = {key1: value1, key2: value2, ...}'''

'''======================================================================================================================='''
'''2. Creating a Dictionary'''

'''2.1: Empty Dictionary'''

empty_dict = {}
print(empty_dict)  # Output: {}

'''2.2: Dictionary with Data'''

person = { "name": "Alice", "age": 30, "city": "New York"}
print(person) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

'''======================================================================================================================='''
'''3. Accessing Values'''

'''3.1 Using Keys'''

person = { "name": "Alice", "age": 30, "city": "New York"}
print(person["name"]) # Output: Alice

'''3.2 3.2 Using .get()'''

person = { "name": "Alice", "age": 30, "city": "New York"}
print(person.get("age"))  # Output: 30
print(person.get("gender"))  # Output: None

'''======================================================================================================================='''
'''4. Adding and Updating Items'''

'''4.1  Add New Key-Value Pairs'''

person = { "name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "Male"
print(person)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'gender': 'Male'}

'''4.2  Update Existing Values'''

person = {"name": "Alice", "age": 30, "city": "New York"}
person["age"] = 60
print(person)
#Output: {'name': 'Alice', 'age': 60, 'city': 'New York'}
'''======================================================================================================================='''
'''5. Removing Items'''

'''5.1 Using del
Removes a key-value pair.'''

person = {"name": "Alice", "age": 30, "city": "New York"}
del person["city"]
print(person) 
# Output: {'name': 'Alice', 'age': 30}

'''5.2 Using .pop()
Removes a key-value pair and returns the value.'''

person = {"name": "Alice", "age": 30, "city": "New York"}
person.pop("name")
print(person)
# Output: {'age': 30, 'city': 'New York'}

'''5.3 Using .popitem()
Removes the last inserted key-value pair.'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
last_item = person.popitem()
print(last_item)  
# Output: ('gender', 'Male')

'''======================================================================================================================='''
'''6. Iterating Over a Dictionary
6.1 Loop Through Keys'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
for key in person:
    print(key)
# Output
# name
# age   
# city  
# gender

'''6.2 Loop Through values'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
for values in person.values():
    print(values)

# Output
# Alice
# 30
# New York
# Male

'''6.3 Loop Through Key-Value Pairs'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
for key, value in person.items():
    print(f"{key}: {value}")
# Output
# name: Alice
# age: 30
# city: New York
# gender: Male
'''======================================================================================================================='''
'''7. Common Dictionary Methods'''

'''7.1. keys()
Returns a view of the keys.'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
print(person.keys())
# Output: dict_keys(['name', 'age', 'city', 'gender'])

'''7.2 values()
Return the values of keys'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
print(person.values())
#Output: dict_values(['Alice', 30, 'New York', 'Male'])

'''7.3 items()
Returns a view of key-value pairs.'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
print(person.items())
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York'), ('gender', 'Male')])

'''7.4 clear()
Removes all items.'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
person.clear()
print(person) 
# Output: {}

'''or'''

person = {"name": "Alice", "age": 30, "city": "New York", "gender": "Male"}
print(person.clear()) 
# Output: None

'''======================================================================================================================='''