# String slicings :  Slicing of string means fetching a certain part of string from a particular strings
# we can slice stirngs from forwad as well as backward of a string
# Slicing string from backward can be referred to as negative slicing

# Each element indexing starts from 0
# For eg: name = "Nayan", here the indexing of N=0, a=1, y=2, a=3, n=4

name ="Nayan"
print(name[0:5]) # This givges output: nayan # Here the python interpreter will find the character at index value 0 and go for it till 5th( it's actually the 4th element but as i have told already indexing starts from 0 so 5 = 4th element which is (5-1) element. The same logic goes for other indexing/slicing methods too.
print(name[1:4]) # This gives output: aya
print(name[2:3]) # This gives output: y
print(name[-3:-2]) # This gives output: y
print(name[:-1]) # Python interpretor will add 0 automatically at the Left side so the range will be [0:-1] so the output will be: nayan
print(name[2:-1]) # the output will be: ya

#Length of the strings: Length of the string can be calculated by using the len function
length = len(name)
print("Name is "+str(length)+" character long") # This will give output: Name is 5 characters long

# Logic behind finding the negative indexing:
# Python interpreter is an intelligent stuff, it is a master of art. So in negative indexing what interpreter actually does is:

# eg: [-3:-2] = so, here python interpreter actually find the length of the string and subtracts the indexing value.

# so it will do like this : [len(name)-3: len(name)-2] = [5-3:5-2] = [2:3], so it will give the element from 2 indexing to 3(3-1 value) indexing.

# so this is the main logic behind the negative indexing

