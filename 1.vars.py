"""
    This is the doc string of this module (file/package)
    It's used to describe the functionality (usage) of the module,
    and provide detailed descriptions of code for users

    this doc string is often processed by developers tools like Sphinx to generate documentation
    for more information see: https://www.datacamp.com/tutorial/docstrings-python
    and https://www.python.org/dev/peps/pep-0257/

    while comments are used in general to explain context and provide background
    for a specific block of code, docstrings are used to document the entire module
    function, or class (user-defined data type)

    documentation includes use cases, parameters, and return values

    comments can be used also as a way to disable sections of code
    so that they are not executed by the interpreter when the program is run

    the interpreter is a program that reads your python code and executes it
    by translating it into machine code (zeros and ones '001001110') and running it
    line by line in real-time.
"""

# int values
number = 3
double_the_number = number * 2
print(double_the_number)

number = number + 15
print(number)

number += 1
print(number)

number *= 2
print(number)

# =============== Strings ==========
# are sequences of characters
# they are written in double quotes or single quotes
# they are immutable (cannot be changed)
# they are used to represent text
# str (string) values
name = "john"
print(name)

name += " Doe" # add (concatenate) " Doe" to "john"
print(name)

print("Hi " * 3) # print "Hi " 3 times as a single string

# =============== Float Values ==========
# are real numbers
# they are written with decimal points
# they are used to represent numbers with decimal places
# float (floating point) values
pi = 3.14159
print(pi)

# =============== Complex Values ==========
# are complex numbers
# they are written with the j symbol
# they are used to represent complex numbers
# complex (complex number) values
complex = 2 + 3j
print(complex)

# =============== Boolean Types ==========
# are used primarily for conditional statements (if, elif, else statements)
# values are either True or False

is_raining = True
if is_raining:
    print("It's raining outside")
else:
    print("It's not raining outside")

is_cloudy = False

# as there is binary operators for int and float data types
# like +, -, *, /, //, %, ** use to do arithmitic operations
# there is aslo conditional operators like ==, !=, >, <, >=, <=, and, or, not
# use to do boolean operations on values of boolean data types
if is_cloudy and is_raining:
    print("It's cloudy and raining outside")
else:
    print("It's not cloudy or raining outside")

print(15 == 15)
print(10 < 3)
print(10 <= 3)

# =============== None Type ==========
# is used to represent the absence of a value
# it is also used to represent the absence of a variable

x = None
print(x)
