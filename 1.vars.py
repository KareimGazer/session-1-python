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

# variable names are case sensitive
# variable names must start with a letter or an underscore
# variable names cannot start with a number
# variable names can only contain alpha numeric characters and underscores
# variables are a way to refer to data values
# some words are reserved and cannot be used as variable names
# meaning they are reserved for special use by the python language
# A variable is a connection between a name in the code and some data in memory.

# The reason we call it a variable is because it is able to vary. 
# We can first say that this name refers to some data in one place in memory, 
# but then later in our program we could change it so that the same name refers 
# to some other data in a different location.
# for example
x = 10
x = "hello"
print(x)

# that make python what is called a dynamically typed language
# that means the type of the variable can be changed during the execution of the program (runtime)
# the type of the variable is determined by the value assigned to it
# for example
x = 10 # int data type
x = "hello" # str data type
print(x)

# there are other data types in python
# for example
x = 10 # int data type
x = "hello" # str data type
x = 10.5 # float data type
x = True # bool data type
x = None # None data type - no value
# any other type of value not listed in these previous examples is a user defined data type (class)
# meaning that it is a custom data type that we can define and use
# and each value of that type is called an instance (object) of that class

# spacing in python is important and is used to separate code into
# different blocks of code (groups of statements) as we will see in loops and if statements

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

# error message does not mean you are a bad programmer
# instead it means the computer can't understand your code
# use errors to help yourself learn and grow

# print(3 + "hello") # generates and error

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


## ToDO: Type annotations