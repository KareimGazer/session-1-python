# A program is a set of instructions for a computer.
# A program is made up of lines of code.
# Each line tells the computer a particular detail of those instructions.

# programs that give instructions to turtles in order to make them create 
# different shapes and patterns. 
# You can think of turtles as virtual robots that know how to draw lines on the screen, 
# following commands such as forward, back, left, and right

# here the first line is importing (bringing) a module (package) called turtle
# a module is a collection of code (instructions) that gives us all we need
# to create and control turtles
import turtle

# here we create a turtle "Turtle" from that module
# and assign it to a variable called fred
# get the code of the turtle from the module
# and call it using () to create a turtle and assign it to the variable fred
fred = turtle.Turtle()

# the turtle can do different things
# and every it can do is called a method
# we use a method by calling the variable name then a dot then the name of the method

# for example the turtle can change its color with the color method
fred.color("red")

# here we call the forward method to move the turtle forward by 100 pixels
fred.forward(100)

# here we call the right method to turn the turtle 135 degrees to the right
fred.right(135)

# and so on
fred.forward(140)
fred.right(135)
fred.forward(100)