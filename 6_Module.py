'''Nov 3, 2024'''
''' Lets call the code in file to run. That code is in function. Whe we call it, it will b executed? '''

# import function             # function is the name of the file
# function.greeting()         # greeting is the name of the function in the file (function, which is a file name)
# function.display()
# function.me()


'''or'''

# import function as fu
# fu.greeting()             # If I want to find the place where the code is store,  I just use Control + and click greeting)
# fu.display()
# fu.me()

'''Or'''

# from function import greeting, display, me
# greeting()
# display()
# me()



# from function import*       # import* will allow us to call all functions in the other file (function)
# greeting()
# display()
# me()





'''Swapping variable'''

# a = 10
# b = 20

# temp = a
# a = b
# b = temp 

# print(a)
# print(b)



# file = open('filename.txt', 'w')
# file.write('This is my data. ')

'''In Python, a **module** is a file containing Python definitions and statements. Modules allow you to organize your code into manageable parts and reuse it across different programs. Here's an overview of how modules work in Python:

### Creating a Module
To create a module, you simply write your Python code in a file with a `.py` extension. For example, you could create a file named `mymodule.py`:

```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b
```

### Importing a Module
To use the functions and variables defined in a module, you need to import the module into your script:

```python
import mymodule

print(mymodule.greet("Thavrat"))  # Output: Hello, Thavrat!
print(mymodule.add_numbers(5, 7))  # Output: 12
```

### Importing Specific Functions or Variables
You can also import specific functions or variables from a module:

```python
from mymodule import greet, add_numbers

print(greet("Thavrat"))  # Output: Hello, Thavrat!
print(add_numbers(5, 7))  # Output: 12
```

### Renaming a Module
If you want to use a shorter name for a module, you can use the `as` keyword to give it an alias:

```python
import mymodule as mm

print(mm.greet("Thavrat"))  # Output: Hello, Thavrat!
```

### Built-in Modules
Python comes with a standard library of modules that you can use without installing anything extra. For example, the `math` module provides access to mathematical functions:

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

### Third-Party Modules
You can also install third-party modules using a package manager like `pip`. For example, to install and use the `requests` module for making HTTP requests:

```bash
pip install requests
```

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200
```

### Writing Modules for Reuse
When writing modules for reuse, it's important to follow good practices like:

- Organizing related functions and classes into the same module.
- Providing docstrings for functions and classes to explain their purpose.
- Using the `if __name__ == "__main__":` construct to allow the module to be run as a script or imported without executing code unintentionally.

```python
# mymodule.py

def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    print(greet("Thavrat"))
    print(add_numbers(5, 7))
```

This setup allows the module to be imported without running the code under the `if __name__ == "__main__":` block.

Let me know if you'd like more details or examples on specific aspects of using modules!'''

'''Example of imporint other code from other file: '''

# import Function
# print(Function.calculator)
# print(Function._List)


'''Three modes in Files
- r
- w
- a
'''



