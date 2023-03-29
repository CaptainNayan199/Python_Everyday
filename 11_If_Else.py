# condition in python: Condition statement in python are same as in other programming languages.
# few conditonal keywords are different in strucutres or else all are same.

#if elif else are main 3 conditional controlling structuring statement in python
# switch case statement are also there, we;ll see about them later on.


#conditional operator in python - they are used to see th relation between variables or any values.
# <, >, >, <=, ==, !=

a = int(input("Enter a number : "))
if a%2==0 and a!=0: #if this condition is met true, then get inside the print statement.
    print("Even")
elif a%2==1: # this will be tested if the above condition is false. # we dont use else if here in python, instead of using else if , elif is used which does the same exact job that esle if do in other languages.
    print("Odd")
else : # this is the final statement, if every above statement are false, then this will be tested and executed
    print("Zero")
    
    
# Nested if else statement in python - Nested if else means the use of if else inside some if else statement.

a = int(input("Enter a number : "))

if a>0:
    if a <=10:
        print("The number is betweeen 1 to 10")
    elif a >10 and a <=20:
        print("The number is between 11-20")
    else :
        print("Ther number is greater than 20")
elif a<0:
    print("Number is negative")
elif a==0:
    print("Number is zero")
else:
    print("Incorrect number provided")
    

# So, yeah this much for today, there are still many things in if else statement, but this is the basic way on how to use this structure.
# we will cover more detail on this strucutre later on while building some logic and stuffs.. Dont worry, we'll cover almost everything.
# Thank you!! Happy coding.

# In tomorrow session we will do some exercise on if else structure(), and be more familiar with 