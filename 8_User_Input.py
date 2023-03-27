# Taking user input in python - Input from user can be asked/taken by the use of input() function in python.
# input() function gives a return value as string/character.
# input() function returns the value as a string, so we have to type cast it another data type as per 
# requirement.
a = input("Give me anything ") # String input is being taken. It is default user input
b = int(input("Give me something ")) # int input is being taken by following type casting method
c = float(input("Give me some something ")) # float input is being taken by following type casting method
print(a,b,c)