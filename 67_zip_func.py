# So today we are going to see about a popular method in python, that is zip function.
# So what is zip function ?
# zip function is a special type of method in python that returns a zip object which is actually an iterator of tuples or list or any other iterable object in python.
# This function basically aggregates two or more iterables like sets, tuples, list, etc. After aggreation, it creates a tuples of zip elements.
# Let's see with an example

s_name = ["Nayan", "Ujjwal", "Roshan", "Tika", "Santosh"]
s_roll = [37, 37, 53, 69, 58]

zipped_elements = zip(s_name, s_roll)

for items in zipped_elements:
    print(items)
    
# Outputs : 
# ('Nayan', 37)
# ('Ujjwal', 37)
# ('Roshan', 53)
# ('Tika', 69)
# ('Santosh', 58)

# This is not only for any two indentical iterables objects in python, it can be dont in between two distinct objects as well.

s_name = ["Nayan", "Ujjwal", "Roshan", "Tika", "Santosh"]
s_roll = (37, 37, 53, 69, 58)

zipped_elements = zip(s_name, s_roll)

for items in zipped_elements:
    print(items)

# The output is same as that of previous one.

# So its simple; zip functions aggregates the items of two or more iterables objects and store them in the form of tuples.