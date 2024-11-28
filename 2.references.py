# python string are immutable (don't change)
# so they are written in the memory only once

# in the first case name1 and name2 point to different strings
name1 = 'john'
name2 = 'joudy'
print(id(name1) == id(name2))
# is is an operator that is the same as doing id(name1) == id(name2)
print(name1 is name2) 

# now since the strings are the same no need to write it twice
# so both will point to the same string
name1 = 'john'
name2 = 'john'
print(name1 is name2)

# here since list are mutable (can be changed)
# each variables will point to a different copy in memory
numbers1 = [1, 2, 3]
numbers2 = [1, 2, 3]
print(numbers1 is numbers2)